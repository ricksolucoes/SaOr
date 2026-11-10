#!/usr/bin/env python3
"""GVA-5 — testes reproduzíveis do executor físico/referencial GVA-4.

Os cenários são sintéticos e efêmeros. Não acessam nem alteram arquivos do SaOr.
A verificação semântica e os aceites humanos NÃO são simulados como conformes.
Executar: python -B -m unittest discover -s .skill/saor-auditoria/tests -p 'test_*.py' -v
"""

from __future__ import annotations

import hashlib
import io
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest
import zipfile

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'auditar_integridade.py'
SOURCE_NORM = '.specs/PROCESSO-ALTERACAO-ASSISTIDA.md'
NORM_CONTENT = b'# Norma sintetica de teste - sem autoridade no projeto\n'


def digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def write(root: Path, relative: str, data: bytes | str):
    target = root / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data.encode('utf-8') if isinstance(data, str) else data)
    return target


def archive(target: Path, entries, *, prefix='SaOr-main/', compression=zipfile.ZIP_DEFLATED):
    """entries: lista de (caminho relativo, bytes), mantendo duplicidades intencionais."""
    with zipfile.ZipFile(target, 'w', compression=compression) as z:
        z.writestr(prefix + SOURCE_NORM, NORM_CONTENT)
        for name, body in entries:
            z.writestr(prefix + name, body)
    return target


def as_png(size=(4, 3), color=(20, 40, 60, 255)):
    from PIL import Image
    out = io.BytesIO()
    Image.new('RGBA', size, color).save(out, format='PNG')
    return out.getvalue()


def board_png(size=(9, 8), region=(2, 3, 4, 3), color=(20, 40, 60, 255), change=False):
    from PIL import Image
    im = Image.new('RGBA', size, (255, 255, 255, 255))
    x, y, w, h = region
    for xx in range(x, x+w):
        for yy in range(y, y+h):
            im.putpixel((xx, yy), color)
    if change:
        im.putpixel((x+1, y+1), (1, 2, 3, 255))
    out = io.BytesIO()
    im.save(out, format='PNG')
    return out.getvalue()


class AuditorFixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='saor-gva5-')
        self.addCleanup(self.tmp.cleanup)
        self.temp = Path(self.tmp.name)
        self.source = self.temp / 'clone'
        self.source.mkdir()
        write(self.source, SOURCE_NORM, NORM_CONTENT)
        self.executor_before = digest(SCRIPT.read_bytes())

    def file(self, name, body):
        return write(self.source, name, body)

    def zip(self, entries, **kwargs):
        return archive(self.temp / 'clone.zip', entries, **kwargs)

    def catalog(self, refs):
        target = self.temp / 'referencias.json'
        target.write_text(json.dumps({'references': refs}, ensure_ascii=False), encoding='utf-8')
        return target

    def invoke(self, source=None, *, mode='SOB_DEMANDA', domain='generico', stage='inicial',
               scope=None, extra=(), classified=True):
        args = [sys.executable, '-B', str(SCRIPT), '--source', str(source or self.source)]
        for selected in (scope if scope is not None else ['.specs', 'docs']):
            args.extend(['--scope', selected])
        args.extend(['--mode', mode, '--domain', domain, '--stage', stage])
        if classified:
            args.extend(['--classification-reviewed', '--legacy-basis', SOURCE_NORM])
        args.extend(str(s) for s in extra)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONHASHSEED='0')
        run = subprocess.run(args, text=True, capture_output=True, cwd=self.temp, env=env,
                             timeout=40, check=False)
        output = run.stdout if run.returncode in (0, 2, 3) else run.stderr
        try:
            result = json.loads(output)
        except json.JSONDecodeError as exc:
            self.fail(f'retorno nao JSON: code={run.returncode}, stdout={run.stdout[:800]}, '
                      f'stderr={run.stderr[:800]}: {exc}')
        self.assertEqual(digest(SCRIPT.read_bytes()), self.executor_before,
                         'GVA-4 modificado durante teste')
        return run.returncode, result

    @staticmethod
    def entry(result, name):
        return next(e for e in result['inventario'] if e['caminho'] == name)

    @staticmethod
    def kinds(result):
        return {i['tipo'] for i in result.get('ocorrencias', [])}

    def ref(self, body_sha, *, source='docs/fonte.md', destination='docs/alvo.txt',
            line=1, category='HASH_FISICO_ATUAL', basis=SOURCE_NORM):
        return {'source': source, 'line': line, 'destination': destination,
                'category': category, 'declared_sha256': body_sha,
                'normative_basis': basis}


