"""Regenera o que e derivado das 31 notas.

    python ferramentas/gera.py

Escreve dois lugares, sempre a partir do resumo e do recall de cada nota:

  README.md        a tabela das notas, entre os marcadores INICIO/FIM NOTAS
  notas/_PISTAS.md as perguntas de recuperacao em fila, para testar tudo

Assim o indice nunca diverge da nota: a nota e a fonte, o resto e derivado.
"""
import io, os, re, glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTAS = os.path.join(BASE, 'notas')
INICIO = '<!-- INICIO NOTAS -->'
FIM = '<!-- FIM NOTAS -->'

# De onde veio o conteudo da nota. Ver a tabela de origem no README.
#   slide  o material da academia sustenta a nota inteira
#   misto  as listas sao do material, o raciocinio em volta e do autor
#   meu    o material da o gancho, o desenvolvimento e do autor
ORIGEM = {
    'GE-03': 'meu',  # Do problema ao módulo
    'GE-01': 'slide',  # O que é o SAP IS-U CCS
    'GE-02': 'slide',  # A evolução do produto
    'GE-04': 'misto',  # Os três setores
    'MD-01': 'slide',  # As quatro divisões
    'MD-08': 'slide',  # Os dois mundos e a validade no tempo
    'MD-02': 'slide',  # A tradução do prédio
    'MD-03': 'slide',  # Parceiro de Negócios
    'MD-04': 'slide',  # PN, dados e customizing
    'MD-05': 'slide',  # Conta Contrato
    'ST-01': 'slide',  # Objeto de Ligação
    'ST-02': 'slide',  # Local de Consumo
    'ST-03': 'slide',  # Instalação
    'ST-04': 'misto',  # Equipamento e Registrador
    'MD-06': 'slide',  # Contrato
    'MD-07': 'meu',  # Move-In e Move-Out
    'CS-01': 'slide',  # O que é CRM
    'CS-02': 'slide',  # Ciclo de vida do cliente
    'CS-03': 'slide',  # SAP CRM e os três pilares
    'CS-04': 'slide',  # CRM no contexto Utilities
    'CS-05': 'slide',  # Processos e atividades
    'AR-01': 'slide',  # O landscape e as cinco camadas
    'AR-02': 'slide',  # Middleware e replicação
    'AR-03': 'slide',  # Objetos replicados
    'SV-01': 'misto',  # Serviço de Campo e os três blocos
    'WM-01': 'misto',  # A nota de serviço
    'WM-02': 'misto',  # Workflow e integrações
    'DM-01': 'misto',  # Ativos, movimentação e estoque
    'DM-02': 'misto',  # Leituras e registradores
    'PE-01': 'misto',  # Fraude e defeito
    'PE-02': 'misto',  # Faturado da época x fatura revista
}

FASES = [
    (('GE', 'MD', 'ST'), 'Fundacao',
     'Valem para qualquer trilha. A ordem e a ordem: cada uma usa a anterior.'),
    (('CS',), 'Atendimento e relacionamento (CRM)', None),
    (('AR',), 'Arquitetura e integracao', None),
    (('SV', 'WM', 'DM', 'PE'), 'Servico de Campo (SVC)', None),
]


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
    perguntas = []
    m = re.search(r'^## Recall\s*$(.*?)(?=^---|^## |\Z)', s, re.M | re.S)
    if m:
        for item in re.finditer(r'^\d+\.\s+(.*?)(?=^\d+\.|\Z)', m.group(1), re.M | re.S):
            p = ' '.join(item.group(1).split())
            if p:
                perguntas.append(p)
    return titulo, ' '.join(resumo), perguntas


def fase_de(codigo):
    for prefixos, rotulo, sub in FASES:
        if codigo[:2] in prefixos:
            return rotulo, sub
    return 'Outras', None


def gerar():
    arquivos = sorted(glob.glob(os.path.join(NOTAS, '[0-9][0-9]-*.md')))
    tabela, pistas = [], []
    atual = None
    n_perg = 0

    for f in arquivos:
        nome = os.path.basename(f)
        num, cod = nome[:2], nome[3:8]
        rotulo, sub = fase_de(cod)
        titulo, resumo, perguntas = partes(f)
        tema = titulo.split(':', 1)[1].strip() if ':' in titulo else titulo

        if rotulo != atual:
            atual = rotulo
            tabela.append('\n### %s\n' % rotulo)
            if sub:
                tabela.append('%s\n' % sub)
            tabela.append('| # | Nota | O que e | Origem |')
            tabela.append('|---|---|---|---|')
            pistas.append('\n---\n\n## %s\n' % rotulo)

        tabela.append('| **%s** | [`%s` %s](notas/%s) | %s | %s |'
                      % (num, cod, tema, nome, resumo, ORIGEM.get(cod, 'misto')))
        if perguntas:
            pistas.append('**[%s](%s)**\n' % (titulo, nome))
            for i, p in enumerate(perguntas, 1):
                pistas.append('%d. %s' % (i, p))
                n_perg += 1
            pistas.append('')

    caminho_readme = os.path.join(BASE, 'README.md')
    s = io.open(caminho_readme, encoding='utf-8').read()
    a, b = s.index(INICIO) + len(INICIO), s.index(FIM)
    s = s[:a] + '\n' + '\n'.join(tabela) + '\n' + s[b:]
    io.open(caminho_readme, 'w', encoding='utf-8', newline='').write(s)

    cabeca = """# AS PISTAS
### Todas as perguntas de recuperacao, em fila

> **Arquivo gerado.** Nao edite aqui: edite a nota e rode
> `python ferramentas/gera.py`.
>
> **Como usar.** Responda em voz alta antes de abrir qualquer coisa. Errar aqui
> vale mais do que reler a nota: e o erro que mostra onde o modelo tem buraco.
> Gabarito em [`_GABARITOS.md`](_GABARITOS.md).
"""
    io.open(os.path.join(NOTAS, '_PISTAS.md'), 'w', encoding='utf-8', newline='').write(
        cabeca + '\n'.join(pistas)
        + '\n---\n\n> %d notas, %d perguntas.\n' % (len(arquivos), n_perg))

    print('README (%d notas) e _PISTAS.md (%d perguntas) gerados'
          % (len(arquivos), n_perg))


if __name__ == '__main__':
    gerar()
