# PISTAS E GABARITO
### As 131 perguntas primeiro. As respostas no fim.

> **Como usar.** Responda em voz alta, ou no papel, antes de descer. Errar aqui
> vale mais do que reler a nota: é o erro que mostra onde o modelo tem buraco.
>
> **As perguntas são geradas** a partir do recall de cada nota. Para editar uma,
> edite a nota e rode `python ferramentas/gera.py`. **O gabarito é escrito à
> mão** e fica abaixo do marcador, intocado pelo gerador.

<!-- INICIO PERGUNTAS -->

---

## Fundação

**[GE-03: Do problema ao módulo](01-GE-03-do-problema-ao-modulo.md)**

1. Quais são as três perguntas que o sistema inteiro existe para responder?
2. Por que errar no corte é mais caro que errar no faturamento?
3. O que torna a venda de energia diferente de uma venda comum?

**[GE-01: O que é o SAP IS-U CCS](02-GE-01-o-que-e-is-u-ccs.md)**

1. Escreva as duas expansões, CCS e IS-U, corretamente.
2. Liste as cinco áreas funcionais na ordem da cadeia.
3. Onde BW aparece no desenho, e por que isso importa para a sua escolha de trilha?

**[GE-02: A evolução do produto, do R/3 ao SaaS](03-GE-02-evolucao-do-produto.md)**

1. Até quando o ECC tem manutenção garantida, e por que isso gera emprego?
2. Qual interface pertence a cada era?
3. O que muda e o que não muda do ECC para o S/4HANA?

**[GE-04: Os três setores, com peso igual](04-GE-04-os-tres-setores.md)**

1. O medidor de gás mede o que se cobra?
2. Um imóvel de saneamento tem quantas instalações, e por quê?
3. Em qual setor a estimativa de consumo é mais frequente, e por quê?
4. Em qual setor o corte é mais delicado?

**[MD-01: As quatro divisões dos dados mestres](05-MD-01-mapa-dos-dados-mestres.md)**

1. Quais são as quatro divisões, na ordem?
2. Por que os dados transacionais aparecem numa lista de dados mestres?
3. O que o material diz sobre a Estrutura Postal, e a que área ela pertence?
4. Qual o critério que separa dado mestre de dado transacional?
5. Um imóvel foi construído e ninguém se mudou ainda. Quais divisões já têm dado, e quais não?

**[MD-08: Os dois mundos e a validade no tempo](06-MD-08-os-dois-mundos.md)**

1. Em que ponto exato os dois mundos se tocam?
2. Qual é o nível mais alto dos dados mestres técnicos?
3. Por que a ordem do desenho não é a hierarquia?
4. O que acontece se você alterar a tarifa de uma instalação sem olhar a data de validade?

**[MD-02: A tradução do prédio](07-MD-02-a-traducao-do-predio.md)**

1. Traduza para SAP: prédio, apartamento, garagem, medidor, cliente.
2. Por que o Local de Consumo e o Local de Instalação de Equipamento são objetos diferentes?
3. Qual objeto liga o mundo comercial ao mundo técnico?

**[MD-03: Parceiro de Negócios, categoria e função](08-MD-03-parceiro-de-negocios.md)**

1. Quais são as três categorias, e qual quase não se usa?
2. Qual função é obrigatória para faturar?
3. Você criou um PN e ele não fatura. Qual a primeira hipótese?

**[MD-04: Parceiro de Negócios, os dados e o customizing](09-MD-04-parceiro-de-negocios-dados.md)**

1. Onde mora o endereço, no PN ou na Conta Contrato?
2. Qual transação define **quais campos aparecem** por função de PN?
3. A conta do cliente está indo para o endereço errado. Onde você olha primeiro?

**[MD-05: Conta Contrato](10-MD-05-conta-contrato.md)**

1. Qual o critério para agrupar contratos numa mesma conta contrato?
2. Solvência é do PN ou da conta contrato?
3. Onde fica o bloqueio de corte, e onde fica o bloqueio de faturamento?

**[ST-01: Objeto de Ligação](11-ST-01-objeto-de-ligacao.md)**

