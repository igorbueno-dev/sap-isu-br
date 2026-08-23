"""Regenera o que e derivado das notas.

    python ferramentas/gera.py             README.md e notas/_PISTAS.md
    python ferramentas/gera.py --caderno   caderno/, a variante para NotebookLM

Modo padrao. Escreve dois lugares, sempre a partir do resumo e do recall de
cada nota:

  README.md        a tabela das notas e a contagem de origem
  notas/_PISTAS.md as perguntas em fila. O gabarito abaixo do marcador nao
                   e tocado: ele e escrito a mao.

Assim o indice nunca diverge da nota: a nota e a fonte, o resto e derivado.

Modo --caderno. Escreve caderno/, que e a versao das mesmas fontes preparada
para ingestao por maquina, onde o arquivo e a unidade e nada fora dele existe:

  cada resposta fica colada na sua pergunta, em vez de morar no _PISTAS
  a Bancada perde as secoes de meta-estudo e fica so referencia

caderno/ e derivado e esta no .gitignore. Regerar e sempre mais barato que
versionar.
"""
import io, os, re, glob, shutil, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTAS = os.path.join(BASE, 'notas')
INICIO = '<!-- INICIO NOTAS -->'
FIM = '<!-- FIM NOTAS -->'
INICIO_ORIGEM = '<!-- INICIO ORIGEM -->'
FIM_ORIGEM = '<!-- FIM ORIGEM -->'
INICIO_PERG = '<!-- INICIO PERGUNTAS -->'
FIM_PERG = '<!-- FIM PERGUNTAS -->'

SIGNIFICADO = [
    ('slide', 'O material da academia sustenta a nota inteira'),
    ('misto', 'As listas e os nomes são do material. **O raciocínio em volta é meu**'),
    ('meu', 'O material dá o gancho, o desenvolvimento é meu. **Confirme antes de repetir**'),
]

# De onde veio o conteudo da nota. Ver a tabela de origem no README.
#   slide  o material da academia sustenta a nota inteira
#   misto  as listas sao do material, o raciocinio em volta e do autor
#   meu    o material da o gancho, o desenvolvimento e do autor
ORIGEM = {
    'GE-03': 'meu',  # Do problema ao módulo
    'GE-01': 'slide',  # O que é o SAP IS-U CCS
    'GE-02': 'slide',  # A evolução do produto
    'GE-04': 'misto',  # Os quatro mercados
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
    'DM-03': 'slide',  # O cadastro do equipamento
    'DM-04': 'slide',  # Planejamento de datas
    'DM-05': 'slide',  # O ciclo da leitura
    'BI-01': 'slide',  # Cálculo e Faturamento
    'BI-02': 'slide',  # Os dados mestres de cálculo
    'BI-03': 'slide',  # Anomalias
    'BI-04': 'slide',  # A impressão
    'CS-06': 'misto',  # A esteira do chamado
    'CS-07': 'misto',  # Reclamação de conta alta
    'CS-08': 'misto',  # Corte e religação
    'CS-09': 'misto',  # O que o atendente vê
}

FASES = [
    (('GE', 'MD', 'ST'), 'Fundação',
     'Valem para qualquer trilha. **A ordem é a ordem**: cada uma usa a anterior.'),
    (('CS',), 'Atendimento e relacionamento (CRM)',
     'As quatro últimas cruzam o CRM com as outras áreas. **Elas são o motivo\nde nada ser colapsado**: quem atende decide para onde o chamado vai.'),
    (('AR',), 'Arquitetura e integração', None),
    (('SV', 'WM', 'DM', 'PE'), 'Serviço de Campo e Equipamento (SVC / DM)', None),
    (('BI',), 'Cálculo e Faturamento (BILL)', None),
]


# Calibragem do autor para o tempo de leitura de uma nota. Trocar aqui muda
# todos os lugares que citam o total, porque nenhum deles e escrito a mao.
MINUTOS_POR_NOTA = 6