class TestFonteEIntegridade(AuditorFixture):
    def test_01_diretorio_integro_com_sha_fisico(self):
        data = b'abc\x00final'
        self.file('docs/a.bin', data)
        code, out = self.invoke()
        self.assertEqual(code, 0)
        self.assertEqual(out['integridade']['arquivos_lidos_por_bytes'], 2)
        self.assertEqual(self.entry(out, 'docs/a.bin')['sha256'], digest(data))
        self.assertEqual(out['encerramento_normativo'], 'NÃO VALIDADO')

    def test_02_zip_com_raiz_repositorio_e_crc(self):
        code, out = self.invoke(self.zip([('docs/a.txt', b'abc')]), scope=['.specs', 'docs'])
        self.assertEqual(code, 0)
        self.assertTrue(self.entry(out, 'docs/a.txt')['crc_zip_verificado'])
        self.assertEqual(out['fonte']['tipo'], 'zip')
        self.assertEqual(out['integridade']['arquivos_lidos_por_bytes'], 2)

    def test_03_zip_crc_corrompido_detectado(self):
        zpath = self.zip([('docs/um.txt', b'SAOR_MARKER_TO_CORRUPT')], compression=zipfile.ZIP_STORED)
        raw = zpath.read_bytes()
        self.assertIn(b'SAOR_MARKER_TO_CORRUPT', raw)
        zpath.write_bytes(raw.replace(b'SAOR_MARKER_TO_CORRUPT', b'RAOR_MARKER_TO_CORRUPT', 1))
        code, out = self.invoke(zpath)
        self.assertEqual(code, 3)
        self.assertIn('integridade_zip', self.kinds(out))
        self.assertNotIn('docs/um.txt', {x['caminho'] for x in out['inventario']})

    def test_04_zip_travessia_rejeitada(self):
        code, out = self.invoke(self.zip([('../escape.md', b'invalido')]))
        self.assertEqual(code, 3)
        self.assertIn('caminho_inseguro', self.kinds(out))

    def test_05_zip_caminho_absoluto_rejeitado(self):
        code, out = self.invoke(self.zip([('/abs.txt', b'invalido')]))
        self.assertEqual(code, 3)
        self.assertIn('caminho_inseguro', self.kinds(out))

    def test_06_zip_duplicidade_rejeitada(self):
        with zipfile.ZipFile(self.temp / 'duplo.zip', 'w') as z:
            z.writestr('SaOr-main/' + SOURCE_NORM, NORM_CONTENT)
            with __import__('warnings').catch_warnings():
                __import__('warnings').simplefilter('ignore', UserWarning)
                z.writestr('SaOr-main/docs/a.txt', b'primeiro')
                z.writestr('SaOr-main/docs/a.txt', b'segundo')
        code, out = self.invoke(self.temp / 'duplo.zip')
        self.assertEqual(code, 3)
        self.assertIn('duplicidade', self.kinds(out))

    def test_07_zip_colisao_unicode_caixa(self):
        code, out = self.invoke(self.zip([('docs/ARQ.md', b'um'), ('docs/arq.md', b'dois')]))
        self.assertEqual(code, 3)
        self.assertIn('colisao_case_unicode', self.kinds(out))

    def test_08_zip_simbolico_rejeitado(self):
        target = self.temp / 'simbolico.zip'
        with zipfile.ZipFile(target, 'w') as z:
            z.writestr('SaOr-main/' + SOURCE_NORM, NORM_CONTENT)
            info = zipfile.ZipInfo('SaOr-main/docs/link')
            info.create_system = 3
            info.external_attr = (stat.S_IFLNK | 0o777) << 16
            z.writestr(info, '../externo')
        code, out = self.invoke(target)
        self.assertEqual(code, 3)
        self.assertIn('entrada_especial', self.kinds(out))

    def test_09_diretorio_link_simbolico_nao_segue(self):
        outside = self.temp / 'externo'
        write(outside, 'secreto.txt', 'SEGREDO_NAO_LER')
        (self.source / 'docs').mkdir()
        (self.source / 'docs' / 'link').symlink_to(outside, target_is_directory=True)
        code, out = self.invoke()
        self.assertEqual(code, 3)
        self.assertIn('symlink', self.kinds(out))
        self.assertNotIn('secreto.txt', json.dumps(out, ensure_ascii=False))

    def test_10_arquivo_link_simbolico_nao_segue(self):
        outside = write(self.temp, 'privado.txt', 'PRIVADO')
        (self.source / 'docs').mkdir()
        (self.source / 'docs' / 'link.txt').symlink_to(outside)
        code, out = self.invoke()
        self.assertEqual(code, 3)
        self.assertIn('symlink', self.kinds(out))
        self.assertNotIn('PRIVADO', json.dumps(out, ensure_ascii=False))

    def test_11_assets_nao_inspecionados(self):
        secret = b'DADO_SIGILOSO_TESTE'
        code, out = self.invoke(self.zip([('assets/canary', secret), ('docs/publico.txt', b'publico')]))
        self.assertEqual(code, 0)
        self.assertNotIn(digest(secret), json.dumps(out, ensure_ascii=False))
        self.assertNotIn('assets/canary', json.dumps(out, ensure_ascii=False))
        self.assertGreaterEqual(out['integridade']['exclusoes']['assets'], 1)

    def test_12_escopo_assets_explicitamente_rejeitado(self):
        code, out = self.invoke(scope=['assets'])
        self.assertEqual(code, 1)
        self.assertEqual(out['estado'], 'BLOQUEADO')

    def test_13_arquivo_legado_excluido_por_declaracao(self):
        self.file('docs/legado.md', 'SEGREDO_LEGADO')
        self.file('docs/atual.md', 'atual')
        code, out = self.invoke(extra=['--legacy-path', 'docs/legado.md'])
        self.assertEqual(code, 0)
        self.assertNotIn('docs/legado.md', {e['caminho'] for e in out['inventario']})
        self.assertEqual(out['solicitacao']['caminhos_legados_excluidos'], 1)
        self.assertIn('Classificação de LEGADO depende', ' '.join(out['limites']))

    def test_14_sem_revisao_de_legados_rejeita_entrada(self):
        code, out = self.invoke(classified=False)
        self.assertEqual(code, 1)
        self.assertEqual(out['estado'], 'BLOQUEADO')

    def test_15_escopo_vazio_nao_e_conforme(self):
        code, out = self.invoke(scope=['nao-existe'])
        self.assertEqual(code, 3)
        self.assertIn('escopo_sem_arquivos', self.kinds(out))

    def test_16_limite_de_expansao_rejeitado(self):
        self.file('docs/grande.bin', b'x'*800)
        code, out = self.invoke(extra=['--max-file-bytes', '500', '--max-total-bytes', '5000'])
        self.assertEqual(code, 3)
        self.assertIn('limite_expansao', self.kinds(out))

    def test_17_limite_incoerente_rejeitado(self):
        code, out = self.invoke(extra=['--max-file-bytes', '1000', '--max-total-bytes', '100'])
        self.assertEqual(code, 1)
        self.assertEqual(out['estado'], 'BLOQUEADO')

    def test_18_arquivo_nao_zip_rejeitado(self):
        fake = write(self.temp, 'nao.zip', b'nao existe zip')
        code, out = self.invoke(fake)
        self.assertEqual(code, 1)
        self.assertEqual(out['estado'], 'BLOQUEADO')


