# SAP IS-U CCS, referência em português

Notas sobre **SAP IS-U CCS** (*Industry Solutions for Utilities / Customer Care
Service*), a solução setorial que roda o ciclo comercial de concessionárias de
energia, água e gás.

Quase não existe material estruturado de IS-U em português. Este repositório é
uma tentativa de mudar isso, em aberto, com correção de quem conhece o módulo
na prática.

**Se for ler só uma coisa, leia [`MD‑02`](notas/07-MD-02-a-traducao-do-predio.md).**
É o diagrama que traduz um prédio de verdade nos objetos do sistema, e resolve
metade da confusão inicial com dados mestres.

**Se tiver quatro minutos, leia [`_MAPA.md`](notas/_MAPA.md)**, que são os 31
resumos em fila. É o acervo inteiro em uma página, e a melhor forma de decidir
o que abrir depois.

---

# As 31 notas

Cada nota é um conceito só: 5 a 10 minutos, terminando em raciocínio fechado.

> **O número na frente do arquivo é a ordem de estudo.** Abra a pasta
> [`notas/`](notas/) e leia de cima para baixo: nenhuma nota depende de uma que
> venha depois dela. A tabela abaixo é a mesma ordem, com o que cada uma
> entrega.

### Fundação, notas 01 a 16

Valem para qualquer trilha. **A ordem é a ordem**: cada uma usa a anterior.

| # | Nota | Tema | Status | O gancho | Tempo |
|---|---|---|---|---|---|
| **01** | [`GE‑03`](notas/01-GE-03-do-problema-ao-modulo.md) | **Do problema ao módulo** | a confirmar | O negócio em 5 parágrafos, e o mapa para o CCS. **Leia primeiro** | 5 min |
| **02** | [`GE‑01`](notas/02-GE-01-o-que-e-is-u-ccs.md) | O que é o SAP IS-U CCS | verificado | As duas siglas, as cinco áreas, e por que BW não é uma delas | 6 min |
| **03** | [`GE‑02`](notas/03-GE-02-evolucao-do-produto.md) | A evolução do produto | verificado | Do R/3 ao SaaS, e a data de 2027 que gera projeto | 4 min |
| **04** | [`GE‑04`](notas/04-GE-04-os-tres-setores.md) | Os três setores | a confirmar | Energia, gás e água. Muda a resposta do exercício | 5 min |
| **05** | [`MD‑01`](notas/05-MD-01-mapa-dos-dados-mestres.md) | **As quatro divisões** | verificado | Cada uma explicada, e as duas comparações | 7 min |
| **06** | [`MD‑08`](notas/06-MD-08-os-dois-mundos.md) | Os dois mundos e a validade no tempo | verificado | O diagrama, a ponte, e a armadilha da ordem invertida | 6 min |
| **07** | [`MD‑02`](notas/07-MD-02-a-traducao-do-predio.md) | **A tradução do prédio** | verificado | O diagrama que converte o mundo real em SAP | 6 min |
| **08** | [`MD‑03`](notas/08-MD-03-parceiro-de-negocios.md) | Parceiro de Negócios | verificado | Categoria é o que ele é, função é o papel. Sem Parceiro de Contrato, não fatura | 7 min |
| **09** | [`MD‑04`](notas/09-MD-04-parceiro-de-negocios-dados.md) | PN, dados e customizing | verificado | Os seis blocos, os endereços, e as 17 transações de configuração | 8 min |
| **10** | [`MD‑05`](notas/10-MD-05-conta-contrato.md) | Conta Contrato | verificado | A bolsa financeira. E onde mora o bloqueio de corte | 7 min |
| **11** | [`ST‑01`](notas/11-ST-01-objeto-de-ligacao.md) | Objeto de Ligação | verificado | O prédio. Nível mais alto, e onde mora o endereço | 5 min |
| **12** | [`ST‑02`](notas/12-ST-02-local-de-consumo.md) | Local de Consumo | verificado | O apartamento. Onde mora o complemento, não o endereço | 5 min |
| **13** | [`ST‑03`](notas/13-ST-03-instalacao.md) | **Instalação** | verificado | O objeto que fatura. Tarifa, unidade de leitura, validação | 6 min |
| **14** | [`ST‑04`](notas/14-ST-04-equipamento.md) | Equipamento e Registrador | misto | O medidor, o TC, as três formas de instalar | 8 min |
| **15** | [`MD‑06`](notas/15-MD-06-contrato.md) | **Contrato** | verificado | A dobradiça, as oito regras, e por que não existe "criar contrato" | 6 min |
| **16** | [`MD‑07`](notas/16-MD-07-move-in-move-out.md) | **Move-In e Move-Out** | a confirmar | O processo que cria o Contrato. Fecha a maior lacuna do modelo | 6 min |

