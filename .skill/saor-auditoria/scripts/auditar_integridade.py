#!/usr/bin/env python3
"""SaOr — verificações físicas e referenciais determinísticas (GVA-4).

Executor SOMENTE LEITURA; não edita, extrai, corrige nem salva resultados.
A SPEC canônica, o contrato do domínio e a Skill são autoridades sobre
requisitos, Gates, interpretações e aprovações. Este programa não os aprova.

Exemplo de uso (saída JSON exclusivamente em stdout):
    python -B .skill/saor-auditoria/scripts/auditar_integridade.py \
      --source /caminho/clone.zip --scope .specs --scope .skill \
      --mode SOB_DEMANDA --domain generic \
      --classification-reviewed --legacy-basis .specs/PROCESSO-ALTERACAO-ASSISTIDA.md

Antes de executar, classificar os LEGADOS nas normas, fornecer
--classification-reviewed e --legacy-basis, e usar --legacy-path para
cada caminho excluído. O programa NÃO presume que a
classificação de LEGADO possa ser inferida pelo nome do arquivo.

Códigos: 0 = verificações automáticas sem defeito comprovado; 2 = defeito
físico/referencial comprovado; 3 = impedimento de segurança ou integridade;
1 = entrada inválida/erro de execução. Zero NÃO representa encerramento.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import struct
import sys
import unicodedata
import warnings
from urllib.parse import unquote, urlsplit
import zipfile

SCRIPT_VERSION = 'GVA-4.1'
HASH_CLASSES = {
    'HASH_FISICO_ATUAL', 'HASH_SUBMISSAO_OU_APROVACAO',
    'HASH_VERSAO_FORMAL_ANTERIOR', 'HASH_AJUSTE_SUBSTITUIDO',
    'HASH_DE_ORIGEM_DOCUMENTADA', 'HASH_SEM_CLASSIFICACAO',
}
SHA256_RE = re.compile(r'^[0-9a-fA-F]{64}$')
LINK_RE = re.compile(r'!?\[[^\]\n]*\]\((?:<([^>\n]*)>|([^\s)]+))(?:\s+["\'][^)]*["\'])?\)')
WINDOWS_DRIVE_RE = re.compile(r'^[a-zA-Z]:')
STATUS = ('CONFORME', 'NÃO CONFORME', 'NÃO VALIDADO', 'PENDENTE', 'NÃO APLICÁVEL', 'BLOQUEADO')
CHUNK = 1024 * 1024


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def hash_stream(stream, limit: int):
    dig = hashlib.sha256()
    total = 0
    while True:
        block = stream.read(CHUNK)
        if not block:
            break
        total += len(block)
        if total > limit:
            raise ValueError('limite de bytes do arquivo excedido')
        dig.update(block)
    return total, dig.hexdigest()


def protected(path: str) -> bool:
    """Proíbe acesso a qualquer segmento assets, inclusive sob raiz ZIP."""
    return any(c.casefold() == 'assets' for c in path.replace('\\', '/').split('/'))


def archive_path(raw: str):
    """Retorna caminho canônico ou razão de rejeição, sem ler o membro."""
    if not raw or '\x00' in raw or '\\' in raw:
        return None, 'caminho ZIP vazio, nulo ou com separador não canônico'
    if raw.startswith('/') or WINDOWS_DRIVE_RE.match(raw):
        return None, 'caminho ZIP absoluto'
    # Um diretório ZIP usa uma única barra terminal; barras repetidas não
    # são um nome canônico e não devem ser removidas silenciosamente.
    pieces = (raw[:-1] if raw.endswith('/') else raw).split('/')
    if any(p in ('.', '..', '') for p in pieces):
        return None, 'normalização perigosa ou travessia de diretórios no ZIP'
    if any(any(ord(c) < 32 for c in p) for p in pieces):
        return None, 'caractere de controle no caminho ZIP'
    return '/'.join(pieces), None


def selector(raw: str) -> str:
    if not raw or raw in ('.', './'):
        return ''
    raw = raw.rstrip('/')
    name, error = archive_path(raw)
    if error:
        raise ValueError(f'escopo ou exclusão inválido: {error}')
    return name


def matches(path: str, pattern: str) -> bool:
    return not pattern or path == pattern or path.startswith(pattern + '/')


def resolve_relative(origin: str, destination: str):
    """Resolve Markdown com '..' legítimo, sem permitir saída da raiz."""
    if not destination or destination.startswith('#'):
        return None, 'âncora interna (sem destino físico separado)'
    split = urlsplit(destination)
    if split.scheme or split.netloc or destination.startswith('//'):
        return None, 'URL externa ou protocolo não local'
    path = unquote(split.path)
    if not path or '\\' in path or path.startswith('/') or WINDOWS_DRIVE_RE.match(path):
        return None, 'destino vazio, absoluto ou com separador não canônico'
    if any(ord(c) < 32 for c in path):
        return None, 'destino contém caractere de controle'
    elements = origin.split('/')[:-1]
    for part in path.split('/'):
        if part in ('', '.'):
            continue
        if part == '..':
            if not elements:
                return None, 'link relativo tenta escapar da raiz'
            elements.pop()
        else:
            elements.append(part)
    if not elements:
        return None, 'destino sem arquivo'
    resolved = '/'.join(elements)
    if protected(resolved):
        return None, 'referência protegida: não acessar assets/'
    return resolved, None


class Auditor:
    def __init__(self, opts):
        self.opts = opts
        self.scopes = [selector(v) for v in opts.scope]
        if any(protected(p) for p in self.scopes):
            raise ValueError('escopo protegido assets/ não pode ser selecionado')
        self.legacy = [selector(v) for v in opts.legacy_path]
        self.exclude = [selector(v) for v in opts.exclude_path]
        self.entries = {}
        self.directories = set()
        self.locators = {}
        self.issues = []
        self.findings = []
        self.base_identity = {}
        self.source_type = None
        self.zipobj = None
        self.root_dir = None
        self.zip_prefix = ''
        self.total_bytes = 0
        self.exclusion_counts = {'assets': 0, 'legado': 0, 'adicional': 0, 'fora_escopo': 0}
        self.limits = [
            'Verificação automatizada não substitui leitura semântica, inspeção visual ou aprovação humana.',
            'Classificação de LEGADO depende de norma conferida pelo responsável; --legacy-path não a autentica.',
            'Links Markdown são detectados por parser restrito a links inline; links de referência, HTML e código não são cobertos.',
            'SHA-256 de submissão e decisão humana não são autenticados automaticamente por igualdade com bytes atuais.',
            'Nenhum controle especializado ou Gate recebe CONFORME automaticamente apenas pelo relatório deste script.',
        ]

    def issue(self, kind, state, detail, path=None, **extra):
        data = {'tipo': kind, 'estado': state, 'detalhe': detail}
        if path is not None:
            data['caminho'] = path
        data.update(extra)
        self.issues.append(data)

    def selected(self, path):
        if protected(path):
            self.exclusion_counts['assets'] += 1
            return False
        if any(matches(path, p) for p in self.legacy):
            self.exclusion_counts['legado'] += 1
            return False
        if any(matches(path, p) for p in self.exclude):
            self.exclusion_counts['adicional'] += 1
            return False
        if not any(matches(path, p) for p in self.scopes):
            self.exclusion_counts['fora_escopo'] += 1
            return False
        return True

    def detect_container(self):
        p = Path(self.opts.source)
        if p.is_symlink() or protected(p.as_posix()) or protected(str(p.resolve())):
            raise ValueError('fonte aponta para link simbólico ou assets/ protegido')
        if p.is_file():
            if not zipfile.is_zipfile(p):
                raise ValueError('fonte regular não é ZIP estruturalmente válido')
            self.source_type = 'zip'
            with p.open('rb') as inp:
                size, sha = hash_stream(inp, self.opts.max_total_bytes)
            self.base_identity = {'tipo': 'zip', 'tamanho_bytes': size, 'sha256': sha}
            self.zipobj = zipfile.ZipFile(p, 'r')
        elif p.is_dir():
            self.source_type = 'directory'
            self.root_dir = p.resolve(strict=True)
            self.base_identity = {'tipo': 'diretorio', 'localizacao': str(p), 'sha256_container': None,
                                  'nota': 'diretórios não possuem SHA-256 de contêiner; identidades são por arquivo'}
        else:
            raise ValueError('fonte inexistente ou tipo não suportado')

    def zip_root(self, infos):
        # Detecta somente através de uma âncora canônica disponível entre caminhos elegíveis.
        candidates = set()
        for obj in infos:
            raw = obj.filename
            if protected(raw):
                continue
            norm, err = archive_path(raw)
            if err or not norm:
                continue
            suffix = '.specs/PROCESSO-ALTERACAO-ASSISTIDA.md'
            if norm == suffix:
                candidates.add('')
            elif norm.endswith('/' + suffix):
                candidates.add(norm[:-len(suffix)])
        if len(candidates) == 1:
            return next(iter(candidates))
        if len(candidates) > 1:
            self.issue('zip_raiz_ambigua', 'BLOQUEADO', 'múltiplas raízes canônicas candidatas')
        else:
            self.limits.append('Raiz do ZIP não demonstrada por norma canônica; caminhos são relativos ao próprio ZIP.')
        return ''

    def enumerate_zip(self):
        infos = self.zipobj.infolist()
        self.zip_prefix = self.zip_root(infos)
        preflight = []
        seen = {}
        seen_case = {}
        for info in infos:
            original = info.filename
            if protected(original):
                self.exclusion_counts['assets'] += 1
                continue
            path, err = archive_path(original)
            if err:
                self.issue('caminho_inseguro', 'BLOQUEADO', err)
                continue
            if path is None:
                continue
            if self.zip_prefix:
                if path == self.zip_prefix.rstrip('/') and info.is_dir():
                    # A raiz explícita também precisa ter metadados compatíveis.
                    mode = (info.external_attr >> 16) & 0xFFFF
                    ftype = stat.S_IFMT(mode)
                    if ftype and ftype != stat.S_IFDIR:
                        self.issue('tipo_zip_incompativel', 'BLOQUEADO',
                                   'tipo Unix da raiz ZIP incompatível com diretório', path)
                    continue  # entrada de diretório-raiz não é uma segunda raiz
                if not path.startswith(self.zip_prefix):
                    self.issue('raiz_mista', 'BLOQUEADO', 'entrada fora da raiz canônica detectada')
                    continue
                path = path[len(self.zip_prefix):]
            if not path:
                continue
            if not self.selected(path):
                continue
            normcase = unicodedata.normalize('NFC', path).casefold()
            if path in seen:
                kind = 'colisao_arquivo_diretorio' if seen[path] != info.is_dir() else 'duplicidade'
                self.issue(kind, 'BLOQUEADO', 'membros ZIP incompatíveis no mesmo caminho', path)
                continue
            if normcase in seen_case:
                _, previous_is_dir = seen_case[normcase]
                kind = ('colisao_arquivo_diretorio' if previous_is_dir != info.is_dir()
                        else 'colisao_case_unicode')
                self.issue(kind, 'BLOQUEADO',
                           'colisão de nome ignorando caixa/normalização Unicode', path)
                continue
            seen[path] = info.is_dir()
            seen_case[normcase] = (path, info.is_dir())
            mode = (info.external_attr >> 16) & 0xFFFF
            ftype = stat.S_IFMT(mode)
            if ftype and ftype not in (stat.S_IFDIR, stat.S_IFREG):
                self.issue('entrada_especial', 'BLOQUEADO', 'link simbólico ou entrada especial ZIP', path)
                continue
            if ((ftype == stat.S_IFDIR and not info.is_dir())
                    or (ftype == stat.S_IFREG and info.is_dir())):
                self.issue('tipo_zip_incompativel', 'BLOQUEADO',
                           'tipo Unix declarado diverge da representação do membro ZIP', path)
                continue
            if info.is_dir():
                self.directories.add(path)
                continue
            if info.file_size > self.opts.max_file_bytes:
                self.issue('limite_expansao', 'BLOQUEADO', 'tamanho expandido excede limite por arquivo', path)
                continue
            preflight.append((path, info))
        # Uma entrada regular não pode representar também um diretório explícito
        # ou um ancestral implícito de outra entrada. Conferir antes de ler bytes.
        required_directories = set()
        for path in self.directories:
            required_directories.add(unicodedata.normalize('NFC', path).casefold())
        for path in list(self.directories) + [name for name, _ in preflight]:
            segments = path.split('/')
            for depth in range(1, len(segments)):
                parent = '/'.join(segments[:depth])
                required_directories.add(unicodedata.normalize('NFC', parent).casefold())
        for path, _ in preflight:
            if unicodedata.normalize('NFC', path).casefold() in required_directories:
                self.issue('colisao_arquivo_diretorio', 'BLOQUEADO',
                           'arquivo regular coincide com diretório explícito ou ancestral implícito', path)
        total_uncompressed = sum(info.file_size for _, info in preflight)
        if total_uncompressed > self.opts.max_total_bytes:
            self.issue('limite_expansao', 'BLOQUEADO', 'expansão total excede limite permitido')
            return
        for path, info in preflight:
            try:
                with self.zipobj.open(info, 'r') as f:
                    size, sha = hash_stream(f, self.opts.max_file_bytes)
                if size != info.file_size:
                    self.issue('tamanho', 'NÃO CONFORME', 'tamanho real diferente do catálogo ZIP', path)
                    continue
                self.entries[path] = {'caminho': path, 'tamanho_bytes': size, 'sha256': sha,
                                      'tipo': self.file_type(path), 'crc_zip_verificado': True}
                self.locators[path] = info
                self.total_bytes += size
            except (OSError, ValueError, RuntimeError, EOFError, NotImplementedError, zipfile.BadZipFile) as exc:
                self.issue('integridade_zip', 'BLOQUEADO', type(exc).__name__ + ': erro na leitura/CRC', path)

    @staticmethod
    def file_type(path):
        suffix = PurePosixPath(path).suffix.casefold()
        if suffix in ('.md', '.txt', '.json', '.csv', '.yaml', '.yml', '.py', '.toml', '.svg'):
            return 'texto_candidato'
        if suffix == '.png':
            return 'png_candidato'
        return 'binario_ou_outro'

    def enumerate_directory(self):
        def onerror(exc):
            self.issue('erro_diretorio', 'BLOQUEADO', type(exc).__name__ + ': falha na enumeração')
        seen_case = {}
        for root, directories, filenames in os.walk(self.root_dir, topdown=True, followlinks=False, onerror=onerror):
            base = Path(root)
            kept = []
            for name in directories:
                candidate = base / name
                relative = candidate.relative_to(self.root_dir).as_posix()
                if protected(relative):
                    self.exclusion_counts['assets'] += 1
                    continue
                if any(matches(relative, p) for p in self.legacy + self.exclude):
                    continue
                # Nunca percorrer subárvores sem interseção com o escopo solicitado.
                if not any(matches(relative, p) or matches(p, relative) for p in self.scopes):
                    continue
                if candidate.is_symlink():
                    self.issue('symlink', 'BLOQUEADO', 'diretório é link simbólico', relative)
                    continue
                self.directories.add(relative)
                kept.append(name)
            directories[:] = kept
            for name in filenames:
                target = base / name
                relative = target.relative_to(self.root_dir).as_posix()
                if not self.selected(relative):
                    continue
                if target.is_symlink():
                    self.issue('symlink', 'BLOQUEADO', 'arquivo é link simbólico', relative)
                    continue
                case_key = unicodedata.normalize('NFC', relative).casefold()
                if case_key in seen_case and seen_case[case_key] != relative:
                    self.issue('colisao_case_unicode', 'BLOQUEADO',
                               'colisão de arquivos ignorando caixa/normalização Unicode', relative)
                    continue
                seen_case[case_key] = relative
                try:
                    st_before = target.lstat()
                    if not stat.S_ISREG(st_before.st_mode):
                        self.issue('arquivo_especial', 'BLOQUEADO', 'arquivo não regular', relative)
                        continue
                    if st_before.st_size > self.opts.max_file_bytes:
                        self.issue('limite_expansao', 'BLOQUEADO', 'arquivo excede limite de bytes', relative)
                        continue
                    if self.total_bytes + st_before.st_size > self.opts.max_total_bytes:
                        self.issue('limite_total', 'BLOQUEADO', 'limite agregado de bytes excedido', relative)
                        continue
                    canonical = target.resolve(strict=True)
                    if not canonical.is_relative_to(self.root_dir) or protected(canonical.as_posix()):
                        self.issue('caminho_protegido', 'BLOQUEADO',
                                   'arquivo resolve fora da raiz ou dentro de assets/', relative)
                        continue
                    descriptor = os.open(target, os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0))
                    with os.fdopen(descriptor, 'rb') as f:
                        size, sha = hash_stream(f, self.opts.max_file_bytes)
                        st_after = os.fstat(f.fileno())
                    if (st_before.st_size != size or st_after.st_ino != st_before.st_ino
                            or st_after.st_dev != st_before.st_dev
                            or st_after.st_mtime_ns != st_before.st_mtime_ns):
                        self.issue('arquivo_instavel', 'NÃO VALIDADO', 'arquivo alterado durante leitura', relative)
                        continue
                    self.entries[relative] = {'caminho': relative, 'tamanho_bytes': size,
                                               'sha256': sha, 'tipo': self.file_type(relative),
                                               'crc_zip_verificado': None}
                    self.locators[relative] = target
                    self.total_bytes += size
                except (OSError, ValueError) as exc:
                    self.issue('leitura', 'BLOQUEADO', type(exc).__name__ + ': falha na leitura', relative)

    def content(self, path: str) -> bytes:
        if not path in self.entries or protected(path):
            raise ValueError('arquivo não elegível ou não verificado')
        if self.source_type == 'zip':
            with self.zipobj.open(self.locators[path], 'r') as f:
                raw = f.read(self.opts.max_file_bytes + 1)
        else:
            p = self.locators[path]
            if p.is_symlink() or protected(str(p.resolve())):
                raise ValueError('arquivo tornou-se link simbólico ou protegido')
            descriptor = os.open(p, os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0))
            with os.fdopen(descriptor, 'rb') as inp:
                raw = inp.read(self.opts.max_file_bytes + 1)
        if (len(raw) != self.entries[path]['tamanho_bytes']
                or sha256_bytes(raw) != self.entries[path]['sha256']):
            raise ValueError('arquivo mudou desde a leitura física inicial')
        return raw

    def index_parent_directories(self):
        for path in self.entries:
            parts = path.split('/')
            for n in range(1, len(parts)):
                self.directories.add('/'.join(parts[:n]))

    def link_checks(self):
        results = []
        if not self.opts.check_links:
            return results
        for path in sorted(self.entries):
            if not path.lower().endswith('.md'):
                continue
            try:
                raw = self.content(path)
                text = raw.decode('utf-8-sig')
            except (UnicodeDecodeError, ValueError, OSError, RuntimeError, NotImplementedError, zipfile.BadZipFile):
                self.issue('markdown', 'NÃO VALIDADO', 'não foi possível ler/decodificar Markdown', path)
                continue
            in_fence = False
            for number, line in enumerate(text.splitlines(), 1):
                stripped = line.lstrip()
                if stripped.startswith('```') or stripped.startswith('~~~'):
                    in_fence = not in_fence
                    continue
                if in_fence:
                    continue
                line = re.sub(r'`[^`]*`', '', line)
                for match in LINK_RE.finditer(line):
                    target = match.group(1) if match.group(1) is not None else match.group(2)
                    resolved, reason = resolve_relative(path, target)
                    item = {'origem': path, 'linha': number, 'referencia': target,
                            'destino': resolved}
                    if resolved is None:
                        if reason.startswith('link relativo'):
                            item['estado'] = 'BLOQUEADO'
                            self.issue('link_inseguro', 'BLOQUEADO', reason, path, linha=number)
                        elif reason.startswith('referência protegida'):
                            item['estado'] = 'NÃO VALIDADO'
                            item['limite'] = 'referência a assets/ registrada, destino excluído da inspeção'
                        else:
                            item['estado'] = 'NÃO APLICÁVEL'
                            item['limite'] = reason
                    elif resolved in self.entries or resolved in self.directories:
                        item['estado'] = 'CONFORME'
                        item['tipo_destino'] = 'arquivo' if resolved in self.entries else 'diretorio'
                    elif resolved in self.locators:
                        item['estado'] = 'NÃO VALIDADO'
                    elif protected(resolved) or any(matches(resolved, p) for p in self.legacy + self.exclude):
                        item['estado'] = 'NÃO APLICÁVEL'
                        item['limite'] = 'destino excluído do escopo de leitura'
                    elif not any(matches(resolved, p) for p in self.scopes):
                        item['estado'] = 'NÃO VALIDADO'
                        item['limite'] = 'destino fora do escopo analisado'
                    else:
                        item['estado'] = 'NÃO CONFORME'
                        self.issue('referencia_quebrada', 'NÃO CONFORME',
                                   'destino local do link não existe no conjunto verificado', path, linha=number, destino=resolved)
                    results.append(item)
        return results

    def hash_occurs_at_source_line(self, source: str, line: int, declared: str) -> bool:
        """Confirma que a referência foi realmente impressa na origem apontada."""
        try:
            lines = self.content(source).decode('utf-8-sig').splitlines()
            return line <= len(lines) and declared.lower() in lines[line-1].lower()
        except (UnicodeDecodeError, ValueError, OSError, RuntimeError, NotImplementedError, zipfile.BadZipFile):
            return False

    @staticmethod
    def hash_cycles(references):
        """Ciclos de SHA corrente com DFS iterativa, sem limite de recursão."""
        graph = {}
        for ref in references:
            if (ref.get('categoria') == 'HASH_FISICO_ATUAL'
                    and ref.get('estado') in ('CONFORME', 'NÃO CONFORME')):
                graph.setdefault(ref['origem'], set()).add(ref['destino'])
        visited, active_positions, path, cycles = set(), {}, [], set()
        for root in sorted(graph):
            if root in visited:
                continue
            active_positions[root] = len(path)
            path.append(root)
            frames = [(root, iter(sorted(graph.get(root, ()))))]
            while frames:
                node, neighbors = frames[-1]
                neighbor = next(neighbors, None)
                if neighbor is None:
                    frames.pop()
                    path.pop()
                    active_positions.pop(node)
                    visited.add(node)
                elif neighbor in active_positions:
                    cycle = path[active_positions[neighbor]:]
                    cycles.add(tuple(sorted(cycle)))
                elif neighbor not in visited:
                    active_positions[neighbor] = len(path)
                    path.append(neighbor)
                    frames.append((neighbor, iter(sorted(graph.get(neighbor, ())))))
        return [list(c) for c in sorted(cycles)]

    def hash_checks(self):
        results = []
        if not self.opts.hash_catalog:
            return results
        catalog_path = Path(self.opts.hash_catalog)
        if catalog_path.is_symlink() or protected(catalog_path.as_posix()) or protected(str(catalog_path.resolve())):
            raise ValueError('catálogo de hashes protegido ou link simbólico')
        if catalog_path.stat().st_size > 5 * 1024 * 1024:
            raise ValueError('catálogo SHA excede limite de 5 MiB')
        with catalog_path.open('r', encoding='utf-8') as f:
            obj = json.load(f)
        if not isinstance(obj, dict) or not isinstance(obj.get('references'), list):
            raise ValueError('catálogo exige objeto com lista references')
        for index, ref in enumerate(obj['references']):
            if not isinstance(ref, dict):
                self.issue('catalogo_hash', 'NÃO VALIDADO', 'entrada não é objeto', indice=index)
                continue
            source, destination = ref.get('source'), ref.get('destination')
            tag, declared = ref.get('category', 'HASH_SEM_CLASSIFICACAO'), ref.get('declared_sha256')
            basis = ref.get('normative_basis')
            item = {'indice': index, 'origem': source, 'destino': destination, 'categoria': tag,
                    'sha_declarado': declared, 'base_normativa': basis, 'linha': ref.get('line')}
            if (not isinstance(source, str) or not isinstance(destination, str)
                    or protected(source) or protected(destination)
                    or not isinstance(tag, str) or tag not in HASH_CLASSES
                    or not isinstance(declared, str) or not SHA256_RE.fullmatch(declared)):
                item['estado'] = 'NÃO VALIDADO'
                item['limite'] = 'entrada de referência inválida ou sem classificação reconhecida'
            elif source not in self.entries or destination not in self.entries:
                item['estado'] = 'NÃO VALIDADO'
                item['limite'] = 'origem ou destino não presentes entre arquivos elegíveis'
            elif not isinstance(basis, str) or not basis.strip():
                item['estado'] = 'NÃO VALIDADO'
                item['limite'] = 'finalidade do hash não lastreada por fonte normativa informada'
            elif not isinstance(ref.get('line'), int) or isinstance(ref.get('line'), bool) or ref['line'] < 1:
                item['estado'] = 'NÃO VALIDADO'
                item['limite'] = 'linha física da referência SHA obrigatória, não informada'
            elif not self.hash_occurs_at_source_line(source, ref['line'], declared):
                item['estado'] = 'NÃO VALIDADO'
                item['limite'] = 'SHA declarado não consta da linha física informada no arquivo de origem'
            elif tag == 'HASH_SEM_CLASSIFICACAO':
                item['estado'] = 'NÃO VALIDADO'
                item['limite'] = 'referência sem classificação semântica demonstrada'
            else:
                actual = self.entries[destination]['sha256']
                item['sha_fisico_atual'] = actual
                item['igual_ao_fisico'] = declared.lower() == actual
                if tag == 'HASH_FISICO_ATUAL':
                    item['estado'] = 'CONFORME' if item['igual_ao_fisico'] else 'NÃO CONFORME'
                    if not item['igual_ao_fisico']:
                        self.issue('hash_corrente_divergente', 'NÃO CONFORME',
                                   'referência declarada corrente diverge do SHA físico', source,
                                   destino=destination, indice=index)
                elif tag == 'HASH_AJUSTE_SUBSTITUIDO':
                    item['estado'] = 'NÃO VALIDADO'
                    item['limite'] = ('ajuste intermediário: identidade não compõe histórico de versão; '
                                      'avaliar somente referências correntes, sem apagar provas de decisão')
                else:
                    item['estado'] = 'NÃO VALIDADO'
                    item['limite'] = ('igualdade com bytes atuais não autentica decisão, versão anterior '
                                      'ou snapshot de origem; revisar fonte e evento')
            results.append(item)
        return results

    def viewport_checks(self):
        results = []
        for row in self.opts.viewport_check:
            screen, board = row[:2]
            try:
                x, y, w, h = [int(q) for q in row[2:]]
                if x < 0 or y < 0 or w < 1 or h < 1:
                    raise ValueError('coordenadas negativas ou dimensões não positivas')
            except ValueError as exc:
                self.issue('viewport_parametro', 'NÃO VALIDADO', str(exc))
                continue
            item = {'tela': screen, 'prancha': board,
                    'viewport': {'x': x, 'y': y, 'largura': w, 'altura': h},
                    'origem_geometria': 'parâmetro explícito; contrato ainda requer verificação humana'}
            if protected(screen) or protected(board) or screen not in self.entries or board not in self.entries:
                item['estado'] = 'NÃO VALIDADO'
                item['limite'] = 'imagem fora da leitura elegível ou inexistente'
                results.append(item)
                continue
            try:
                from PIL import Image
            except ImportError:
                item['estado'] = 'NÃO VALIDADO'
                item['limite'] = 'Pillow indisponível; comparação não realizada'
                results.append(item)
                continue
            try:
                with warnings.catch_warnings():
                    warnings.simplefilter('error', Image.DecompressionBombWarning)
                    with Image.open(io.BytesIO(self.content(screen))) as im1, Image.open(io.BytesIO(self.content(board))) as im2:
                        im1.load()
                        im2.load()
                        result_im1 = im1.copy()
                        result_im2 = im2.copy()
                with result_im1 as im1, result_im2 as im2:
                    item['dimensoes_tela'] = list(im1.size)
                    item['dimensoes_prancha'] = list(im2.size)
                    if im1.size != (w, h) or x + w > im2.width or y + h > im2.height:
                        item['estado'] = 'NÃO CONFORME'
                        item['limite'] = 'geometria incompatível com dimensões físicas das imagens'
                        self.issue('geometria_viewport', 'NÃO CONFORME', item['limite'], board)
                    else:
                        a = im1.convert('RGBA')
                        b = im2.crop((x, y, x+w, y+h)).convert('RGBA')
                        first, second = a.tobytes(), b.tobytes()
                        different = sum(first[i:i+4] != second[i:i+4] for i in range(0, len(first), 4))
                        item['pixels_comparados'] = w * h
                        item['pixels_diferentes'] = different
                        item['estado'] = 'CONFORME' if different == 0 else 'NÃO CONFORME'
                        if different:
                            self.issue('viewport_pixels', 'NÃO CONFORME',
                                       'ViewPort difere do PNG na geometria informada', board,
                                       pixels_diferentes=different)
                item['limite_semantico'] = 'igualdade de pixels não valida legibilidade, conteúdo ou Gate'
            except (OSError, ValueError, Image.DecompressionBombError, Image.DecompressionBombWarning) as exc:
                item['estado'] = 'NÃO VALIDADO'
                item['limite'] = 'não foi possível decodificar ou comparar: ' + type(exc).__name__
            results.append(item)
        return results

    def compare_baseline(self):
        if not self.opts.baseline:
            return None
        alt = argparse.Namespace(**vars(self.opts))
        alt.source = self.opts.baseline
        alt.baseline = None
        alt.hash_catalog = None
        alt.viewport_check = []
        alt.check_links = False
        other = Auditor(alt)
        try:
            other.detect_container()
            if other.source_type == 'zip':
                other.enumerate_zip()
            else:
                other.enumerate_directory()
            current, previous = self.entries, other.entries
            common = set(current) & set(previous)
            result = {
                'base_anterior': other.base_identity,
                'adicionados': sorted(set(current) - set(previous)),
                'excluidos': sorted(set(previous) - set(current)),
                'alterados': sorted(p for p in common if current[p]['sha256'] != previous[p]['sha256']
                                   or current[p]['tamanho_bytes'] != previous[p]['tamanho_bytes']),
                'inalterados': len([p for p in common if current[p]['sha256'] == previous[p]['sha256']
                                    and current[p]['tamanho_bytes'] == previous[p]['tamanho_bytes']]),
                'limites': ('compara bytes/hash/size, não comprova leituras semânticas históricas nem equivalência '
                            'de aprovações'),
                'falhas_de_integridade': other.issues,
            }
            if other.issues:
                self.issue('baseline_insegura', 'NÃO VALIDADO',
                           'comparação incremental possui falhas ou escopo parcialmente inacessível')
            return result
        finally:
            if other.zipobj:
                other.zipobj.close()

    def run(self):
        self.detect_container()
        try:
            if self.source_type == 'zip':
                self.enumerate_zip()
            else:
                self.enumerate_directory()
            if not self.entries:
                self.issue('escopo_sem_arquivos', 'BLOQUEADO',
                           'nenhum arquivo elegível foi lido; auditoria física não pode ser declarada conforme')
            self.index_parent_directories()
            links = self.link_checks()
            hashes = self.hash_checks()
            viewport = self.viewport_checks()
            previous = self.compare_baseline()
            cycles = self.hash_cycles(hashes)
            for cycle in cycles:
                self.issue('ciclo_hash_corrente', 'NÃO VALIDADO',
                           'dependência circular entre hashes correntes exige contrato de resolução',
                           caminhos=cycle)
            blocked = any(a['estado'] == 'BLOQUEADO' for a in self.issues)
            failed = any(a['estado'] == 'NÃO CONFORME' for a in self.issues)
            automatic = 'BLOQUEADO' if blocked else ('NÃO CONFORME' if failed else 'CONFORME')
            output = {
                'ferramenta': {'nome': 'saor-auditoria-integridade', 'versao': SCRIPT_VERSION,
                               'sha256_script': sha256_bytes(Path(__file__).read_bytes()),
                               'execucao': 'somente_leitura', 'relatorio_persistido': False},
                'solicitacao': {'modo': self.opts.mode, 'dominio': self.opts.domain,
                                'estagio_declarado': self.opts.stage, 'escopo': self.scopes,
                                'classificacao_legado_revisada_pelo_operador': self.opts.classification_reviewed,
                                'caminhos_legados_excluidos': len(self.legacy),
                                'fonte_evidencia_classificacao': self.opts.legacy_basis},
                'fonte': self.base_identity,
                'integridade': {'arquivos_lidos_por_bytes': len(self.entries),
                                'total_bytes_hash_integridade': self.total_bytes,
                                'exclusoes': self.exclusion_counts,
                                'estado_automatizado': automatic,
                                'abrangencia': 'arquivos regulares elegíveis dentro dos escopos informados'},
                'inventario': [self.entries[p] for p in sorted(self.entries)],
                'links_markdown_inline': links,
                'referencias_sha_classificadas': hashes,
                'ciclos_sha_corrente': cycles,
                'controles_automatizados': {
                    'AU-00': {'estado': automatic, 'verificacao': 'identidade do contêiner, caminhos e leitura elegível'},
                    'AU-02': {'estado': automatic, 'verificacao': 'inventário físico limitado ao escopo recebido'},
                    'AU-04': {'estado': 'NÃO VALIDADO', 'verificacao': 'validador editorial oficial não invocado pelo executor'},
                    'AU-06': {'estado': 'NÃO VALIDADO', 'verificacao': 'links inline e catálogo explicitamente informado; não cobre toda a semântica'},
                    'AU-07': {'estado': 'NÃO VALIDADO', 'verificacao': 'classificação de versão formal e cronologia depende de norma'},
                    'AU-08': {'estado': 'NÃO VALIDADO', 'verificacao': 'aprovações e escopos humanos não inferidos'},
                    'AU-12': {'estado': 'NÃO VALIDADO', 'verificacao': 'encerramento só após auditoria humana e todos os controles'},
                },
                'comparacoes_viewport': viewport,
                'comparacao_incremental': previous,
                'ocorrencias': self.issues,
                'limites': self.limits,
                'controles_externos_pendentes': [
                    'hierarquia normativa e exigibilidade do estágio',
                    'interpretação semântica e de regras de negócio',
                    'inspeção visual humana/assistida das imagens',
                    'identidade e abrangência das decisões e aprovações humanas',
                    'classificação normativa de LEGADOS e de cada hash de decisão',
                    'validadores oficiais de domínio e segunda auditoria pós-correção',
                ],
                'encerramento_normativo': 'NÃO VALIDADO',
            }
            code = 3 if blocked else (2 if failed else 0)
            return output, code
        finally:
            if self.zipobj:
                self.zipobj.close()


def arguments(argv):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--source', required=True, help='ZIP ou diretório físico autorizado')
    parser.add_argument('--scope', action='append', required=True,
                        help='caminho relativo elegível; repetir para múltiplos escopos')
    parser.add_argument('--mode', choices=('SOB_DEMANDA', 'ENCERRAMENTO'), required=True)
    parser.add_argument('--domain', required=True, help='identificador de domínio, sem inferência de contrato')
    parser.add_argument('--stage', help='estágio documental, de caráter declaratório; não prova aprovação')
    parser.add_argument('--classification-reviewed', action='store_true',
                        help='declara que a classificação normativa de LEGADOS no escopo foi examinada')
    parser.add_argument('--legacy-path', action='append', default=[],
                        help='caminho excluído por classificação normativa verificada previamente')
    parser.add_argument('--legacy-basis', help='fonte normativa usada para classificar os LEGADOS')
    parser.add_argument('--exclude-path', action='append', default=[], help='outra exclusão explicitamente autorizada')
    parser.add_argument('--baseline', help='fonte física para comparação incremental (mesmo escopo e exclusões)')
    parser.add_argument('--check-links', action='store_true', help='verifica links Markdown inline do escopo')
    parser.add_argument('--hash-catalog', help='JSON com references: source, line, destination, category, declared_sha256, normative_basis')
    parser.add_argument('--viewport-check', action='append', nargs=6, default=[],
                        metavar=('TELA', 'PRANCHA', 'X', 'Y', 'W', 'H'),
                        help='comparação opcional com geometria explicitamente fornecida pelo contrato')
    parser.add_argument('--max-file-bytes', type=int, default=512 * 1024 * 1024)
    parser.add_argument('--max-total-bytes', type=int, default=2 * 1024 * 1024 * 1024)
    return parser.parse_args(argv)


def main(argv=None):
    try:
        opts = arguments(argv)
        if opts.max_file_bytes < 1 or opts.max_total_bytes < opts.max_file_bytes:
            raise ValueError('limites de bytes inconsistentes')
        if not opts.classification_reviewed or not opts.legacy_basis:
            raise ValueError('classificação prévia obrigatória: informar --classification-reviewed e --legacy-basis')
        auditor = Auditor(opts)
        output, code = auditor.run()
        print(json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2))
        return code
    except (ValueError, OSError, RuntimeError, zipfile.BadZipFile, json.JSONDecodeError) as exc:
        print(json.dumps({'estado': 'BLOQUEADO', 'erro': type(exc).__name__,
                          'motivo': str(exc), 'encerramento_normativo': 'NÃO VALIDADO'},
                         ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