class TestReferencias(AuditorFixture):
    def test_19_link_relativo_valido(self):
        self.file('docs/a.md', '[alvo](b.md)\n')
        self.file('docs/b.md', 'alvo')
        code, out = self.invoke(extra=['--check-links'])
        self.assertEqual(code, 0)
        link = next(x for x in out['links_markdown_inline'] if x['origem'] == 'docs/a.md')
        self.assertEqual((link['estado'], link['destino']), ('CONFORME', 'docs/b.md'))

    def test_20_link_para_diretorio_valido(self):
        self.file('docs/a.md', '[pasta](sub)\n')
        self.file('docs/sub/b.md', 'alvo')
        code, out = self.invoke(extra=['--check-links'])
        self.assertEqual(code, 0)
        self.assertEqual(out['links_markdown_inline'][0]['tipo_destino'], 'diretorio')

    def test_21_link_quebrado_detectado(self):
        self.file('docs/a.md', '[alvo](inexistente.md)')
        code, out = self.invoke(extra=['--check-links'])
        self.assertEqual(code, 2)
        self.assertIn('referencia_quebrada', self.kinds(out))

    def test_22_link_que_sai_da_raiz_bloqueado(self):
        self.file('docs/a.md', '[fora](../../fora.md)')
        code, out = self.invoke(extra=['--check-links'])
        self.assertEqual(code, 3)
        self.assertIn('link_inseguro', self.kinds(out))

    def test_23_link_externo_nao_e_link_quebrado(self):
        self.file('docs/a.md', '[externo](https://example.org/recurso)')
        code, out = self.invoke(extra=['--check-links'])
        self.assertEqual(code, 0)
        self.assertEqual(out['links_markdown_inline'][0]['estado'], 'NÃO APLICÁVEL')

    def test_24_link_em_bloco_codigo_nao_e_avaliado(self):
        self.file('docs/a.md', '```md\n[exemplo](faltando.md)\n```\n')
        code, out = self.invoke(extra=['--check-links'])
        self.assertEqual(code, 0)
        self.assertEqual(out['links_markdown_inline'], [])

    def test_25_link_para_assets_nao_acessado(self):
        self.file('docs/a.md', '[protegido](../assets/segredo.md)')
        code, out = self.invoke(extra=['--check-links'])
        self.assertEqual(code, 0)
        self.assertEqual(out['links_markdown_inline'][0]['estado'], 'NÃO VALIDADO')
        self.assertNotIn('referencia_quebrada', self.kinds(out))

    def test_26_links_fora_escopo_nao_falsamente_quebrados(self):
        self.file('docs/a.md', '[contrato](../normas/contrato.md)')
        code, out = self.invoke(extra=['--check-links'])
        self.assertEqual(code, 0)
        self.assertEqual(out['links_markdown_inline'][0]['estado'], 'NÃO VALIDADO')

    def test_27_limite_do_parser_de_links_esta_declarado(self):
        self.file('docs/a.md', '[referencia][id]\n[id]: faltando.md\n')
        code, out = self.invoke(extra=['--check-links'])
        self.assertEqual(code, 0)
        self.assertEqual(out['links_markdown_inline'], [])
        self.assertTrue(any('links de referência' in s for s in out['limites']))