# Numeros que ficam na prosa, fora dos marcadores. Antes eram escritos a mao e
# envelheciam sozinhos: o README chegou a anunciar 31 notas e 131 perguntas
# quando ja eram 42 e 364. Cada padrao abaixo e reescrito a cada geracao.
CONTAGENS = [
    (r'as \d+ perguntas em voz alta', u'as %(perg)d perguntas em voz alta'),
    (r'### As \d+ perguntas primeiro', u'### As %(perg)d perguntas primeiro'),
    (r'\| \*\*\d+ horas?\*\* \| As \d+ notas',
     u'| **%(horas)d horas** | As %(notas)d notas'),
    (r'(?m)^# As \d+ notas$', u'# As %(notas)d notas'),
    (r'Cerca de \*\*\d+ minutos\*\* no total',
     u'Cerca de **%(minutos)d minutos** no total'),
]


def contagens(s, notas, perg, minutos, horas):
    """Reescreve na prosa todo numero que e derivado das notas."""
    valores = {'notas': notas, 'perg': perg, 'minutos': minutos, 'horas': horas}
    for padrao, molde in CONTAGENS:
        s = re.sub(padrao, molde % valores, s)
    return s


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
        bloco = re.split(r'^>', m.group(1), maxsplit=1, flags=re.M)[0]
        for item in re.finditer(r'^\d+\.\s+(.*?)(?=^\d+\.|\Z)', bloco, re.M | re.S):
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
            tabela.append('| # | Nota | O que é | Origem |')
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

    quantas = {}
    for f in arquivos:
        o = ORIGEM.get(os.path.basename(f)[3:8], 'misto')
        quantas[o] = quantas.get(o, 0) + 1
    origem = ['| Origem | Significa | Quantas |', '|---|---|---|']
    for chave, texto in SIGNIFICADO:
        origem.append('| **%s** | %s | %d |' % (chave, texto, quantas.get(chave, 0)))
    origem.append('| `⟨confirmar⟩` no texto '
                  '| Código ou nome de tabela de que não tenho certeza | |')

    n_notas = len(arquivos)
    minutos = n_notas * MINUTOS_POR_NOTA
    horas = int(round(minutos / 60.0))

    caminho_readme = os.path.join(BASE, 'README.md')
    s = io.open(caminho_readme, encoding='utf-8').read()
    a, b = s.index(INICIO) + len(INICIO), s.index(FIM)
    s = s[:a] + '\n' + '\n'.join(tabela) + '\n' + s[b:]
    a, b = s.index(INICIO_ORIGEM) + len(INICIO_ORIGEM), s.index(FIM_ORIGEM)
    s = s[:a] + '\n' + '\n'.join(origem) + '\n' + s[b:]
    s = contagens(s, n_notas, n_perg, minutos, horas)
    io.open(caminho_readme, 'w', encoding='utf-8', newline='').write(s)

    caminho_pistas = os.path.join(NOTAS, '_PISTAS.md')
    s = io.open(caminho_pistas, encoding='utf-8').read()
    a, b = s.index(INICIO_PERG) + len(INICIO_PERG), s.index(FIM_PERG)
    s = s[:a] + '\n' + '\n'.join(pistas) + '\n' + s[b:]
    s = contagens(s, n_notas, n_perg, minutos, horas)
    io.open(caminho_pistas, 'w', encoding='utf-8', newline='').write(s)

    print('README (%d notas) e _PISTAS.md (%d perguntas) gerados'
          % (len(arquivos), n_perg))


CADERNO = os.path.join(BASE, 'caderno')
BANCADA = os.path.join(BASE, 'referencia', '02-BANCADA.md')

# Secoes da Bancada que falam do estudo, e nao do sistema. Elas nao sobem:
# misturadas com a referencia, o modelo responde palpite sobre a prova com o
# mesmo tom com que responde sobre uma transacao.
PODA_BANCADA = [
    'O exercício de navegação que fixa a arquitetura',
    'As duas técnicas que resolvem quase tudo',
    'O que você resolve sozinho e o que você escala',
    'Os cinco erros mais comuns neste exercício',
    'O que costuma ser cobrado',
    'Tipos de exercício prático',
    'Os cinco testes que dizem se você está pronto',
]

# Um item de gabarito comeca em inicio de linha ou logo depois do ponto do
# meio que separa respostas curtas na mesma linha.
ITEM = re.compile(r'(?m)(?:^|·\s+)(\d{1,2})\.\s')


