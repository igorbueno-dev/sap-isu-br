"""Gera as duas camadas rapidas de leitura a partir das 31 notas.

_MAPA.md    todos os resumos em fila, a camada de 4 minutos
_PISTAS.md  todas as perguntas de recall em fila, a camada de teste

Os dois sao gerados. Nunca edite a mao: edite a nota e rode isto de novo.
    python ferramentas/gera-camadas.py
"""
import io, os, re, glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTAS = os.path.join(BASE, 'notas')

# Os arquivos ja estao em ordem de leitura no disco (prefixo 01 a 31).
# A fase muda quando o codigo entra num bloco de area.
FASES = [
    (('GE', 'MD', 'ST'), 'Fundacao, vale para qualquer trilha'),
    (('CS',), 'Atendimento e relacionamento (CRM)'),
    (('AR',), 'Arquitetura e integracao'),
    (('SV', 'WM', 'DM', 'PE'), 'Servico de Campo (SVC)'),
]


def fase_de(codigo):
    for prefixos, rotulo in FASES:
        if codigo[:2] in prefixos:
            return rotulo
    return 'Outras'


def ler(caminho):
    return io.open(caminho, encoding='utf-8').read()


def partes(texto):
    """Devolve (titulo, resumo, perguntas) de uma nota."""
    linhas = texto.split('\n')
    titulo = linhas[0].lstrip('# ').strip()

    resumo = []
    for l in linhas[1:]:
        if l.startswith('>'):
            resumo.append(l.lstrip('> ').rstrip())
        elif resumo:
            break
        elif l.strip() and not l.startswith('>'):
            break

    perguntas = []
    m = re.search(r'^## Recall\s*$(.*?)(?=^---|^## |\Z)', texto, re.M | re.S)
    if m:
        bloco = m.group(1)
        for item in re.finditer(r'^\d+\.\s+(.*?)(?=^\d+\.|\Z)', bloco, re.M | re.S):
            p = ' '.join(item.group(1).split())
            if p:
                perguntas.append(p)

    return titulo, ' '.join(resumo), perguntas


def gerar():
    arquivos = sorted(glob.glob(os.path.join(NOTAS, '[0-9][0-9]-*.md')))
    mapa = ["""# O MAPA
### Os resumos das 31 notas, em fila

> **Arquivo gerado.** Nao edite aqui: edite a nota e rode
> `python ferramentas/gera-camadas.py`.
>
> **Como usar.** Esta e a camada de 4 minutos. Leia de ponta a ponta antes da
> aula. Onde voce nao conseguir completar a ideia sozinho, abra a nota.
>
> **A ordem aqui e a ordem da pasta**, e as duas sao a ordem de estudo.
"""]
    pistas = ["""# AS PISTAS
### Todas as perguntas de recuperacao, em fila

> **Arquivo gerado.** Nao edite aqui: edite a nota e rode
> `python ferramentas/gera-camadas.py`.
>
> **Como usar.** Responda em voz alta antes de abrir qualquer coisa. Errar aqui
> vale mais do que reler a nota: e o erro que mostra onde o modelo tem buraco.
> Gabarito em [`_GABARITOS.md`](_GABARITOS.md).
"""]

    n_notas = n_perg = 0
    atual = None
    for f in arquivos:
        nome = os.path.basename(f)
        rotulo = fase_de(nome[3:5])
        if rotulo != atual:
            atual = rotulo
            mapa.append('\n---\n\n## %s\n' % rotulo)
            pistas.append('\n---\n\n## %s\n' % rotulo)
        titulo, resumo, perguntas = partes(ler(f))
        n_notas += 1
        mapa.append('**[%s](%s)**  \n%s\n' % (titulo, nome, resumo))
        if perguntas:
            pistas.append('**[%s](%s)**\n' % (titulo, nome))
            for i, p in enumerate(perguntas, 1):
                pistas.append('%d. %s' % (i, p))
                n_perg += 1
            pistas.append('')

    rodape = '\n---\n\n> %d notas, %d perguntas.\n' % (n_notas, n_perg)
    io.open(os.path.join(NOTAS, '_MAPA.md'), 'w', encoding='utf-8', newline='').write(
        '\n'.join(mapa) + rodape)
    io.open(os.path.join(NOTAS, '_PISTAS.md'), 'w', encoding='utf-8', newline='').write(
        '\n'.join(pistas) + rodape)
    print('_MAPA.md e _PISTAS.md gerados: %d notas, %d perguntas' % (n_notas, n_perg))


if __name__ == '__main__':
    gerar()