class TestHashesEVersoes(AuditorFixture):
    def pair(self, declared=None):
        target = b'bytes efetivos v01'
        actual = digest(target)
        declared = declared or actual
        self.file('docs/fonte.md', f'arquivo: {declared}\n')
        self.file('docs/alvo.txt', target)
        return actual, declared

    def test_28_sha_corrente_confere(self):
        actual, declared = self.pair()
        code, out = self.invoke(extra=['--hash-catalog', self.catalog([self.ref(declared)])])
        self.assertEqual(code, 0)
        ref = out['referencias_sha_classificadas'][0]
        self.assertEqual(ref['estado'], 'CONFORME')
        self.assertEqual(ref['sha_fisico_atual'], actual)

    def test_29_sha_corrente_divergente(self):
        _, declared = self.pair('a'*64)
        code, out = self.invoke(extra=['--hash-catalog', self.catalog([self.ref(declared)])])
        self.assertEqual(code, 2)
        self.assertEqual(out['referencias_sha_classificadas'][0]['estado'], 'NÃO CONFORME')
        self.assertIn('hash_corrente_divergente', self.kinds(out))

    def test_30_hash_aprovacao_apos_edicao_nao_e_erro_automatico(self):
        _, declared = self.pair('b'*64)
        code, out = self.invoke(extra=['--hash-catalog', self.catalog([
            self.ref(declared, category='HASH_SUBMISSAO_OU_APROVACAO')])])
        self.assertEqual(code, 0)
        self.assertEqual(out['referencias_sha_classificadas'][0]['estado'], 'NÃO VALIDADO')
        self.assertEqual(out['encerramento_normativo'], 'NÃO VALIDADO')
        self.assertNotIn('hash_corrente_divergente', self.kinds(out))

    def test_31_ajuste_mesma_versao_nao_gera_historico(self):
        _, declared = self.pair('c'*64)
        code, out = self.invoke(extra=['--hash-catalog', self.catalog([
            self.ref(declared, category='HASH_AJUSTE_SUBSTITUIDO')])])
        self.assertEqual(code, 0)
        item = out['referencias_sha_classificadas'][0]
        self.assertEqual(item['categoria'], 'HASH_AJUSTE_SUBSTITUIDO')
        self.assertEqual(item['estado'], 'NÃO VALIDADO')
        self.assertNotIn('versoes_criadas', out)
        self.assertNotIn('hash_corrente_divergente', self.kinds(out))

    def test_32_versao_formal_anterior_nao_comparada_com_atual(self):
        _, declared = self.pair('d'*64)
        code, out = self.invoke(extra=['--hash-catalog', self.catalog([
            self.ref(declared, category='HASH_VERSAO_FORMAL_ANTERIOR')])])
        self.assertEqual(code, 0)
        self.assertEqual(out['referencias_sha_classificadas'][0]['estado'], 'NÃO VALIDADO')

    def test_33_hash_origem_documentada_exige_confirmacao(self):
        _, declared = self.pair('e'*64)
        code, out = self.invoke(extra=['--hash-catalog', self.catalog([
            self.ref(declared, category='HASH_DE_ORIGEM_DOCUMENTADA')])])
        self.assertEqual(code, 0)
        self.assertEqual(out['referencias_sha_classificadas'][0]['estado'], 'NÃO VALIDADO')

    def test_34_hash_sem_classificacao_nao_e_aceito(self):
        _, declared = self.pair('f'*64)
        code, out = self.invoke(extra=['--hash-catalog', self.catalog([
            self.ref(declared, category='HASH_SEM_CLASSIFICACAO')])])
        self.assertEqual(code, 0)
        self.assertEqual(out['referencias_sha_classificadas'][0]['estado'], 'NÃO VALIDADO')

    def test_35_fonte_sha_linha_nao_correspondente(self):
        _, declared = self.pair()
        code, out = self.invoke(extra=['--hash-catalog', self.catalog([
            self.ref(declared, line=2)])])
        self.assertEqual(code, 0)
        self.assertEqual(out['referencias_sha_classificadas'][0]['estado'], 'NÃO VALIDADO')

    def test_36_fonte_normativa_ausente_nao_e_conforme(self):
        _, declared = self.pair()
        code, out = self.invoke(extra=['--hash-catalog', self.catalog([
            self.ref(declared, basis='')])])
        self.assertEqual(code, 0)
        self.assertEqual(out['referencias_sha_classificadas'][0]['estado'], 'NÃO VALIDADO')

    def test_37_entrada_catalogo_invalida_nao_e_corrigida(self):
        self.pair()
        code, out = self.invoke(extra=['--hash-catalog', self.catalog([{'source': 'docs/fonte.md'}])])
        self.assertEqual(code, 0)
        self.assertEqual(out['referencias_sha_classificadas'][0]['estado'], 'NÃO VALIDADO')

    def test_38_autorreferencia_sha_sinalizada(self):
        fake = '0'*64
        self.file('docs/fonte.md', 'HASH=' + fake)
        ref = self.ref(fake, source='docs/fonte.md', destination='docs/fonte.md')
        code, out = self.invoke(extra=['--hash-catalog', self.catalog([ref])])
        self.assertEqual(code, 2)  # divergencia do SHA fisico calculado
        self.assertTrue(out['ciclos_sha_corrente'])
        self.assertIn('ciclo_hash_corrente', self.kinds(out))

    def test_39_ciclo_sha_corrente_entre_arquivos(self):
        sha_a, sha_b = 'a'*64, 'b'*64
        self.file('docs/a.md', 'SHA B: ' + sha_b)
        self.file('docs/b.md', 'SHA A: ' + sha_a)
        refs = [self.ref(sha_b, source='docs/a.md', destination='docs/b.md'),
                self.ref(sha_a, source='docs/b.md', destination='docs/a.md')]
        code, out = self.invoke(extra=['--hash-catalog', self.catalog(refs)])
        self.assertEqual(code, 2)
        self.assertTrue(out['ciclos_sha_corrente'])
        self.assertIn('ciclo_hash_corrente', self.kinds(out))