1. Qual campo é o relevante do Objeto de Ligação?
2. Ele é o nível mais alto ou mais baixo dos dados mestres técnicos?
3. Dois sobrados colados, com números prediais diferentes. Um ou dois objetos de ligação?

**[ST-02: Local de Consumo](12-ST-02-local-de-consumo.md)**

1. O Local de Consumo tem endereço próprio?
2. Quais os dois campos relevantes dele?
3. Um prédio de 40 apartamentos: quantos objetos de ligação e quantos locais de consumo?

**[ST-03: Instalação](13-ST-03-instalacao.md)**

1. Qual objeto guarda o tipo de tarifa?
2. O que é o Indicador de Baixa Renda e onde ele fica?
3. Conta veio com valor absurdo. Onde você olha antes de suspeitar do cálculo?

**[ST-04: Equipamento e Local de Instalação](14-ST-04-equipamento.md)**

1. Um prédio de 40 apartamentos tem quantos Locais de Instalação de Equipamento?
2. Além do medidor, o que mais é Equipamento?
3. Medidor trocado no campo, conta ainda com leitura do antigo. Hipótese?

**[MD-06: Contrato](15-MD-06-contrato.md)**

1. Quando o Contrato é criado?
2. Um contrato pode estar ligado a duas instalações?
3. Em que nível ocorre o cálculo?
4. Por que não existe transação de criar contrato?

**[MD-07: Move-In e Move-Out](16-MD-07-move-in-move-out.md)**

1. O morador se muda. O que acontece com a Instalação, e o que acontece com o Contrato?
2. O que sempre acompanha um Move-In?
3. Consumo registrado numa instalação sem contrato ativo. O que isso sugere?
4. Por que Move-In com data retroativa é caro?


---

## Atendimento e relacionamento (CRM)

**[CS-01: O que é CRM](17-CS-01-o-que-e-crm.md)**

1. CRM é uma tecnologia? Responda usando as três camadas da definição.
2. Onde começa e onde termina o escopo do CRM?
3. Qual o verbo central da definição, e por que isso muda o entendimento?
4. Se o cliente de uma concessionária não pode trocar de fornecedor, o que o CRM gerencia de fato?

**[CS-02: Ciclo de vida do cliente](18-CS-02-ciclo-de-vida-do-cliente.md)**

1. Liste as seis etapas na ordem.
2. Quais duas etapas pertencem a cada pilar?
3. Por que o ciclo é desenhado como círculo e não como linha?
4. Em que etapa um cliente de concessionária normalmente entra, e por quê?

**[CS-03: SAP CRM e os três pilares](19-CS-03-sap-crm-e-os-pilares.md)**

1. Quais os três pilares, e qual carrega o setor de utilities?
2. Qual a diferença entre um pilar e uma faixa vertical da matriz?
3. Cite um módulo de cada pilar.
4. O que é o S/4 Customer Engagement, e qual sua relação com o CRM clássico?

**[CS-04: CRM no contexto Utilities](20-CS-04-crm-no-contexto-utilities.md)**

1. CRM é um módulo dentro do IS-U? Justifique com uma palavra.
2. Qual a posição do CS + CRM na cadeia das cinco áreas?
3. Onde uma ligação nova entra no sistema?
4. Por que BW não conta como área funcional?
5. O que significa dizer que o SAP CRM integra com Salesforce?

**[CS-05: Processos e atividades no atendimento](21-CS-05-processos-e-atividades.md)**

1. Qual a diferença entre protocolo e atividade, e qual contém qual?
2. Por que o protocolo importa fora da empresa?
3. Cite quatro processos da lista de FOPs.
4. Alteração de titularidade corresponde a que processo no lado dos dados mestres?
5. Onde o conceito de "prospect" aparece como dado no sistema?


---

## Arquitetura e integração

**[AR-01: O landscape e as cinco camadas](22-AR-01-landscape-e-camadas.md)**

1. No landscape, o IS-U é back end ou front end em relação ao CRM?
2. Onde o BW aparece, e o que isso confirma?
3. Liste as cinco camadas da arquitetura, de cima para baixo.
4. O que ITS e CTI conectam, respectivamente?
5. Por que a existência de um middleware prova que CRM e IS-U são sistemas distintos?