### Atendimento e relacionamento, CRM, notas 17 a 21

| # | Nota | Tema | Status | O gancho | Tempo |
|---|---|---|---|---|---|
| **17** | [`CS‑01`](notas/17-CS-01-o-que-e-crm.md) | O que é CRM | verificado | Práticas, estratégia e só então tecnologia | 5 min |
| **18** | [`CS‑02`](notas/18-CS-02-ciclo-de-vida-do-cliente.md) | Ciclo de vida do cliente | verificado | Seis etapas, três pilares, e onde a concessionária vive | 5 min |
| **19** | [`CS‑03`](notas/19-CS-03-sap-crm-e-os-pilares.md) | SAP CRM e os três pilares | verificado | A matriz funcional, e o S/4 Customer Engagement | 7 min |
| **20** | [`CS‑04`](notas/20-CS-04-crm-no-contexto-utilities.md) | **CRM no contexto Utilities** | verificado | O encaixe na cadeia das cinco áreas | 6 min |
| **21** | [`CS‑05`](notas/21-CS-05-processos-e-atividades.md) | Processos e atividades | verificado | Protocolo, atividade e os processos do dia a dia | 6 min |

### Arquitetura e integração, notas 22 a 24

| # | Nota | Tema | Status | O gancho | Tempo |
|---|---|---|---|---|---|
| **22** | [`AR‑01`](notas/22-AR-01-landscape-e-camadas.md) | O landscape e as cinco camadas | verificado | Onde cada sistema mora | 6 min |
| **23** | [`AR‑02`](notas/23-AR-02-middleware-e-replicacao.md) | **Middleware e replicação** | verificado | Como o dado atravessa, e as 4 transações que resolvem chamado | 7 min |
| **24** | [`AR‑03`](notas/24-AR-03-objetos-replicados.md) | Objetos replicados | verificado | O de-para CRM ↔ IS-U | 5 min |

### Serviço de Campo, SVC, notas 25 a 31

> **As sete notas de SVC são `misto`.** A fonte original é uma apresentação
> panorâmica: ela dá as listas, os nomes e a fronteira entre os blocos. **O
> raciocínio em volta é meu**, montado com o resto do material e com
> conhecimento do setor elétrico. Trate as listas como fato e o resto como
> interpretação, e me corrija por issue onde eu errei.

| # | Nota | Tema | Status | O gancho | Tempo |
|---|---|---|---|---|---|
| **25** | [`SV‑01`](notas/25-SV-01-servico-de-campo.md) | **Serviço de Campo e os três blocos** | misto | Quatro nomes para a mesma área. **Comece por aqui** | 6 min |
| **26** | [`WM‑01`](notas/26-WM-01-nota-de-servico.md) | A nota de serviço | misto | Os sete tipos, os quatro campos, e onde mora a multa | 6 min |
| **27** | [`WM‑02`](notas/27-WM-02-workflow-e-integracoes.md) | Workflow e integrações | misto | As quatro portas do campo, e o diagnóstico de "pedi e não aconteceu" | 6 min |
| **28** | [`DM‑01`](notas/28-DM-01-ativos-e-estoque.md) | Ativos, movimentação e estoque | misto | O ciclo de vida do medidor, e o laço que faz o histórico importar | 6 min |
| **29** | [`DM‑02`](notas/29-DM-02-leituras-e-registradores.md) | **Leituras e registradores** | misto | Três eixos que parecem um só. E a energia injetada | 6 min |
| **30** | [`PE‑01`](notas/30-PE-01-fraude-e-defeito.md) | **Fraude e defeito** | misto | Mesmo efeito na medição, mundos jurídicos diferentes | 5 min |
| **31** | [`PE‑02`](notas/31-PE-02-faturado-da-epoca.md) | Faturado da época x fatura revista | misto | O cálculo que vira dinheiro de volta | 6 min |

