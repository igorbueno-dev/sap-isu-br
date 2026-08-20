"""Colapsa as areas nao escolhidas depois da decisao de trilha.

A semana 1 e panoramica: cada area recebeu um dia. Na semana 2 so uma delas
e aprofundada. As outras deixam de precisar de profundidade, mas continuam
podendo cair em prova, entao viram uma pagina de mapa em vez de sumirem.

    python ferramentas/colapsa-areas.py --trilha SVC
    python ferramentas/colapsa-areas.py --trilha CRM --confirmar

Sem --confirmar ele so mostra o que faria.

As notas colapsadas vao para notas/_profundidade/ e continuam versionadas.
Para desfazer:  git mv notas/_profundidade/CS-*.md notas/
"""
import io, os, re, glob, sys, argparse

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTAS = os.path.join(BASE, 'notas')
FUNDO = os.path.join(NOTAS, '_profundidade')

TRILHAS = {
    'CRM': (['CS'], 'Atendimento e relacionamento'),
    'ARQ': (['AR'], 'Arquitetura e integracao'),
    'SVC': (['SV', 'WM', 'DM', 'PE'], 'Servico de Campo'),
}
FUNDACAO = ['GE', 'MD', 'ST']


def partes(caminho):
    s = io.open(caminho, encoding='utf-8').read()
    linhas = s.split('\n')
    titulo = linhas[0].lstrip('# ').strip()
    resumo = []
    for l in linhas[1:]:
        if l.startswith('>'):
            resumo.append(l.lstrip('> ').rstrip())
        elif resumo:
            break
    secoes = [t.strip() for t in re.findall(r'^#{2,3}\s+(.*)$', s, re.M)
              if t.strip() not in ('Recall',)]
    return titulo, ' '.join(resumo), secoes


def pagina(prefixos, rotulo, arquivos):
    out = ['# MAPA: %s' % rotulo,
           '> Area **nao escolhida** como trilha. Esta pagina guarda o nivel que a',
           '> semana 1 entregou: os nomes, as listas e a fronteira entre os assuntos.',
           '',
           '**As notas completas nao foram apagadas.** Estao em',
           '[`_profundidade/`](_profundidade/), a um clique, caso a avaliacao cobre',
           'esta area ou voce queira voltar a ela depois.',
           '', '---', '']
    for f in arquivos:
        titulo, resumo, secoes = partes(f)
        nome = os.path.basename(f)
        out.append('## %s' % titulo)
        out.append('%s' % resumo)
        out.append('')
        out.append('O que a nota completa cobre:')
        for sec in secoes:
            out.append('- %s' % sec)
        out.append('')
        out.append('> Nota completa: [`%s`](_profundidade/%s)' % (nome, nome))
        out.append('')
        out.append('---')
        out.append('')
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--trilha', required=True, choices=sorted(TRILHAS))
    ap.add_argument('--confirmar', action='store_true')
    a = ap.parse_args()

    escolhida = TRILHAS[a.trilha][0]
    total_antes = total_depois = 0

    for chave, (prefixos, rotulo) in sorted(TRILHAS.items()):
        arquivos = []
        for p in prefixos:
            arquivos += sorted(glob.glob(os.path.join(NOTAS, '%s-*.md' % p)))
        linhas = sum(io.open(f, encoding='utf-8').read().count('\n') for f in arquivos)
        total_antes += linhas
        if prefixos == escolhida:
            print('MANTIDA   %-28s %2d notas  %4d linhas' % (rotulo, len(arquivos), linhas))
            total_depois += linhas
            continue
        texto = pagina(prefixos, rotulo, arquivos)
        n = texto.count('\n')
        total_depois += n
        print('COLAPSADA %-28s %2d notas  %4d -> %3d linhas' % (rotulo, len(arquivos), linhas, n))
        if not a.confirmar:
            continue
        if not os.path.isdir(FUNDO):
            os.makedirs(FUNDO)
        destino = os.path.join(NOTAS, '_AREA-%s.md' % chave)
        io.open(destino, 'w', encoding='utf-8', newline='').write(texto)
        for f in arquivos:
            os.rename(f, os.path.join(FUNDO, os.path.basename(f)))

    fund = sum(io.open(f, encoding='utf-8').read().count('\n')
               for p in FUNDACAO for f in glob.glob(os.path.join(NOTAS, '%s-*.md' % p)))
    print()
    print('Fundacao intocada: %d linhas' % fund)
    print('Areas: %d -> %d linhas  (%.0f%% fora do caminho)'
          % (total_antes, total_depois, 100.0 * (total_antes - total_depois) / total_antes))
    if not a.confirmar:
        print()
        print('Simulacao. Rode de novo com --confirmar para executar.')


if __name__ == '__main__':
    main()