**[AR-02: Middleware e replicação](23-AR-02-middleware-e-replicacao.md)**

1. Por que existe middleware entre CRM e IS-U?
2. O que significam BDoc e qRFC?
3. Descreva o caminho de replicação de um BP, do CRM ao IS-U.
4. Um cliente criado no CRM não chegou ao IS-U. Qual sua sequência de investigação, com as transações?
5. Qual a diferença entre `R3AS` e `R3AR2`?

**[AR-03: Objetos replicados](24-AR-03-objetos-replicados.md)**

1. Qual objeto tem o mesmo nome de tabela nos dois sistemas, e por quê?
2. Por que Objeto de Ligação vira `COMM_PRODUCT` no CRM?
3. O que significa `IBASE`?
4. Alguém fala em "Business Agreement". Do que está falando?
5. De onde vêm os nomes de tabela desta nota?


---

## Serviço de Campo (SVC)

**[SV-01: Serviço de Campo (SVC) e os três blocos](25-SV-01-servico-de-campo.md)**

1. Quais são os três blocos do SVC, e qual a frase de uma linha de cada?
2. Por que a sigla `SVC` é ambígua?
3. Por que Perdas é um bloco separado, e não parte de WM ou de DM?
4. A cadeia das cinco áreas está errada por não ter Perdas?
5. Qual objeto a esteira de sete etapas cita sem nunca definir?

**[WM-01: A nota de serviço e o ciclo do campo](26-WM-01-nota-de-servico.md)**

1. Quais são os quatro campos que a nota carrega ao nascer, e o que cada um decide?
2. Cite quatro dos sete tipos de nota de serviço.
3. O que é uma transgressão, e por que "suspensão" existe?
4. Um técnico chega e o imóvel está trancado. O que registrar, e por quê?
5. Qual tipo de nota é a porta de entrada da Gestão de Perdas?

**[WM-02: Workflow e as quatro integrações do campo](27-WM-02-workflow-e-integracoes.md)**

1. Quais são as quatro integrações do serviço de campo, e qual delas é o motor?
2. Dunning corta o cliente? Explique quem faz o quê.
3. Cliente pagou e foi cortado. Qual é o mecanismo por trás?
4. Uma nota pode ter mais de um workflow?
5. Você abre o workflow e o responsável da etapa travada é `WF BATCH`. O que isso te diz?
6. Alguém diz "registrei a solicitação e nada aconteceu". Qual seu primeiro suspeito?

**[DM-01: Ativos, movimentação e estoque](28-DM-01-ativos-e-estoque.md)**

1. Qual é o corte entre esta nota e a DM-02?
2. Para que servem TC e TP, e qual o erro caro associado a eles?
3. Descreva o ciclo de vida do equipamento. Onde está o laço, e por quê?
4. Qual é a única saída definitiva de um equipamento do parque?
5. O técnico chegou em campo sem o medidor. Onde você procura a causa?
6. Por que "histórico completo" é a frente que sustenta perícia?

**[DM-02: Leituras e registradores](29-DM-02-leituras-e-registradores.md)**

1. Quais são os três eixos, e que pergunta cada um responde?
2. Um cliente ligou e passou o número do medidor. Que tipo de leitura é essa?
3. Trocaram um medidor. Quantas leituras isso gera, e o que acontece se faltar uma?
4. Uma instalação teve três leituras num mês. Isso é erro?
5. O que é energia injetada, e por que ela existe?
6. Uma instalação não faturou e o medidor está corretamente instalado. Qual sua primeira hipótese?

**[PE-01: Gestão de Perdas, fraude e defeito](30-PE-01-fraude-e-defeito.md)**

1. Em uma frase, o que a Gestão de Perdas faz?
2. Quais dos seis gatilhos escalam, e por quê?
3. Qual é a diferença entre fraude e defeito, e qual não muda entre as duas?
4. O que é um by-pass? E uma inversão de ligação?
5. Por que classificar errado é o erro mais caro desta área, nos dois sentidos?
6. Como um caso de Perdas nasce dentro de WM e de DM?