**Tudo: cerca de 185 minutos.** Para a revisão rápida, use
[`_MAPA.md`](notas/_MAPA.md), que são os 31 resumos em 4 minutos.

---

## Por que esta ordem

`MD‑06`, o Contrato, é o único conceito que **exige os dois ramos completos**:
precisa da Conta Contrato do lado comercial e da Instalação do lado técnico.
Por isso ele é a nota **15**, e não a sexta dos dados mestres comerciais.

Antes dele, os dois ramos descem em paralelo e podem ser lidos assim:

| Comercial, 08 a 10 | Técnico, 11 a 14 |
|---|---|
| `MD‑03` → `MD‑04` → `MD‑05` | `ST‑01` → `ST‑02` → `ST‑03` → `ST‑04` |

Depois de `MD‑06` vem `MD‑07`, o Move-In, que é o processo que **cria** o
Contrato. O grafo completo está em
[`notas/_DEPENDENCIAS.md`](notas/_DEPENDENCIAS.md).

**As áreas, 17 a 31, são independentes entre si.** Depois da escolha de trilha,
só uma delas continua valendo leitura profunda.

## As quatro que mais valem

1. **[`GE‑03`](notas/01-GE-03-do-problema-ao-modulo.md)**, do problema ao módulo. Sem o
   problema de negócio, o resto vira decoreba.
2. **[`MD‑02`](notas/07-MD-02-a-traducao-do-predio.md)**, a tradução do prédio.
3. **[`MD‑06`](notas/15-MD-06-contrato.md)**, o Contrato. O mais denso em regra.
4. **[`ST‑03`](notas/13-ST-03-instalacao.md)**, a Instalação. O objeto que fatura.

---

# Material de apoio

| Arquivo | Para quê |
|---|---|
| [`notas/_MAPA.md`](notas/_MAPA.md) | **Os 31 resumos em fila. A revisão de 4 minutos.** Gerado |
| [`notas/_PISTAS.md`](notas/_PISTAS.md) | **As 131 perguntas em fila. A sessão de teste.** Gerado |
| [`referencia/02-BANCADA.md`](referencia/02-BANCADA.md) | Transações, tabelas e caminhos de menu. É consulta, use `Ctrl+F` |
| [`notas/_GABARITOS.md`](notas/_GABARITOS.md) | Respostas dos recalls, separadas de propósito |
| [`notas/_PADRAO.md`](notas/_PADRAO.md) | A forma da nota, e o que nunca pode ocupar posição estrutural |
| [`notas/_DEPENDENCIAS.md`](notas/_DEPENDENCIAS.md) | A ordem de estudo e os pontos em aberto |

---

# Como isto funciona

**Nota atômica.** Um conceito por arquivo, teto de 120 linhas. Se cresce, vira
duas. Cada nota termina em **recall**, com perguntas sem resposta à vista.

**Nada aqui pede confiança cega.** Duas marcas dizem o grau:

| Marca | Significa |
|---|---|
| **verificado** | Conferido contra o sistema ou material de produto |
| **a confirmar** | Escrito por raciocínio e leitura, não conferido na documentação SAP |
| **(confirmar)** no texto | Código de transação específico de que não tenho certeza |

Prefiro a dúvida explícita a um código errado que alguém vai digitar na frente
de um cliente.

# Como contribuir

**Todo `(confirmar)` é um convite.** Se você roda IS-U em produção, sua
resposta vale mais que uma semana de leitura minha.

- **[Corrigir conteúdo](../../issues/new?template=correcao-de-conteudo.yml)**,
  quando algo está errado, incompleto ou confuso
- **[Confirmar transação](../../issues/new?template=confirmar-transacao.yml)**,
  quando você sabe um código marcado como duvidoso
- **[Ver o que está aberto](../../issues)**, se quiser pegar algo pronto
- [`CONTRIBUTING.md`](CONTRIBUTING.md) para o resto

Se você leu uma nota e não entendeu, **a nota está mal escrita**. Isso também
vale issue, e é o defeito que eu não consigo enxergar sozinho.

---

Trabalho independente, sem vínculo com a SAP nem com qualquer empregador.
SAP, SAP IS-U e S/4HANA são marcas da SAP SE. Nada aqui reproduz material de
treinamento proprietário, e este repositório não é fonte oficial: para decisão
de projeto, consulte a documentação da SAP.