def gabaritos():
    """Le notas/_PISTAS.md e devolve {codigo: {numero: resposta}}."""
    s = io.open(os.path.join(NOTAS, '_PISTAS.md'), encoding='utf-8').read()
    s = s[s.index('# GABARITO'):]
    fora = {}
    blocos = list(re.finditer(r'(?m)^## ([A-Z]{2}-\d\d)\s*$', s))
    for i, m in enumerate(blocos):
        fim = blocos[i + 1].start() if i + 1 < len(blocos) else len(s)
        bloco = s[m.end():fim]
        bloco = re.sub(r'(?m)^\*\*[A-Z]{2}-\d\d:.*$', '', bloco)  # linha do titulo
        bloco = re.split(r'(?m)^---\s*$', bloco)[0]
        achados = list(ITEM.finditer(bloco))
        respostas = {}
        for j, a in enumerate(achados):
            corte = achados[j + 1].start() if j + 1 < len(achados) else len(bloco)
            texto = ' '.join(bloco[a.end():corte].split())
            respostas[int(a.group(1))] = texto
        fora[m.group(1)] = respostas
    return fora


def com_resposta(texto, respostas, cod):
    """Troca o bloco de Recall pelo mesmo bloco com a resposta colada."""
    m = re.search(r'(?ms)^## Recall\s*$(.*?)(?=^---|\Z)', texto)
    if not m:
        return texto, 0, 0
    corpo = re.split(r'(?m)^>', m.group(1), maxsplit=1)[0]
    perguntas = re.findall(r'(?m)^(\d{1,2})\. (.+)$', corpo)
    linhas = ['## Recall', '',
              '**Responda em voz alta antes de ler a resposta.**', '']
    faltando = 0
    for num, p in perguntas:
        r = respostas.get(int(num))
        linhas.append('**%s.** %s' % (num, p))
        if r:
            linhas.append('**Resposta:** %s' % r)
        else:
            linhas.append('**Resposta:** ⟨ausente no gabarito⟩')
            faltando += 1
        linhas.append('')
    novo = texto[:m.start()] + '\n'.join(linhas) + '\n' + texto[m.end():]
    return novo, len(perguntas), faltando


def poda(texto, titulos):
    """Remove secoes de nivel 2 pelo titulo, ate o proximo titulo de nivel 2."""
    for t in titulos:
        m = re.search(r'(?m)^## %s\s*$' % re.escape(t), texto)
        if not m:
            print('  aviso: secao nao encontrada na Bancada: %s' % t)
            continue
        prox = re.search(r'(?m)^## ', texto[m.end():])
        fim = m.end() + prox.start() if prox else len(texto)
        texto = texto[:m.start()] + texto[fim:]
    return texto


def caderno():
    if os.path.isdir(CADERNO):
        shutil.rmtree(CADERNO)
    os.makedirs(CADERNO)

    gab = gabaritos()
    arquivos = sorted(glob.glob(os.path.join(NOTAS, '[0-9][0-9]-*.md')))
    total = furos = 0
    for f in arquivos:
        nome = os.path.basename(f)
        s = io.open(f, encoding='utf-8').read()
        cod = re.match(r'^# ([A-Z]{2}-\d\d)', s).group(1)
        s, n, faltando = com_resposta(s, gab.get(cod, {}), cod)
        total += n
        furos += faltando
        if faltando:
            print('  %-42s %d de %d sem resposta' % (nome, faltando, n))
        io.open(os.path.join(CADERNO, nome), 'w',
                encoding='utf-8', newline='').write(s)

    b = io.open(BANCADA, encoding='utf-8').read()
    antes = b.count('\n')
    b = poda(b, PODA_BANCADA)
    io.open(os.path.join(CADERNO, '02-BANCADA.md'), 'w',
            encoding='utf-8', newline='').write(b)

    print('caderno/: %d notas com %d perguntas respondidas no proprio arquivo'
          % (len(arquivos), total - furos))
    print('caderno/02-BANCADA.md: %d linhas podadas de meta-estudo'
          % (antes - b.count('\n')))
    if furos:
        print('ATENCAO: %d perguntas sem resposta no gabarito' % furos)


if __name__ == '__main__':
    if '--caderno' in sys.argv:
        caderno()
    else:
        gerar()