**[PE-02: Faturado da época x fatura revista](31-PE-02-faturado-da-epoca.md)**

1. O que é faturado da época, e o que é fatura revista?
2. A fatura antiga é cancelada no processo de revisão?
3. Qual é o insumo mais disputado do cálculo, e o que limita a disputa?
4. Quais são as três saídas da diferença apurada, e por que a terceira importa?
5. O que precisa ser verdade sobre a memória de cálculo para a cobrança se sustentar?
6. Por que o recálculo separa TE e TUSD, e o que o prefixo `ISUBR` indica?

<!-- FIM PERGUNTAS -->

---

# GABARITO

> **Daqui para baixo são as respostas.** Só desça depois de ter tentado.

## GE-03
**GE-03: Do problema ao módulo**  ·  [voltar para a nota](01-GE-03-do-problema-ao-modulo.md)

1. **Onde** está ligado, **quanto** consumiu, **por quanto** é cobrado.
2. Porque envolve deslocar uma pessoa, e cortar quem pagou vira processo
   judicial e multa do regulador. Erro de faturamento se corrige com estorno.
3. O consumo vem antes da autorização e antes do pagamento. Não há pedido,
   não há vendedor, e o produto é invisível.

---

## GE-01
**GE-01: O que é o SAP IS-U CCS**  ·  [voltar para a nota](02-GE-01-o-que-e-is-u-ccs.md)

1. Customer Care Service, e Industry Solutions for Utilities.
2. CS+CRM, WM, DM, BILL, FI-CA.
3. Como faixa transversal, por baixo das cinco. BW enxerga tudo mas não é
   parte do CCS, e por isso não está entre as trilhas disponíveis.

---

## GE-02
**GE-02: A evolução do produto, do R/3 ao SaaS**  ·  [voltar para a nota](03-GE-02-evolucao-do-produto.md)

1. Fim de 2027. Força a migração de toda a base instalada para S/4HANA, o que
   gera projetos.
2. SAP GUI na clássica, Fiori na moderna, Web/nativo em nuvem no futuro SaaS.
3. Muda a tecnologia (HANA, tempo real) e a interface. **Não muda o modelo de
   dados de negócio** nem os conceitos do CCS.

---

## GE-04
**GE-04: Os três setores, com peso igual**  ·  [voltar para a nota](04-GE-04-os-tres-setores.md)

1. **Não.** Mede volume em m³, a cobrança é por energia. Há conversão no meio.
2. **Duas**, água e esgoto. A de esgoto normalmente não tem medidor e fatura
   como percentual da água.
3. **Saneamento**, por medidor embaçado, enterrado ou inacessível.
4. **Saneamento**, por ser o mais sensível juridicamente. A régua de cobrança
   costuma ser mais conservadora.

---

## MD-01
**MD-01: As quatro divisões dos dados mestres**  ·  [voltar para a nota](05-MD-01-mapa-dos-dados-mestres.md)

1. Estrutura Postal, Dados Mestre Técnicos, Dados Mestre Comercial, Dados
   Transacionais.
2. Para servir de **contraste**. Ela não é dado mestre, e é justamente isso
   que define os outros três por oposição.
3. **Só o nome.** O material lista a Estrutura Postal e nunca a desenvolve. A
   única pista é que **manter estruturas políticas e postais é
   responsabilidade de WM**. O conteúdo dela é pergunta em aberto.
4. **Duração da validade.** Mestre dura muito e é a única versão válida no
   período. Transacional é dinâmico e vale pouco tempo.
5. Já têm dado: **Dados Mestres Técnicos** (o prédio, o local de consumo e a
   instalação existem sem morador). Não têm: **Comerciais** e
   **Transacionais**, porque não há quem pague nem o que medir.

---

## MD-02
**MD-02: A tradução do prédio**  ·  [voltar para a nota](07-MD-02-a-traducao-do-predio.md)

1. Objeto de Ligação, Local de Consumo, Local de Instalação de Equipamento,
   Equipamento, Parceiro de Negócios.
2. Porque o lugar onde se **consome** não é o lugar onde o aparelho está
   **instalado**. No prédio, consome-se no apartamento e mede-se na garagem.