class TestComparacoesEEstado(AuditorFixture):
    def test_40_viewport_identico_pixel_a_pixel(self):
        self.file('docs/tela.png', as_png())
        self.file('docs/prancha.png', board_png())
        code, out = self.invoke(extra=['--viewport-check', 'docs/tela.png', 'docs/prancha.png',
                                       '2', '3', '4', '3'])
        self.assertEqual(code, 0)
        check = out['comparacoes_viewport'][0]
        self.assertEqual((check['estado'], check['pixels_comparados'], check['pixels_diferentes']),
                         ('CONFORME', 12, 0))

    def test_41_viewport_um_pixel_divergente(self):
        self.file('docs/tela.png', as_png())
        self.file('docs/prancha.png', board_png(change=True))
        code, out = self.invoke(extra=['--viewport-check', 'docs/tela.png', 'docs/prancha.png',
                                       '2', '3', '4', '3'])
        self.assertEqual(code, 2)
        self.assertEqual(out['comparacoes_viewport'][0]['pixels_diferentes'], 1)
        self.assertIn('viewport_pixels', self.kinds(out))

    def test_42_viewport_geometria_incorreta(self):
        self.file('docs/tela.png', as_png())
        self.file('docs/prancha.png', board_png())
        code, out = self.invoke(extra=['--viewport-check', 'docs/tela.png', 'docs/prancha.png',
                                       '7', '7', '4', '3'])
        self.assertEqual(code, 2)
        self.assertIn('geometria_viewport', self.kinds(out))

    def test_43_viewport_arquivo_nao_imagem_nao_e_conforme(self):
        self.file('docs/tela.png', b'nao e PNG')
        self.file('docs/prancha.png', board_png())
        code, out = self.invoke(extra=['--viewport-check', 'docs/tela.png', 'docs/prancha.png',
                                       '2', '3', '4', '3'])
        self.assertEqual(code, 0)
        self.assertEqual(out['comparacoes_viewport'][0]['estado'], 'NÃO VALIDADO')

    def test_44_incremental_inclusao_exclusao_alteracao(self):
        self.file('docs/a.txt', b'atual')
        self.file('docs/c.txt', b'novo')
        before = self.temp / 'anterior'
        write(before, SOURCE_NORM, NORM_CONTENT)
        write(before, 'docs/a.txt', b'antigo')
        write(before, 'docs/b.txt', b'removido')
        code, out = self.invoke(extra=['--baseline', before])
        self.assertEqual(code, 0)
        comp = out['comparacao_incremental']
        self.assertEqual(comp['adicionados'], ['docs/c.txt'])
        self.assertEqual(comp['excluidos'], ['docs/b.txt'])
        self.assertEqual(comp['alterados'], ['docs/a.txt'])
        self.assertEqual(comp['inalterados'], 1)

    def test_45_incremental_fonte_identica_sem_regressao(self):
        self.file('docs/a.txt', b'igual')
        before = self.temp / 'anterior'
        write(before, SOURCE_NORM, NORM_CONTENT)
        write(before, 'docs/a.txt', b'igual')
        code, out = self.invoke(extra=['--baseline', before])
        self.assertEqual(code, 0)
        comp = out['comparacao_incremental']
        self.assertEqual(comp['alterados'], [])
        self.assertEqual(comp['adicionados'], [])
        self.assertEqual(comp['excluidos'], [])
        self.assertEqual(comp['inalterados'], 2)

    def test_46_baseline_insegura_sinaliza_limite(self):
        before = self.temp / 'anterior'
        write(before, SOURCE_NORM, NORM_CONTENT)
        write(before, 'docs/dado.txt', 'texto')
        (before/'docs/link').symlink_to(self.temp/'externo')
        code, out = self.invoke(extra=['--baseline', before])
        self.assertEqual(code, 0)
        self.assertIn('baseline_insegura', self.kinds(out))
        self.assertEqual(out['comparacao_incremental']['falhas_de_integridade'][0]['estado'], 'BLOQUEADO')

    def test_47_dominios_e_modos_nao_inferem_gates(self):
        self.file('docs/a.txt', 'conteudo')
        for mode, domain in [('SOB_DEMANDA', 'dominio_x'), ('ENCERRAMENTO', 'dominio_y')]:
            with self.subTest(mode=mode, domain=domain):
                code, out = self.invoke(mode=mode, domain=domain)
                self.assertEqual(code, 0)
                self.assertEqual(out['solicitacao']['modo'], mode)
                self.assertEqual(out['solicitacao']['dominio'], domain)
                self.assertEqual(out['encerramento_normativo'], 'NÃO VALIDADO')
                self.assertEqual(out['controles_automatizados']['AU-08']['estado'], 'NÃO VALIDADO')

    def test_48_nao_cria_corrige_ou_persiste_arquivos(self):
        self.file('docs/a.md', '[nao](existe.md)')
        initial = {p.relative_to(self.source).as_posix(): digest(p.read_bytes())
                   for p in self.source.rglob('*') if p.is_file()}
        code, out = self.invoke(extra=['--check-links'])
        self.assertEqual(code, 2)
        final = {p.relative_to(self.source).as_posix(): digest(p.read_bytes())
                 for p in self.source.rglob('*') if p.is_file()}
        self.assertEqual(initial, final)
        self.assertFalse(out['ferramenta']['relatorio_persistido'])
        self.assertEqual(out['ferramenta']['execucao'], 'somente_leitura')
        self.assertFalse(list(self.source.rglob('__pycache__')))

    def test_49_saida_repetida_deterministica(self):
        self.file('docs/a.txt', b'constante')
        c1, a = self.invoke()
        c2, b = self.invoke()
        self.assertEqual(c1, 0)
        self.assertEqual(c1, c2)
        self.assertEqual(a, b)

    def test_50_controles_nao_automatizados_nao_viram_conformes(self):
        self.file('docs/a.md', '# valido estruturalmente nao implica correto')
        code, out = self.invoke(mode='ENCERRAMENTO')
        self.assertEqual(code, 0)
        for control in ('AU-04', 'AU-06', 'AU-07', 'AU-08', 'AU-12'):
            self.assertEqual(out['controles_automatizados'][control]['estado'], 'NÃO VALIDADO')
        self.assertEqual(out['encerramento_normativo'], 'NÃO VALIDADO')


