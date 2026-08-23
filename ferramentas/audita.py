"""Audita as notas contra o _projeto/PADRAO.md.

    python ferramentas/audita.py              todas
    python ferramentas/audita.py 01 02 03     so essas

Mede o que da para medir por regra objetiva:

  No sistema      zona 5, obrigatoria quando a nota cita codigo
  Se sobrar       zona 7, obrigatoria sempre
  cobertura       todo codigo de transacao ou tabela vira pista Transacao,
                  exceto identificador de exemplo, valor de campo, no de
                  customizing, contraexemplo citado para ser evitado e
                  codigo dentro de bloco de inferencia
  pistas ruins    fora das cinco formas: Por que, ou 'e' juntando dois pedidos
  negrito         marcas por linha. O padrao condena 1 a cada 4
"""
import io, os, re, glob, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTAS = os.path.join(BASE, 'notas')

# Codigos que a regra de cobertura nao alcanca, ver _projeto/PADRAO.md
IGNORA = re.compile(r'^(S_KK4|CJ\d|SP[BM]T|UL_|TT\d|CT\d|T\d|E\d$|BR2$|ES53$)')
CODIGO = re.compile(r'`([A-Z][A-Z0-9_*]{2,14})`')
PARECE_CODIGO = re.compile(r'^[A-Z]{2,5}[0-9*]|^SCAL$|^ELMU$|^EQUI$|^ADRC$')


def codigos_de(texto):
    """Codigos citados fora de bloco marcado como inferencia."""
    limpo = re.sub(r'^> \*\*Inferência.*?(?=\n\n)', '', texto, flags=re.M | re.S)
    achados = set()
    for c in CODIGO.findall(limpo):
        if IGNORA.match(c) or not PARECE_CODIGO.match(c):
            continue
        achados.add(c)
    return achados


def audita(caminho, gabarito):
    s = io.open(caminho, encoding='utf-8').read()
    nome = os.path.basename(caminho)
    linhas = s.count('\n') or 1
    secoes = re.findall(r'^## (.*)$', s, re.M)
    cod = codigos_de(s)

    m = re.search(r'^## Recall\s*$(.*?)(?=^>|\Z)', s, re.M | re.S)
    perguntas = re.findall(r'^\d+\.\s+(.*)$', m.group(1), re.M) if m else []

    sec_gab = re.search(r'## %s\n(.*?)(?=\n---|\Z)' % nome[3:8], gabarito, re.S)
    texto_gab = sec_gab.group(1) if sec_gab else ''
    cobertos = {c for c in cod
                if any(c in p for p in perguntas) or c in texto_gab}

    # Duas classes que a versao anterior deixava passar, e que produziram
    # quatro pistas binarias e tres duplas no bloco FI-CA antes de serem vistas:
    #   "por que" com acento circunflexo no fim da frase
    #   pergunta binaria, detectada pelo gabarito que comeca com Sim ou Nao
    ruins = [p for p in perguntas
             if re.match(r'^Por qu[eê]', p)
             or re.search(r', e (qual|o que|como|por qu[eê])', p)
             or re.search(r'\bo [\wÀ-ÿ-]+ ou o [\wÀ-ÿ-]+\?$', p)]
    for i, p in enumerate(perguntas, 1):
        r = re.search(r'(?m)(?:^|·\s+)%d\.\s+(.*)' % i, texto_gab)
        if r and re.match(r'\*\*(N[aã]o|Sim)[.,;:]?\*\*', r.group(1).strip()) and p not in ruins:
            ruins.append(p)

    return {
        'nome': nome, 'linhas': linhas,
        'negrito': (len(re.findall(r'\*\*', s)) // 2) / linhas,
        'no_sistema': any('No sistema' in x for x in secoes) or not cod,
        'se_sobrar': any('Se sobrar' in x for x in secoes),
        'cod': len(cod), 'cobertos': len(cobertos),
        'falta': sorted(cod - cobertos),
        'pistas': len(perguntas), 'ruins': ruins,
    }


def main():
    filtro = sys.argv[1:]
    gabarito = io.open(os.path.join(NOTAS, '_PISTAS.md'), encoding='utf-8').read()
    arquivos = sorted(glob.glob(os.path.join(NOTAS, '[0-9][0-9]-*.md')))
    if filtro:
        arquivos = [f for f in arquivos if os.path.basename(f)[:2] in filtro]

    print('%-34s %5s %6s %4s %4s %8s %6s %5s'
          % ('nota', 'linh', 'negr', 'sis', 'sob', 'codigos', 'pistas', 'ruins'))
    tc = tk = tr = 0
    faltando = []
    for f in arquivos:
        a = audita(f, gabarito)
        tc += a['cobertos']; tk += a['cod']; tr += len(a['ruins'])
        if a['falta']:
            faltando.append((a['nome'][:8], a['falta']))
        print('%-34s %5d %6.2f %4s %4s %5d/%-2d %6d %5d'
              % (a['nome'][:34], a['linhas'], a['negrito'],
                 'ok' if a['no_sistema'] else 'NAO',
                 'ok' if a['se_sobrar'] else 'NAO',
                 a['cobertos'], a['cod'], a['pistas'], len(a['ruins'])))

    print('\ncobertura: %d de %d codigos (%.0f%%)  ·  pistas ruins: %d'
          % (tc, tk, 100.0 * tc / tk if tk else 100, tr))
    for nome, falta in faltando:
        print('  %s falta: %s' % (nome, ' '.join(falta)))


if __name__ == '__main__':
    main()