3. O **Contrato**.

---

## MD-03
**MD-03: Parceiro de Negócios, categoria e função**  ·  [voltar para a nota](08-MD-03-parceiro-de-negocios.md)

1. Pessoa, Organização e Grupo. Grupo normalmente não é utilizada.
2. **Parceiro de Contrato.**
3. Que ele não tem a função Parceiro de Contrato, ou tem só função de
   Pessoa de Contato, que não carrega contrato.

---

## MD-04
**MD-04: Parceiro de Negócios, os dados e o customizing**  ·  [voltar para a nota](09-MD-04-parceiro-de-negocios-dados.md)

1. **No PN.** Mas o direcionamento por função pode ser feito no nível da
   Conta Contrato.
2. `BUCG`, agrupamento de campos por função de PN.
3. No endereço standard do PN, e depois no endereço de correspondência da
   Conta Contrato, que é herdado do PN mas pode ser sobreposto.

---

## MD-05
**MD-05: Conta Contrato**  ·  [voltar para a nota](10-MD-05-conta-contrato.md)

1. **Mesmos dados de pagamento e cobrança.**
2. Do **PN** (business partner level).
3. Bloqueio de corte/cobrança na **Conta Contrato**. Bloqueio de faturamento
   no **Contrato**.

---

## MD-06
**MD-06: Contrato**  ·  [voltar para a nota](15-MD-06-contrato.md)

1. Durante o **Move In**, ou em troca de titularidade / nova ligação.
2. **Não.** Um contrato liga a exatamente uma Conta Contrato e uma Instalação.
3. **No nível do Contrato.**
4. Porque ele é resultado do processo de Move In, não de cadastro direto.

---

## MD-07
**MD-07: Move-In e Move-Out**  ·  [voltar para a nota](16-MD-07-move-in-move-out.md)

1. A **Instalação permanece**, é do imóvel. O **Contrato é encerrado**, é da
   pessoa.
2. Uma **leitura inicial**.
3. **Ligação clandestina.** O sistema monitora imóveis desocupados justamente
   por isso.
4. Porque obriga a desfazer e refazer todo o faturamento posterior à data.

---

## ST-01
**ST-01: Objeto de Ligação**  ·  [voltar para a nota](11-ST-01-objeto-de-ligacao.md)

1. **Endereço.**
2. **Mais alto.**
3. **Dois.** Cada número predial é um Objeto de Ligação.

---

## ST-02
**ST-02: Local de Consumo**  ·  [voltar para a nota](12-ST-02-local-de-consumo.md)

1. **Não.** Ele assume o endereço do Objeto de Ligação e guarda só o
   complemento.
2. Tipo do Local de Consumo, e Complemento do endereço.
3. **Um** objeto de ligação, **quarenta** locais de consumo.

---

## ST-03
**ST-03: Instalação**  ·  [voltar para a nota](13-ST-03-instalacao.md)

1. A **Instalação**, no bloco Faturamento e Medição.
2. Marcação de tarifa social, campo brasileiro, no bloco Informações
   Individuais da **Instalação**.
3. Nos dados mestres da **Instalação**: tarifa, vigência da tarifa, unidade
   de leitura e tipo de validação.

---

## ST-04
**ST-04: Equipamento e Local de Instalação**  ·  [voltar para a nota](14-ST-04-equipamento.md)

1. Normalmente **um**, com os 40 relógios juntos.
2. **Transformador de Corrente (TC).**
3. Foi feita instalação **técnica** (`EG33`) sem a parte **com efeito no
   cálculo** (`EG34`). Faltou completar a instalação.

---

## CS-01
**CS-01: O que é CRM**  ·  [voltar para a nota](17-CS-01-o-que-e-crm.md)

1. Não. É **práticas + estratégias de negócio + tecnologias**. A tecnologia
   é a terceira camada, não a definição.
2. Da **prospecção** até a **fidelização e retenção**. Ciclo inteiro, não só a venda.
3. **Conhecer.** Conhecer comportamento e necessidades para antecipar desejos.
   Vender é consequência.
4. **Custo e qualidade do atendimento.** Num monopólio o cliente insatisfeito
   não cancela, ele reclama, e reclamação tem preço com o regulador.