class TestRegressoesGVA6(AuditorFixture):
    """Reproduz GVA6-OC-01 e OC-02 por entradas e oráculos independentes."""

    def long_hash_graph(self, count, *, circular):
        declared = 'a' * 64
        refs = []
        for i in range(count):
            source = f'docs/no_{i:04d}.md'
            self.file(source, f'SHA: {declared}\n')
            if circular or i < count - 1:
                destination = f'docs/no_{(i + 1) % count:04d}.md'
                refs.append(self.ref(declared, source=source, destination=destination))
        return refs

    def test_51_cadeia_aciclica_profunda_sem_recursionerror(self):
        refs = self.long_hash_graph(1350, circular=False)
        code, out = self.invoke(extra=['--hash-catalog', self.catalog(refs)])
        self.assertEqual(code, 2)  # hashes sintéticos atuais não correspondem aos bytes
        self.assertEqual(len(out['referencias_sha_classificadas']), 1349)
        self.assertEqual(out['ciclos_sha_corrente'], [])
        self.assertNotIn('ciclo_hash_corrente', self.kinds(out))

    def test_52_ciclo_profundo_sem_recursionerror(self):
        refs = self.long_hash_graph(1350, circular=True)
        code, out = self.invoke(extra=['--hash-catalog', self.catalog(refs)])
        self.assertEqual(code, 2)
        self.assertEqual(len(out['ciclos_sha_corrente']), 1)
        self.assertEqual(len(out['ciclos_sha_corrente'][0]), 1350)
        self.assertIn('docs/no_0000.md', out['ciclos_sha_corrente'][0])
        self.assertIn('ciclo_hash_corrente', self.kinds(out))

    def test_53_ciclos_independentes_com_ramificacao(self):
        sha = 'b' * 64
        self.file('docs/a.md', f'{sha}\n{sha}\n')
        for name in ['b', 'c', 'd']:
            self.file(f'docs/{name}.md', sha + '\n')
        pairs = [('a', 'b', 1), ('a', 'c', 2), ('b', 'a', 1),
                 ('c', 'd', 1), ('d', 'c', 1)]
        refs = [self.ref(sha, source=f'docs/{a}.md', destination=f'docs/{b}.md', line=line)
                for a, b, line in pairs]
        code, out = self.invoke(extra=['--hash-catalog', self.catalog(refs)])
        self.assertEqual(code, 2)
        self.assertEqual(out['ciclos_sha_corrente'],
                         [['docs/a.md', 'docs/b.md'], ['docs/c.md', 'docs/d.md']])

    def test_54_arquivo_ancestral_implicito_zip(self):
        code, out = self.invoke(self.zip([('docs/x', b'arquivo'),
                                          ('docs/x/y.md', b'filho')]))
        self.assertEqual(code, 3)
        self.assertIn('colisao_arquivo_diretorio', self.kinds(out))
        self.assertEqual(out['integridade']['estado_automatizado'], 'BLOQUEADO')

    def test_55_arquivo_ancestral_implicito_ordem_invertida(self):
        code, out = self.invoke(self.zip([('docs/x/y.md', b'filho'),
                                          ('docs/x', b'arquivo')]))
        self.assertEqual(code, 3)
        self.assertIn('colisao_arquivo_diretorio', self.kinds(out))

    def test_56_arquivo_e_diretorio_explicito_mesmo_caminho(self):
        code, out = self.invoke(self.zip([('docs/x/', b''), ('docs/x', b'arquivo')]))
        self.assertEqual(code, 3)
        self.assertIn('colisao_arquivo_diretorio', self.kinds(out))

    def test_57_arquivo_ancestral_por_casefold(self):
        code, out = self.invoke(self.zip([('docs/Pasta', b'arquivo'),
                                          ('docs/pasta/filho.md', b'filho')]))
        self.assertEqual(code, 3)
        self.assertIn('colisao_arquivo_diretorio', self.kinds(out))

    def test_58_zip_valido_diretorio_implicito_e_explicito(self):
        code, out = self.invoke(self.zip([('docs/pasta/', b''),
                                          ('docs/pasta/a.md', b'A'),
                                          ('docs/pasta/b.md', b'B')]))
        self.assertEqual(code, 0)
        self.assertNotIn('colisao_arquivo_diretorio', self.kinds(out))
        self.assertIn('docs/pasta/a.md', {e['caminho'] for e in out['inventario']})

    def test_59_arquivo_ancestral_por_normalizacao_unicode(self):
        code, out = self.invoke(self.zip([('docs/Café', b'arquivo'),
                                          ('docs/Cafe\u0301/filho.md', b'filho')]))
        self.assertEqual(code, 3)
        self.assertIn('colisao_arquivo_diretorio', self.kinds(out))

    def test_60_arquivo_e_diretorio_explicito_casefold(self):
        code, out = self.invoke(self.zip([('docs/Pasta/', b''),
                                          ('docs/pasta', b'arquivo')]))
        self.assertEqual(code, 3)
        self.assertIn('colisao_arquivo_diretorio', self.kinds(out))