---

## CS-02
**CS-02: Ciclo de vida do cliente**  ·  [voltar para a nota](18-CS-02-ciclo-de-vida-do-cliente.md)

1. Prospecção, Qualificação, Conversão, Venda, Pós-venda, Fidelização.
2. Marketing: prospecção e qualificação. Vendas: conversão e venda.
   Serviços: pós-venda e fidelização.
3. Porque **a fidelização realimenta a prospecção**: cliente fiel indica outro.
4. Na etapa 5, **pós-venda**. Ele não foi prospectado nem convertido: mudou-se para um imóvel que já
   tinha ligação. Entrou por Move-In.

---

## CS-03
**CS-03: SAP CRM e os três pilares**  ·  [voltar para a nota](19-CS-03-sap-crm-e-os-pilares.md)

1. **Marketing, Vendas (Sales) e Serviço (Service)**. Serviço carrega utilities.
2. Pilar é **área de negócio** (linha da matriz). Faixa vertical é **canal**
   (Web Channel, Interaction Center, Partner Channel Management) e atravessa
   os três pilares.
3. Exemplos: Marketing → Campaign Management. Sales → Opportunity Management.
   Service → Customer Service & Support.
4. Versão **simplificada do SAP CRM embutida no S/4HANA**, que aproveita a
   tecnologia do CRM Web UI e entrega o **S/4HANA Interaction Center**.

---

## CS-04
**CS-04: CRM no contexto Utilities**  ·  [voltar para a nota](20-CS-04-crm-no-contexto-utilities.md)

1. Não. O material diz **camada** de atendimento **integrada** ao IS-U/CCS. É um
   sistema por cima, não um módulo dentro.
2. **A primeira.** `CS + CRM → WM → DM → BILL → FI-CA`.
3. No **CS + CRM**, que oferece os serviços ao cliente (new connection,
   reconnection).
4. Porque aparece como **faixa única atravessando as cinco**, não como caixa
   na fila. É camada de informação sobre todas.
5. Que **pode existir mais de um CRM** na paisagem. Salesforce na ponta e SAP
   CRM no meio é arranjo comum.

---

## CS-05
**CS-05: Processos e atividades**  ·  [voltar para a nota](21-CS-05-processos-e-atividades.md)

1. **Protocolo** é o número que o cliente recebe e acompanha; **atividade** é
   o registro do que foi feito. **Um protocolo contém várias atividades.**
2. Porque ele **prova prazo de atendimento perante o regulador**.
3. Ligação Nova, Alteração de titularidade, Segundas Vias, Reclamações,
   Cadastro, Modificações Contratuais.
4. O material liga os dois pontos: "Alteração de titularidade" está na lista
   de processos do CRM, e o Contrato **"é criado quando ocorre uma nova ligação
   ou troca de titularidade"**. Se é literalmente Move-Out mais Move-In,
   **está em aberto**.
5. No campo **Status** do Parceiro de Negócios, com valores Cliente,
   **Prospect**, Inativo.

---

## AR-01
**AR-01: O landscape e as cinco camadas**  ·  [voltar para a nota](22-AR-01-landscape-e-camadas.md)

1. **Back end.** O CRM fica no meio, o IS-U atrás dele.
2. No quadrante **Analyses**, junto do back end. Confirma que BW é camada de
   dados, não área funcional.
3. Canais → Camada CRM → Middleware → Camada IS-U/CCS → Integrações externas.
4. **ITS** conecta ao **WebClient**; **CTI** conecta ao **Call Center**.
5. Porque **middleware só existe entre sistemas distintos**. Se fossem o mesmo
   sistema, com a mesma base, replicar não faria sentido.

---

## AR-02
**AR-02: Middleware e replicação**  ·  [voltar para a nota](23-AR-02-middleware-e-replicacao.md)

1. Porque CRM e IS-U são sistemas separados com bases próprias, e o mesmo
   cliente precisa existir nos dois.
2. **BDoc** = Business Document, o envelope do dado. **qRFC** = queued Remote
   Function Call, a fila que garante ordem.
3. `CRM cria BP → SMW01 BDoc → SMQ1 fila qRFC → RFC comunicação → IS-U recebe
   → BUT000 criado`.
4. `SMW01` (o BDoc saiu?) → `SMQ1` e `SMQ2` (parou na fila?) → `SM58` (a
   conexão caiu?) → `ST22` (deu dump?).
5. `R3AS` é **carga inicial**, traz tudo na implantação. `R3AR2` é
   **repetição de carga**, para o que não veio.

---

## AR-03
**AR-03: Objetos replicados**  ·  [voltar para a nota](24-AR-03-objetos-replicados.md)

1. O **Parceiro de Negócios**, `BUT000` dos dois lados. É objeto central
   compartilhado do SAP, e o primeiro a replicar.
2. Porque para o CRM o que existe naquele endereço é um **produto
   contratado**. A estrutura física é problema do IS-U.
3. **Installed Base**, a base instalada: o que o cliente tem instalado.
4. De **Conta Contrato**. `CRMM_BUAG`, de Business Agreement, é o nome dela
   no CRM.
5. Do **slide de replicação da Aula 02**, que traz o de-para completo. Não
   são dedução nem memória: estão no material.

---

## MD-08
**MD-08: Os dois mundos e a validade no tempo**  ·  [voltar para a nota](06-MD-08-os-dois-mundos.md)

1. No **Contrato indo para a Instalação**. É a única ligação entre os dois
   lados; todo o resto desce dentro do próprio mundo.
2. O **Objeto de Ligação**.
3. Porque o desenho lista do **mais específico para o mais genérico**, e a
   hierarquia física vai do **prédio para o medidor**. São ordens inversas.
4. Você pode ter **alterado o passado**: se a nova tarifa valer desde uma data
   antiga, o sistema vai querer refaturar meses já fechados.
---

## SV-01
**SV-01: Serviço de Campo (SVC) e os três blocos**  ·  [voltar para a nota](25-SV-01-servico-de-campo.md)

1. **WM / SVC**, manda gente para a rua. **DM / GAT**, cuida do que fica
   pendurado na parede. **Perdas**, descobre que o número estava errado e
   cobra a diferença.
2. Porque designa **os dois níveis**: é o nome do guarda-chuva, a área
   inteira, e também o apelido do Bloco 1.
3. Porque é o que acontece quando WM e DM, **juntos**, descobrem que a medição
   não representava a realidade. A fiscalização é nota (WM), o medidor
   adulterado é ativo (DM), mas **o recálculo não é de nenhum dos dois**.
4. Não. Ela responde **por onde o dado passa**; os três blocos respondem
   **quem senta junto**. Dois mapas do mesmo território.
5. A **Ordem**. A etapa 5 diz "equipe recebe a ordem" e o objeto nunca é
   apresentado.

---

## WM-01
**WM-01: A nota de serviço e o ciclo do campo**  ·  [voltar para a nota](26-WM-01-nota-de-servico.md)

1. **Tipo de processo** (que trabalho é), **motivo** (por que foi pedido),
   **prioridade** (ordem na fila) e **prazo** (o relógio regulatório).
2. Corte, religação, fiscalização, modificação, inspeção, ligação nova,
   substituição de medidor.
3. **Transgressão é o prazo regulatório estourado**, e é infração com valor,
   não atraso administrativo. **Suspensão** existe para parar o relógio quando
   a culpa não é da concessionária.
4. O **evento de paralisação** e a **suspensão** do prazo. Sem isso o relógio
   continua correndo e vira transgressão que não existiu.
5. **Fiscalização.**

---

## WM-02
**WM-02: Workflow e as quatro integrações do campo**  ·  [voltar para a nota](27-WM-02-workflow-e-integracoes.md)

1. **CRM, Dunning, Billing/FI-CA e Workflow.** O workflow é o **motor**; os
   outros três são portas.
2. Não. **Dunning decide e manda; quem corta é o WM**, por nota de serviço.
3. **Descompasso de relógios.** A régua de cobrança rodou no ciclo dela, o
   pagamento entrou pelo ciclo do banco depois, e a nota de corte já tinha
   saído.