class TestRegressoesGVA7(AuditorFixture):
    """GVA7-OC-01/02/03: entradas adversas e equivalentes ZIP válidos."""

    def invalid_catalog_category(self, category):
        body = b'conteudo independente para hash'
        sha = digest(body)
        self.file('docs/fonte.md', f'referencia {sha}\n')
        self.file('docs/alvo.txt', body)
        return self.catalog([self.ref(sha, category=category)])

    def typed_zip(self, member, filetype, *, root=False):
        target = self.temp / 'tipagem.zip'
        with zipfile.ZipFile(target, 'w') as z:
            if root:
                root_info = zipfile.ZipInfo('SaOr-main/')
                root_info.create_system = 3
                root_info.external_attr = (filetype | 0o755) << 16
                z.writestr(root_info, b'')
            z.writestr('SaOr-main/' + SOURCE_NORM, NORM_CONTENT)
            if not root:
                member_info = zipfile.ZipInfo('SaOr-main/' + member)
                member_info.create_system = 3
                member_info.external_attr = (filetype | 0o755) << 16
                z.writestr(member_info, b'' if member.endswith('/') else b'conteudo')
        return target

    def test_61_categoria_sha_lista_e_nao_validada_sem_excecao(self):
        code, out = self.invoke(extra=['--hash-catalog', self.invalid_catalog_category([])])
        self.assertEqual(code, 0)
        self.assertEqual(out['referencias_sha_classificadas'][0]['estado'], 'NÃO VALIDADO')
        self.assertEqual(out['encerramento_normativo'], 'NÃO VALIDADO')

    def test_62_categoria_sha_objeto_e_nao_validada_sem_excecao(self):
        code, out = self.invoke(extra=['--hash-catalog', self.invalid_catalog_category({})])
        self.assertEqual(code, 0)
        self.assertEqual(out['referencias_sha_classificadas'][0]['estado'], 'NÃO VALIDADO')
        self.assertEqual(out['encerramento_normativo'], 'NÃO VALIDADO')

    def test_63_categoria_sha_lista_aninhada_e_nao_validada(self):
        code, out = self.invoke(extra=['--hash-catalog', self.invalid_catalog_category([{'x': []}])])
        self.assertEqual(code, 0)
        self.assertEqual(out['referencias_sha_classificadas'][0]['estado'], 'NÃO VALIDADO')
        self.assertNotIn('hash_corrente_divergente', self.kinds(out))

    def test_64_tipo_unix_diretorio_sem_barra_rejeitado(self):
        code, out = self.invoke(self.typed_zip('docs/weird', stat.S_IFDIR))
        self.assertEqual(code, 3)
        self.assertIn('tipo_zip_incompativel', self.kinds(out))
        self.assertNotIn('docs/weird', {i['caminho'] for i in out['inventario']})

    def test_65_tipo_unix_arquivo_com_barra_rejeitado(self):
        code, out = self.invoke(self.typed_zip('docs/weird/', stat.S_IFREG))
        self.assertEqual(code, 3)
        self.assertIn('tipo_zip_incompativel', self.kinds(out))
        self.assertNotIn('docs/weird', {i['caminho'] for i in out['inventario']})

    def test_66_tipo_unix_diretorio_compativel_aceito(self):
        target = self.typed_zip('docs/weird/', stat.S_IFDIR)
        code, out = self.invoke(target)
        self.assertEqual(code, 0)
        self.assertNotIn('tipo_zip_incompativel', self.kinds(out))

    def test_67_tipo_unix_arquivo_compativel_aceito(self):
        code, out = self.invoke(self.typed_zip('docs/weird', stat.S_IFREG))
        self.assertEqual(code, 0)
        self.assertIn('docs/weird', {i['caminho'] for i in out['inventario']})

    def test_68_tipo_unix_nao_declarado_nao_e_falso_erro(self):
        code, out = self.invoke(self.typed_zip('docs/weird', 0))
        self.assertEqual(code, 0)
        self.assertNotIn('tipo_zip_incompativel', self.kinds(out))

    def test_69_duas_barras_finais_em_zip_rejeitadas(self):
        code, out = self.invoke(self.zip([('docs/dir//', b'')]))
        self.assertEqual(code, 3)
        self.assertIn('caminho_inseguro', self.kinds(out))

    def test_70_tres_barras_finais_em_zip_rejeitadas(self):
        code, out = self.invoke(self.zip([('docs/dir///', b'')]))
        self.assertEqual(code, 3)
        self.assertIn('caminho_inseguro', self.kinds(out))

    def test_71_uma_barra_final_de_diretorio_e_valida(self):
        code, out = self.invoke(self.zip([('docs/dir/', b''),
                                          ('docs/dir/conteudo.txt', b'OK')]))
        self.assertEqual(code, 0)
        self.assertIn('docs/dir/conteudo.txt', {e['caminho'] for e in out['inventario']})

    def test_72_separador_repetido_no_meio_tambem_rejeitado(self):
        code, out = self.invoke(self.zip([('docs//dir/', b'')]))
        self.assertEqual(code, 3)
        self.assertIn('caminho_inseguro', self.kinds(out))

    def test_73_diretorio_raiz_com_tipo_unix_arquivo_rejeitado(self):
        code, out = self.invoke(self.typed_zip('', stat.S_IFREG, root=True))
        self.assertEqual(code, 3)
        self.assertIn('tipo_zip_incompativel', self.kinds(out))



if __name__ == '__main__':
    unittest.main(verbosity=2)