4. **Sim.** O caso real desta nota tinha quatro workflows na mesma nota
   de serviço.
5. Que rodou **automático, em job**, sem pessoa envolvida. Se travou, ninguém
   percebeu até alguém reclamar.
6. **O workflow travado, não a nota.** A nota provavelmente existe; o que não
   andou foi o fluxo.

---

## DM-01
**DM-01: Ativos, movimentação e estoque**  ·  [voltar para a nota](28-DM-01-ativos-e-estoque.md)

1. Aqui é o **aparelho como bem patrimonial**; na DM-02, **o número que ele
   produz**.
2. Reduzem o sinal de cliente grande a uma escala que o medidor aguenta, e o
   sistema multiplica de volta por uma **constante**. Constante errada faz a
   conta errar **por um fator**, não por um pouco.
3. Recebimento em estoque → transferência → instalação em campo → retirada →
   manutenção → **volta ao estoque**. O laço está na manutenção: o mesmo
   número de série é instalado de novo, em outro imóvel.
4. **Sucateamento.**
5. No **estoque**: reserva não feita ou não respeitada. É erro de estoque que
   aparece como falha de campo.
6. Porque quando o cliente contesta, é o **histórico do número de série** que
   reconstrói o que aconteceu com aquele aparelho.

---

## DM-02
**DM-02: Leituras e registradores**  ·  [voltar para a nota](29-DM-02-leituras-e-registradores.md)

1. **Tipo** (como o número foi obtido), **motivo** (por que foram ler) e
   **registrador** (o que foi medido).
2. **Leitura informada.**
3. **Três:** de retirada (o velho), de instalação (o novo) e de troca (amarra
   o par). Faltando uma, **o consumo do mês fica sem dono**.
4. Não. **Três dos cinco motivos** são disparados por evento, não pelo ciclo.
5. É o registrador de quem **gera** energia e manda o excedente para a rede.
   Existe porque o cliente virou gerador.
6. **Falta a relação registrador/tarifa.** Instalado tecnicamente, não
   instalado para faturamento.

---

## PE-01
**PE-01: Gestão de Perdas, fraude e defeito**  ·  [voltar para a nota](30-PE-01-fraude-e-defeito.md)

1. Descobre que o medidor não contava a verdade, **calcula quanto deveria ter
   sido cobrado** e cobra a diferença.
2. **Consumo atípico, análises estatísticas e monitoramento de indicadores.**
   Fiscalizar milhões de imóveis a pé é inviável; achar por padrão e mandar
   técnico só onde vale a pena é o que torna a área possível.
3. **Fraude é ação intencional, defeito é falha técnica.** O que **não** muda:
   as duas produzem consumo medido menor que o real.
4. **By-pass** é uma ponte que contorna o medidor. **Inversão de ligação** é a
   troca de posição dos cabos, e é a mais difícil de achar porque nada parece
   violado por fora.
5. Nos dois sentidos: defeito classificado como fraude **acusa um inocente de
   crime**; fraude classificada como defeito **entrega dinheiro e não pune**.
6. A fiscalização em campo é uma **nota de serviço** tipo Fiscalização (WM), e
   a leitura tirada lá tem **motivo** Fiscalização (DM).

---

## PE-02
**PE-02: Faturado da época x fatura revista**  ·  [voltar para a nota](31-PE-02-faturado-da-epoca.md)

1. **Faturado da época** é o que o cliente pagou com o medidor errado.
   **Fatura revista** é o que ele deveria ter pago.
2. **Não.** A fatura antiga continua existindo, e a revisão é documento novo
   ao lado dela. O histórico precisa mostrar as duas versões.
3. O **período da irregularidade**. Os **critérios regulatórios** limitam até
   onde se pode voltar no tempo.
4. **Receita recuperada, débito adicional e crédito ao cliente.** A terceira
   dá credibilidade: defeito pode fazer o aparelho contar **a mais**, e uma
   área que só produz débito está calibrada errado.
5. Que **um terceiro consiga refazer o cálculo e chegar no mesmo número.**
6. Porque **TE e TUSD têm alíquotas e destinos diferentes**. E `ISUBR` indica
   **localização Brasil**.
