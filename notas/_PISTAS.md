# PISTAS E GABARITO
### As 367 perguntas primeiro. As respostas no fim.

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
2. O que separa a venda de energia de uma venda comum?
3. Uma concessionária corta o fornecimento de quem já havia pagado. Cite o que torna esse erro mais caro que um erro de faturamento.
4. Qual pedaço do CCS resolve o problema de receber o dinheiro?

**[GE-01: O que é o SAP IS-U CCS](02-GE-01-o-que-e-is-u-ccs.md)**

1. Escreva a expansão de CCS.
2. Escreva a expansão de IS-U.
3. Ordene as cinco áreas funcionais na ordem da cadeia.
4. Onde o BW aparece no desenho das cinco áreas?
5. O BW é uma das cinco áreas?

**[GE-02: A evolução do produto, do R/3 ao SaaS](03-GE-02-evolucao-do-produto.md)**

1. Até quando o ECC tem manutenção garantida?
2. Cite o efeito dessa data sobre o mercado de trabalho.
3. Qual interface pertence a cada era do produto?
4. O que muda do ECC para o S/4HANA?
5. O que não muda do ECC para o S/4HANA?

**[GE-04: Os quatro mercados, com peso igual](04-GE-04-os-quatro-mercados.md)**

1. Nomeie os quatro mercados atendidos pelo SAP IS-U.
2. O medidor de gás mede o que se cobra?
3. Quantas instalações tem um imóvel de saneamento?
4. O que explica esse número de instalações?
5. Em qual mercado a estimativa de consumo é mais frequente?
6. Em qual mercado o corte é mais delicado?

**[MD-01: As quatro divisões dos dados mestres](05-MD-01-mapa-dos-dados-mestres.md)**

1. Quais são as quatro divisões dos dados mestres, na ordem?
2. Qual é o papel dos Dados Transacionais dentro dessa lista?
3. O que o material da aula diz sobre o conteúdo da Estrutura Postal?
4. A que área pertence a manutenção das estruturas postais?
5. Qual o critério que separa dado mestre de dado transacional?
6. Um imóvel foi construído e ninguém se mudou ainda. Qual divisão já tem dado?
7. Qual par de tabelas liga o endereço à unidade de leitura?
8. Cite o que esse par explica sobre a posição da Estrutura Postal na lista.
9. Uma rua nova foi cadastrada e as instalações dela não entraram em nenhuma ordem de leitura. Cite onde olhar.

**[MD-08: Os dois mundos e a validade no tempo](06-MD-08-os-dois-mundos.md)**

1. Em que ponto exato os dois mundos se tocam?
2. Qual é o nível mais alto dos dados mestres técnicos?
3. O que separa a ordem do desenho da hierarquia real dos objetos?
4. Cite os três objetos do material em que o campo de validade aparece.
5. Uma tarifa foi alterada sem olhar a data. Cite a consequência.

**[MD-02: A tradução do prédio](07-MD-02-a-traducao-do-predio.md)**

1. Como o SAP chama o prédio?
2. Como o SAP chama o apartamento?
3. Como o SAP chama a garagem onde ficam os medidores?
4. Como o SAP chama o medidor?
5. Como o SAP chama o cliente?
6. O que separa o Local de Consumo do Local de Instalação de Equipamento?
7. Qual objeto liga o mundo comercial ao mundo técnico?

**[MD-03: Parceiro de Negócios, categoria e função](08-MD-03-parceiro-de-negocios.md)**

1. Qual transação cria um Parceiro de Negócios?
2. Qual transação modifica um Parceiro de Negócios?
3. Qual transação exibe um Parceiro de Negócios?
4. Nomeie as três categorias de Parceiro de Negócios.
5. Qual das três categorias quase não se usa?
6. Qual função é obrigatória para faturar o cliente?
7. O que separa categoria de função?
8. Você criou um PN e ele não fatura. Cite a primeira hipótese.

**[MD-04: Parceiro de Negócios, os dados e o customizing](09-MD-04-parceiro-de-negocios-dados.md)**

1. Qual transação define agrupamentos e atribuição de faixas de numeração?
2. Qual transação define o tipo de endereço padrão por função?
3. Qual transação define as formas de tratamento?
4. Qual transação define as regras de formatação de nome?
5. Qual transação define as formas jurídicas?
6. Qual transação define a entidade legal?
7. Qual transação define o layout de tela?
8. Qual transação define as faixas de numeração de relacionamento?
9. Onde mora o endereço, no PN ou na Conta Contrato?
10. A conta do cliente está indo para o endereço errado. Cite onde olhar primeiro.

**[MD-05: Conta Contrato](10-MD-05-conta-contrato.md)**

1. Qual transação cria uma Conta Contrato?
2. Qual transação modifica uma Conta Contrato?
3. Qual transação exibe uma Conta Contrato?
4. Qual transação ativa modificações planejadas?
5. Qual o critério para agrupar contratos numa mesma conta contrato?
6. Solvência é do Parceiro de Negócios ou da Conta Contrato?
7. Onde fica o bloqueio de corte?
8. Onde fica o bloqueio de faturamento?

**[ST-01: Objeto de Ligação](11-ST-01-objeto-de-ligacao.md)**

1. Qual transação cria um Objeto de Ligação?
2. Qual transação modifica um Objeto de Ligação?
3. Qual transação exibe um Objeto de Ligação?
4. Qual é o campo relevante do Objeto de Ligação?
5. O Objeto de Ligação é o nível mais alto ou o mais baixo dos dados mestres técnicos?
6. Dois sobrados colados, com números prediais diferentes. Um ou dois Objetos de Ligação?

**[ST-02: Local de Consumo](12-ST-02-local-de-consumo.md)**

1. Qual transação cria um Local de Consumo?
2. Qual transação modifica um Local de Consumo?
3. Qual transação exibe um Local de Consumo?
4. O Local de Consumo tem endereço próprio?
5. Nomeie os dois campos relevantes do Local de Consumo.
6. Um prédio de 40 apartamentos tem quantos Objetos de Ligação?
7. O mesmo prédio tem quantos Locais de Consumo?
8. Um colega diz que `ES61` cria o Local de Consumo. Ele está certo?

**[ST-03: Instalação](13-ST-03-instalacao.md)**

1. Qual transação cria uma Instalação?
2. Qual transação modifica uma Instalação?
3. Qual transação exibe uma Instalação?
4. Qual objeto guarda o tipo de tarifa?
5. O que é o Indicador de Baixa Renda?
6. Em qual objeto fica o Indicador de Baixa Renda?
7. Uma conta veio com valor absurdo. Cite onde olhar antes de suspeitar do cálculo.

**[ST-04: Equipamento e Local de Instalação](14-ST-04-equipamento.md)**

1. Qual transação cria um Local de Instalação de Equipamento?
2. Qual transação modifica um Local de Instalação de Equipamento?
3. Qual transação exibe um Local de Instalação de Equipamento?
4. Qual transação faz a instalação total do equipamento?
5. Qual transação faz só a instalação técnica?
6. Qual transação faz só a parte com efeito no cálculo da fatura?
7. Qual transação estorna a instalação técnica?
8. Um prédio de 40 apartamentos tem quantos Locais de Instalação de Equipamento?
9. Além do medidor, o que mais é cadastrado como Equipamento?
10. Um medidor foi trocado no campo e a conta ainda usa a leitura do antigo. Cite a causa mais provável.

**[MD-06: Contrato](15-MD-06-contrato.md)**

1. Qual transação modifica um Contrato?
2. Qual transação exibe um Contrato?
3. Qual transação modifica todos os contratos?
4. Qual transação exibe todos os contratos?
5. Quando o Contrato é criado?
6. Um contrato pode estar ligado a duas instalações?
7. Em que nível ocorre o cálculo?
8. O que cria o Contrato, já que não existe transação de criar?

**[MD-07: Move-In e Move-Out](16-MD-07-move-in-move-out.md)**

1. O morador se muda. O que acontece com a Instalação?
2. O morador se muda. O que acontece com o Contrato?
3. O que sempre acompanha um Move-In?
4. Há consumo registrado numa instalação sem contrato ativo. Cite o que isso sugere.
5. Um Move-In foi lançado com data retroativa. Cite a consequência.


---

## Atendimento e relacionamento (CRM)

**[CS-01: O que é CRM](17-CS-01-o-que-e-crm.md)**

1. O CRM é uma tecnologia?
2. Nomeie as três camadas da definição de CRM.
3. Onde começa o escopo do CRM?
4. Onde termina o escopo do CRM?
5. Qual o verbo central da definição de CRM?
6. O cliente de uma concessionária não pode trocar de fornecedor. Cite o que o CRM ainda decide nesse caso.

**[CS-02: Ciclo de vida do cliente](18-CS-02-ciclo-de-vida-do-cliente.md)**

1. Liste as seis etapas do ciclo de vida do cliente, na ordem.
2. Quais duas etapas pertencem ao pilar Marketing?
3. Quais duas etapas pertencem ao pilar Vendas?
4. Quais duas etapas pertencem ao pilar Serviço?
5. O que faz o ciclo ser um círculo e não uma linha?
6. Em qual etapa um cliente de concessionária normalmente entra?
7. O que explica ele entrar por essa etapa?

**[CS-03: SAP CRM e os três pilares](19-CS-03-sap-crm-e-os-pilares.md)**

1. Nomeie os três pilares do SAP CRM.
2. Qual dos três pilares carrega o setor de utilities?
3. O que separa um pilar de uma faixa vertical da matriz?
4. Nomeie as três faixas verticais da matriz.
5. Cite um módulo do pilar Marketing.
6. Cite um módulo do pilar Vendas.
7. Cite um módulo do pilar Serviço.
8. Como o SAP chama hoje a versão do CRM embutida no S/4HANA?
9. O que essa versão entrega no lugar do Interaction Center clássico?

**[CS-04: CRM no contexto Utilities](20-CS-04-crm-no-contexto-utilities.md)**

1. O CRM é um módulo dentro do IS-U?
2. Qual a palavra que o material usa para descrever a relação entre CRM e IS-U?
3. Qual a posição do CS + CRM na cadeia das cinco áreas?
4. Ordene as cinco áreas da cadeia.
5. Onde uma ligação nova entra no sistema?
6. O BW conta como área funcional?
7. Como o BW aparece no desenho da cadeia?
8. Uma paisagem tem Salesforce e SAP CRM ao mesmo tempo. Isso é erro de arquitetura?

**[CS-05: Processos e atividades no atendimento](21-CS-05-processos-e-atividades.md)**

1. Qual tabela guarda o Parceiro de Negócios, onde mora o status de prospect?
2. O que separa protocolo de atividade?
3. Qual dos dois contém o outro?
4. Cite o que torna o protocolo importante fora da empresa.
5. Cite quatro processos da lista de FOPs.
6. A que processo do lado dos dados mestres corresponde a Alteração de titularidade?
7. Em qual campo do Parceiro de Negócios aparece o conceito de prospect?

**[CS-06: A esteira do chamado, do protocolo ao fechamento](22-CS-06-a-esteira-do-chamado.md)**

1. Qual objeto encerra a esteira de Ligação Nova?
2. Em que ponto da esteira de Ligação Nova o Contrato é criado?
3. Por qual área passa um pedido de Segunda Via?
4. Quais três áreas uma reclamação de valor pode atravessar?
5. Quem decide o corte, e quem o executa?
6. Ordene a esteira de Ligação Nova: Contrato, instalação do equipamento, nota de serviço, protocolo.
7. Um atendente promete ao cliente o prazo do protocolo para uma ligação nova. Cite a consequência.
8. Um cliente pede religação depois de pagar. Cite a área que confirma o pagamento.

**[CS-07: Reclamação de conta alta, o roteiro de diagnóstico](23-CS-07-reclamacao-de-conta-alta.md)**

1. Nomeie as cinco causas de conta alta, na ordem de investigação.
2. Qual o critério que ordena essa lista?
3. Em qual das saídas o cliente paga mais depois de reclamar?
4. Qual par de transações, se incompleto, faz a conta usar o medidor antigo?
5. Onde se verifica se a leitura foi estimada?
6. O que separa a causa "tarifa errada" da causa "irregularidade" quanto a quem executa a correção?
7. Um atendente abre fiscalização como primeiro passo. Cite o desperdício.
8. Um cliente reclama de conta alta e o histórico está estável. Cite as duas causas mais prováveis.

**[CS-08: Corte e religação, o descompasso que gera chamado](24-CS-08-corte-e-religacao.md)**

1. Quem decide o corte?
2. Quem executa o corte?
3. Quem confirma o pagamento?
4. Em qual objeto mora o bloqueio de corte?
5. Nomeie as quatro verificações do atendimento, na ordem.
6. O que separa corte de religação quanto a prazo?
7. Um cliente pagou e foi cortado. Cite a causa estrutural.
8. Um cliente apresenta o comprovante e pede religação imediata. Cite o que o comprovante não prova.

**[CS-09: O que o atendente vê, e onde mora o resto](25-CS-09-o-que-o-atendente-ve.md)**

1. Nomeie os quatro objetos que existem dos dois lados.
2. Qual objeto tem o mesmo nome de tabela nos dois sistemas?
3. Qual o nome da Conta Contrato no CRM?
4. Em que o Objeto de Ligação se transforma do lado do CRM?
5. O Contrato replica para o CRM?
6. Em qual sistema está a resposta para "quanto eu consumi"?
7. Em qual sistema está a resposta para "estou devendo"?
8. Um dado não aparece na tela do CRM. Cite a conclusão errada que isso costuma gerar.
9. Um dado existe nos dois sistemas com valores diferentes. Cite onde está o problema.


---

## Arquitetura e integração

**[AR-01: O landscape e as cinco camadas](26-AR-01-landscape-e-camadas.md)**

1. No landscape, o IS-U é back end ou front end em relação ao CRM?
2. Liste as cinco camadas da arquitetura, de cima para baixo.
3. Em qual quadrante o BW aparece?
4. O que a posição do BW confirma sobre ele?
5. O que o ITS conecta?
6. O que o CTI conecta?
7. O que a existência de um middleware prova sobre CRM e IS-U?

**[AR-02: Middleware e replicação](27-AR-02-middleware-e-replicacao.md)**

1. Qual transação mostra os BDocs e se algum falhou?
2. Qual transação mostra a fila de entrada?
3. Qual transação mostra a fila de saída?
4. Qual transação monitora a conexão RFC?
5. Qual transação mostra o log do sistema?
6. Qual transação mostra o dump de programa?
7. Qual transação faz a carga inicial?
8. Qual transação repete a carga do que não veio?
9. O que significa BDoc?
10. O que significa qRFC?
11. Descreva o caminho de replicação de um Parceiro de Negócios, do CRM ao IS-U.
12. O que separa carga inicial de fluxo do dia?
13. Um cliente criado no CRM não chegou ao IS-U. Cite as quatro verificações, na ordem.

**[AR-03: Objetos replicados](28-AR-03-objetos-replicados.md)**

1. Qual tabela guarda o Parceiro de Negócios no IS-U?
2. Qual tabela guarda o Parceiro de Negócios no CRM?
3. Qual tabela guarda a Conta Contrato no IS-U?
4. Qual tabela guarda a Conta Contrato no CRM?
5. Qual tabela guarda o Objeto de Ligação no IS-U?
6. Em que objeto o Objeto de Ligação se transforma no CRM?
7. Qual tabela guarda o Ponto de Entrega no IS-U?
8. O que significa `IBASE`?
9. Qual objeto tem o mesmo nome de tabela nos dois sistemas?
10. Alguém fala em Business Agreement. Do que está falando?
11. De onde vêm os nomes de tabela desta nota?


---

## Serviço de Campo e Equipamento (SVC / DM)

**[SV-01: Serviço de Campo (SVC) e os três blocos](29-SV-01-servico-de-campo.md)**

1. Nomeie os três blocos do SVC.
2. Em uma linha, o que o bloco WM faz?
3. Em uma linha, o que o bloco DM faz?
4. Em uma linha, o que o bloco Perdas faz?
5. O que torna a sigla `SVC` ambígua?
6. O que justifica Perdas ser um bloco separado, e não parte de WM ou de DM?
7. A cadeia das cinco áreas está errada por não ter Perdas?
8. O que separa a cadeia das cinco áreas dos três blocos do SVC?
9. Qual objeto a esteira de sete etapas cita sem nunca definir?

**[WM-01: A nota de serviço e o ciclo do campo](30-WM-01-nota-de-servico.md)**

1. Nomeie os quatro campos que a nota de serviço carrega ao nascer.
2. O que o campo tipo de processo decide?
3. O que o campo prazo decide?
4. Cite quatro dos sete tipos de nota de serviço.
5. O que é uma transgressão?
6. Para que serve a suspensão de prazo?
7. Qual tipo de nota é a porta de entrada da Gestão de Perdas?
8. Um técnico chega e o imóvel está trancado. Cite o que registrar.
9. Cite o que acontece se essa paralisação não for registrada.

**[WM-02: Workflow e as quatro integrações do campo](31-WM-02-workflow-e-integracoes.md)**

1. Nomeie as quatro integrações do serviço de campo.
2. Qual das quatro é o motor?
3. O Dunning corta o cliente?
4. Quem executa o corte?
5. Uma nota de serviço pode ter mais de um workflow?
6. Um cliente pagou e foi cortado. Cite o mecanismo por trás.
7. O responsável da etapa travada é `WF BATCH`. Cite o que isso indica.
8. Alguém diz que registrou a solicitação e nada aconteceu. Cite o primeiro suspeito.

**[DM-01: Ativos, movimentação e estoque](32-DM-01-ativos-e-estoque.md)**

1. O que separa esta nota da `DM-02`?
2. Para que servem o TC e o TP?
3. Cite o erro caro associado ao TC e ao TP.
4. Descreva o ciclo de vida do equipamento.
5. Onde está o laço nesse ciclo?
6. Qual é a única saída definitiva de um equipamento do parque?
7. O técnico chegou em campo sem o medidor. Cite onde procurar a causa.
8. Cite o que faz do histórico completo a base de uma perícia.

**[DM-02: Leituras e registradores](33-DM-02-leituras-e-registradores.md)**

1. Nomeie os três eixos da leitura.
2. Que pergunta o eixo tipo responde?
3. Que pergunta o eixo motivo responde?
4. Que pergunta o eixo registrador responde?
5. Um cliente ligou e passou o número do medidor. Que tipo de leitura é essa?
6. Trocaram um medidor. Quantas leituras isso gera?
7. Cite o que acontece se faltar uma dessas leituras.
8. Uma instalação teve três leituras num mês. Isso é erro?
9. O que é energia injetada?
10. Uma instalação não faturou e o medidor está corretamente instalado. Cite a primeira hipótese.

**[DM-03: O cadastro do equipamento, do material ao medidor instalado](34-DM-03-cadastro-do-equipamento.md)**

1. Ordene, do primeiro ao último: Equipamento, Grupo de Registradores, Tipo de Equipamento, Material.
2. Qual transação cria o Grupo de Registradores?
3. Qual transação cria o Tipo de Equipamento?
4. Qual transação cria o Equipamento?
5. Qual transação cria o Grupo de Equipamentos?
6. Qual transação faz a instalação total?
7. Qual transação cria o material?
8. Como o SAP chama o objeto que substitui o Grupo de Registradores no caminho do transformador?
9. Um medidor foi criado no `IQ01` e não aparece na instalação. O que faltou?
10. O que o Grupo de Registradores decide?
11. O que separa Tipo de Equipamento de Equipamento?

**[DM-04: Planejamento de datas, quem carrega o calendário](35-DM-04-planejamento-de-datas.md)**

1. Qual objeto carrega a data de faturamento?
2. Qual objeto carrega a data de leitura?
3. Qual transação cria o Conjunto de Contratos?
4. Qual transação cria a Unidade de Leitura?
5. Qual transação atribui a Instalação ao planejamento?
6. Qual transação cadastra feriados e calendários?
7. Qual transação exibe as Unidades de Leitura?
8. Qual transação modifica a sequência de leitura?
9. Quais duas transações criam e atualizam o Registro de Datas?
10. Qual transação define o Grupo de Parâmetros?
11. Como a data da Unidade de Leitura é definida?
12. Duas casas na mesma rua estão em Unidades de Leitura diferentes. Isso é erro?
13. O que separa o Conjunto de Contratos da Unidade de Leitura?
14. Uma concessionária fatura três milhões de clientes. Cite a razão de existirem vários Conjuntos de Contratos.

**[DM-05: O ciclo da leitura, da ordem à validação](36-DM-05-ciclo-da-leitura.md)**

1. Qual transação cria a ordem de leitura, uma a uma?
2. Qual transação cria ordens de leitura em massa?
3. Qual transação baixa a ordem de leitura?
4. Qual transação sobe o resultado de leitura?
5. Qual transação faz entrada de leitura manual?
6. Qual transação trata a leitura?
7. Qual transação estima leitura, uma a uma?
8. Qual transação estima leitura em massa?
9. Qual transação monitora a leitura?
10. Qual transação estorna leitura?
11. Qual transação cria a relação entre registradores?
12. Quais duas etapas do ciclo acontecem fora da concessionária?
13. O que separa a ordem de leitura periódica da não periódica?
14. Nomeie os três tipos de validação de leitura.
15. O que distingue a validação dependente das independentes?
16. Uma leitura voltou do campo e o faturamento não rodou. Cite três causas possíveis.

**[PE-01: Gestão de Perdas, fraude e defeito](37-PE-01-fraude-e-defeito.md)**

1. Em uma frase, o que a Gestão de Perdas faz?
2. Quais dos seis gatilhos escalam para muitos casos de uma vez?
3. Cite o que torna esses gatilhos indispensáveis.
4. O que separa fraude de defeito?
5. O que não muda entre fraude e defeito?
6. O que é um by-pass?
7. O que é uma inversão de ligação?
8. Classificar defeito como fraude produz qual dano?
9. Classificar fraude como defeito produz qual dano?
10. Como um caso de Perdas nasce dentro de WM e de DM?

**[PE-02: Faturado da época x fatura revista](38-PE-02-faturado-da-epoca.md)**

1. Qual transação gerencia os processos de irregularidade e executa os cálculos?
2. O que o prefixo `ISUBR` indica sobre uma transação?
3. O que é faturado da época?
4. O que é fatura revista?
5. A fatura antiga é cancelada no processo de revisão?
6. Qual é o insumo mais disputado do cálculo?
7. Cite o que limita essa disputa.
8. Nomeie as três saídas da diferença apurada.
9. Cite o que a terceira saída revela sobre a calibragem da área.
10. O que precisa ser verdade sobre a memória de cálculo para a cobrança se sustentar?
11. Cite o motivo de o recálculo separar `TE` e `TUSD`.


---

## Cálculo e Faturamento (BILL)

**[BI-01: Cálculo e Faturamento, a distinção que define o módulo](39-BI-01-calculo-e-faturamento.md)**

1. Qual transação faz o cálculo individual?
2. Qual transação faz o cálculo em massa?
3. Qual transação faz o faturamento individual?
4. Qual transação faz o faturamento em massa?
5. Qual transação imprime, uma a uma?
6. Qual transação imprime em massa?
7. Qual transação trata anomalia, tanto de cálculo quanto de faturamento?
8. Qual tabela é a entrada do cálculo?
9. Qual tabela é a dobradiça entre cálculo e faturamento?
10. Qual tabela prova que o faturamento cria a dívida?
11. O que separa cálculo de faturamento quanto ao objeto sobre o qual agem?
12. Qual a entrada do faturamento?
13. Um cliente tem três contratos na mesma conta contrato. Quantos cálculos saem?
14. O mesmo cliente recebe quantas faturas?
15. Alguém diz "o faturamento não rodou". Cite a primeira pergunta a fazer.

**[BI-02: Os dados mestres de cálculo, como o sistema escolhe a tarifa](40-BI-02-dados-mestres-de-calculo.md)**

1. Qual transação define tipos de tarifa?
2. Qual tabela guarda as tarifas?
3. Qual tabela guarda a categoria de tarifa?
4. Qual tabela guarda a determinação de tarifa?
5. Qual tabela guarda os operandos?
6. Qual tabela guarda os tipos de tarifa?
7. Quais duas tabelas guardam o esquema de cálculo?
8. O que a instalação guarda, na faixa de tempo, a respeito de tarifa?
9. Quais são as duas entradas da determinação de tarifa?
10. O que a determinação de tarifa produz?
11. Como o SAP chama a variável que o cálculo usa e que o customizing define à parte?
12. Onde ficam armazenados os valores de operando válidos?
13. Um analista abre a instalação e não encontra a tarifa. Isso é erro?
14. Uma tarifa foi reajustada em março. Cite o que impede o recálculo de janeiro de usar o valor novo.
15. O que separa Tipo de Tarifa de Categoria de Tarifa?

**[BI-03: Anomalias, dois fluxos que parecem iguais e não são](41-BI-03-anomalias.md)**

1. Qual transação trata anomalia?
2. Qual tabela guarda a anomalia do cálculo?
3. Qual tabela guarda a anomalia da fatura?
4. Como o SAP chama a retenção de um documento que não passou na consistência?
5. O que a anomalia impede?
6. O que separa a liberação de anomalia de cálculo da de faturamento?
7. Que duas saídas o usuário tem diante de um documento retido?
8. Mil documentos entraram em anomalia. Cite o que impede resolver isso com um job.
9. Uma anomalia de faturamento foi liberada por engano. O que o sistema verifica depois?

**[BI-04: A impressão, do spool ao papel na casa do cliente](42-BI-04-impressao.md)**

1. Qual transação imprime, uma a uma?
2. Qual transação imprime em massa?
3. Como o SAP chama a saída para impressão de um documento?
4. Como o SAP chama o envio de um spool para um dispositivo específico?
5. Como o SAP chama o repositório onde os dados do spool ficam guardados?
6. Como o SAP chama a funcionalidade de construção de formulários de impressão?
7. O que separa spool de output request?
8. Como a fatura chega à empreiteira que imprime?
9. Uma transação do fluxo começa com `Z`. O que isso diz sobre ela?
10. Uma conta saiu com valor certo e um campo em branco. Cite onde está o defeito.

<!-- FIM PERGUNTAS -->

---

# GABARITO

> **Daqui para baixo são as respostas.** Só desça depois de ter tentado.

## GE-03
**GE-03: Do problema ao módulo**  ·  [voltar para a nota](01-GE-03-do-problema-ao-modulo.md)

1. **Onde** está ligado, **quanto** consumiu, **por quanto** é cobrado.
2. O consumo vem **antes** da autorização e antes do pagamento. Não há pedido,
   não há vendedor, e o produto é invisível.
3. Cortar quem pagou vira **processo judicial e multa do regulador**, e desfazer
   exige deslocar uma pessoa. Erro de faturamento se corrige com estorno.
4. **FI-CA**, arrecadação e cobrança.

---

## GE-01
**GE-01: O que é o SAP IS-U CCS**  ·  [voltar para a nota](02-GE-01-o-que-e-is-u-ccs.md)

1. **Customer Care Service.**
2. **Industry Solutions for Utilities.**
3. `CS + CRM` → `WM` → `DM` → `BILL` → `FI-CA`.
4. Como **faixa transversal**, por baixo das cinco.
5. **Não.** O BW enxerga tudo mas não é parte do CCS, e por isso não está entre
   as trilhas disponíveis.

---

## GE-02
**GE-02: A evolução do produto, do R/3 ao SaaS**  ·  [voltar para a nota](03-GE-02-evolucao-do-produto.md)

1. **Fim de 2027.**
2. Força a migração de toda a base instalada para o S/4HANA, e isso **gera
   projeto**, que é onde entra consultoria.
3. SAP GUI na era clássica, Fiori na moderna, Web e nativo em nuvem no SaaS.
4. Muda a **tecnologia** (HANA, tempo real) e a **interface**.
5. **Não muda o modelo de dados de negócio** nem os conceitos do CCS. É por
   isso que aprender IS-U hoje não vira conhecimento descartável.

---

## GE-04
**GE-04: Os quatro mercados, com peso igual**  ·  [voltar para a nota](04-GE-04-os-quatro-mercados.md)

1. **Luz, Água, Gás e Saneamento.**
2. **Não.** Mede volume em m³ e a cobrança é por energia. Há conversão no meio.
3. **Duas**, água e esgoto.
4. A de esgoto normalmente **não tem medidor** e fatura como percentual da água.
5. **Saneamento**, por medidor embaçado, enterrado ou inacessível.
6. **Saneamento**, por ser o mais sensível juridicamente. A régua de cobrança
   costuma ser mais conservadora.

---

## MD-01
**MD-01: As quatro divisões dos dados mestres**  ·  [voltar para a nota](05-MD-01-mapa-dos-dados-mestres.md)

1. Estrutura Postal, Dados Mestre Técnicos, Dados Mestre Comercial, Dados
   Transacionais.
2. Servir de **contraste**. Eles não são dado mestre, e é isso que define os
   outros três por oposição.
3. **Só o nome.** A aula lista a Estrutura Postal e nunca a desenvolve. O que a
   nota tem além disso veio do pôster de tabelas, não do slide.
4. A **WM**, que "mantém estruturas políticas e postais".
5. **Duração da validade.** Mestre dura muito e é a única versão válida no
   período. Transacional é dinâmico e vale pouco tempo.
6. Os **Dados Mestres Técnicos**: o prédio, o local de consumo e a instalação
   existem sem morador.
7. `ADRCITYMRU` e `ADRSTRTMRU`, unidade de leitura por cidade e por logradouro.
8. Que **sem estrutura postal não há roteirização**, sem roteirização não há
   leitura e sem leitura não há faturamento. Ela abre a lista porque tudo o mais
   depende dela. **A leitura é do autor, as tabelas é que são fonte.**
9. Na **estrutura postal**, em `ADRSTRTMRU`: o logradouro provavelmente não foi
   ligado a nenhuma unidade de leitura. Sem esse vínculo a rota não passa lá.

---

## MD-02
**MD-02: A tradução do prédio**  ·  [voltar para a nota](07-MD-02-a-traducao-do-predio.md)

1. **Objeto de Ligação.**
2. **Local de Consumo.**
3. **Local de Instalação de Equipamento.**
4. **Equipamento.**
5. **Parceiro de Negócios.**
6. O lugar onde se **consome** não é o lugar onde o aparelho está
   **instalado**. No prédio, consome-se no apartamento e mede-se na garagem.
7. O **Contrato**.

---

## MD-03
**MD-03: Parceiro de Negócios, categoria e função**  ·  [voltar para a nota](08-MD-03-parceiro-de-negocios.md)

1. `FPP1` ou `BP`.
2. `FPP2` ou `BP`.
3. `FPP3` ou `BP`.
4. **Pessoa, Organização e Grupo.**
5. **Grupo.** Normalmente não é utilizada.
6. **Parceiro de Contrato.**
7. **Categoria é o que o parceiro é** (pessoa física ou jurídica) e decide
   quais campos aparecem na tela. **Função é o papel que ele cumpre**, e o
   mesmo parceiro pode ter várias.
8. Que ele **não tem a função Parceiro de Contrato**, ou tem só função de
   Pessoa de Contato, que não carrega contrato.

---

## MD-04
**MD-04: Parceiro de Negócios, os dados e o customizing**  ·  [voltar para a nota](09-MD-04-parceiro-de-negocios-dados.md)

1. `BUC2`  ·  2. `BUC4`  ·  3. `BUC0`  ·  4. `SA13`  ·  5. `BUC8`
6. `BUC9`  ·  7. `BUS5`  ·  8. `BUB9`
9. **No PN.** Mas o direcionamento por função pode ser feito no nível da Conta
   Contrato.
10. No **endereço standard do PN**, e depois no endereço de correspondência da
    Conta Contrato, que é herdado do PN mas pode ser sobreposto.

---

## MD-05
**MD-05: Conta Contrato**  ·  [voltar para a nota](10-MD-05-conta-contrato.md)

1. `CAA1`  ·  2. `CAA2`  ·  3. `CAA3`  ·  4. `FPP2A`
5. **Mesmos dados de pagamento e cobrança.**
6. Do **Parceiro de Negócios**.
7. Na **Conta Contrato**.
8. No **Contrato**.

---

## MD-06
**MD-06: Contrato**  ·  [voltar para a nota](15-MD-06-contrato.md)

1. `ES21`  ·  2. `ES22`  ·  3. `ES27`  ·  4. `ES28`
5. Durante o **Move In**, ou em troca de titularidade e nova ligação.
6. **Não.** Um contrato liga a exatamente uma Conta Contrato e uma Instalação.
7. **No nível do Contrato.**
8. O **Move In**. O contrato é resultado de um processo, não de cadastro
   direto, e é por isso que não há transação de criar.

---

## MD-07
**MD-07: Move-In e Move-Out**  ·  [voltar para a nota](16-MD-07-move-in-move-out.md)

1. A **Instalação permanece**. Ela é do imóvel.
2. O **Contrato é encerrado**. Ele é da pessoa.
3. Uma **leitura inicial**.
4. **Ligação clandestina.** O sistema monitora imóveis desocupados justamente
   por isso.
5. Obriga a **desfazer e refazer todo o faturamento posterior à data**.

---

## ST-01
**ST-01: Objeto de Ligação**  ·  [voltar para a nota](11-ST-01-objeto-de-ligacao.md)

1. `ES55`  ·  2. `ES56`  ·  3. `ES57`
4. **Endereço.**
5. **O mais alto.**
6. **Dois.** Cada número predial é um Objeto de Ligação.

---

## ST-02
**ST-02: Local de Consumo**  ·  [voltar para a nota](12-ST-02-local-de-consumo.md)

1. `ES60`  ·  2. `ES61`  ·  3. `ES62`
4. **Não.** Ele assume o endereço do Objeto de Ligação e guarda só o
   complemento.
5. **Tipo do Local de Consumo** e **Complemento do endereço**.
6. **Um.**
7. **Quarenta.**
8. **Não.** `ES61` modifica e `ES62` exibe. Para criar, o correto é `ES60`.

---

## ST-03
**ST-03: Instalação**  ·  [voltar para a nota](13-ST-03-instalacao.md)

1. `ES30`  ·  2. `ES31`  ·  3. `ES32`
4. A **Instalação**, no bloco Faturamento e Medição.
5. A marcação de **tarifa social**, campo brasileiro.
6. Na **Instalação**, no bloco Informações Individuais.
7. Nos dados mestres da **Instalação**: tarifa, vigência da tarifa, unidade de
   leitura e tipo de validação.

---

## ST-04
**ST-04: Equipamento e Local de Instalação**  ·  [voltar para a nota](14-ST-04-equipamento.md)

1. `ES65`  ·  2. `ES66`  ·  3. `ES67`  ·  4. `EG31`  ·  5. `EG33`
6. `EG34`  ·  7. `EG51`
8. Normalmente **um**, com os 40 relógios juntos.
9. O **Transformador de Corrente (TC)**, e o de Potencial (TP).
10. Foi feita instalação **técnica** (`EG33`) sem a parte **com efeito no
    cálculo** (`EG34`). Faltou completar a instalação.

---

## CS-01
**CS-01: O que é CRM**  ·  [voltar para a nota](17-CS-01-o-que-e-crm.md)

1. **Não.** É **práticas + estratégias de negócio + tecnologias**. A tecnologia
   é a terceira camada, não a definição.
2. **Práticas, estratégias de negócio e tecnologias.**
3. Na **prospecção**.
4. Na **fidelização e retenção**. Ciclo inteiro, não só a venda.
5. **Conhecer.** Conhecer comportamento e necessidades para antecipar desejos.
   Vender é consequência.
6. **Custo e qualidade do atendimento.** Num monopólio o cliente insatisfeito
   não cancela, ele reclama, e reclamação tem preço com o regulador.

---

## CS-02
**CS-02: Ciclo de vida do cliente**  ·  [voltar para a nota](18-CS-02-ciclo-de-vida-do-cliente.md)

1. Prospecção, Qualificação, Conversão, Venda, Pós-venda, Fidelização.
2. **Prospecção e qualificação.**
3. **Conversão e venda.**
4. **Pós-venda e fidelização.**
5. **A fidelização realimenta a prospecção**: cliente fiel indica outro.
6. Na etapa 5, **pós-venda**.
7. Ele **não foi prospectado nem convertido**: mudou-se para um imóvel que já
   tinha ligação. Entrou por Move-In.

---

## CS-03
**CS-03: SAP CRM e os três pilares**  ·  [voltar para a nota](19-CS-03-sap-crm-e-os-pilares.md)

1. **Marketing, Vendas (Sales) e Serviço (Service).**
2. **Serviço.**
3. **Pilar é área de negócio**, linha da matriz. **Faixa vertical é canal**, e
   atravessa os três pilares.
4. **Web Channel, Interaction Center e Partner Channel Management.**
5. Campaign Management.
6. Opportunity Management.
7. Customer Service & Support.
8. **S/4 Customer Engagement**, versão simplificada do SAP CRM embutida no
   S/4HANA.
9. O **S/4HANA Interaction Center**, aproveitando a tecnologia do CRM Web UI.

---

## CS-04
**CS-04: CRM no contexto Utilities**  ·  [voltar para a nota](20-CS-04-crm-no-contexto-utilities.md)

1. **Não.**
2. **Camada.** O material diz camada de atendimento **integrada** ao IS-U/CCS:
   um sistema por cima, não um módulo dentro.
3. **A primeira.**
4. `CS + CRM` → `WM` → `DM` → `BILL` → `FI-CA`.
5. No **CS + CRM**, que oferece os serviços ao cliente (*new connection*,
   *reconnection*).
6. **Não.**
7. Como **faixa única atravessando as cinco**, não como caixa na fila. É camada
   de informação sobre todas.
8. **Não.** Pode existir mais de um CRM na paisagem: Salesforce na ponta e SAP
   CRM no meio é arranjo comum.

---

## CS-05
**CS-05: Processos e atividades**  ·  [voltar para a nota](21-CS-05-processos-e-atividades.md)

1. `BUT000`.
2. **Protocolo é o número que o cliente recebe e acompanha. Atividade é o
   registro do que foi feito.**
3. **O protocolo contém as atividades.**
4. Ele **prova prazo de atendimento perante o regulador**.
5. Ligação Nova, Alteração de titularidade, Segundas Vias, Reclamações,
   Cadastro, Modificações Contratuais.
6. Ao processo que **cria o Contrato**: o material diz que ele "é criado quando
   ocorre uma nova ligação ou troca de titularidade". Se é literalmente
   Move-Out mais Move-In, **está em aberto**.
7. No campo **Status**, com valores Cliente, **Prospect** e Inativo.

---

## AR-01
**AR-01: O landscape e as cinco camadas**  ·  [voltar para a nota](26-AR-01-landscape-e-camadas.md)

1. **Back end.** O CRM fica no meio, o IS-U atrás dele.
2. Canais → Camada CRM → Middleware → Camada IS-U/CCS → Integrações externas.
3. No quadrante **Analyses**, junto do back end.
4. Que ele é **camada de dados, não área funcional**.
5. O **WebClient**.
6. O **Call Center**.
7. Que são **sistemas distintos**. Middleware só existe entre sistemas
   separados; se fossem o mesmo, com a mesma base, replicar não faria sentido.

---

## AR-02
**AR-02: Middleware e replicação**  ·  [voltar para a nota](27-AR-02-middleware-e-replicacao.md)

1. `SMW01`  ·  2. `SMQ1`  ·  3. `SMQ2`  ·  4. `SM58`  ·  5. `SM21`  ·  6. `ST22`
7. `R3AS`  ·  8. `R3AR2`
9. **Business Document**, o envelope do dado.
10. **queued Remote Function Call**, a fila que garante a ordem.
11. `CRM cria BP` → `SMW01` BDoc → `SMQ1` fila qRFC → RFC → IS-U recebe →
    `BUT000` criado.
12. **Carga inicial traz tudo na implantação** (`R3AS`). **Fluxo do dia replica
    o que muda**, um objeto de cada vez.
13. `SMW01` o BDoc saiu? → `SMQ1` e `SMQ2` parou na fila? → `SM58` a conexão
    caiu? → `ST22` deu dump no destino?

---

## AR-03
**AR-03: Objetos replicados**  ·  [voltar para a nota](28-AR-03-objetos-replicados.md)

1. `BUT000`  ·  2. `BUT000`, o mesmo  ·  3. `FKKVKP`  ·  4. `CRMM_BUAG`
5. `EHAUISU`  ·  6. Em **`COMM_PRODUCT`**, um produto contratado  ·  7. `EUIHEAD`
8. **Installed Base**, a base instalada: o que o cliente tem instalado.
9. O **Parceiro de Negócios**. É objeto central compartilhado do SAP, e o
   primeiro a replicar.
10. Da **Conta Contrato**. `CRMM_BUAG` é o nome dela no CRM.
11. Do **slide de replicação da Aula 02**, reconferidos no pôster de tabelas
    IS-U. Não são dedução nem memória.

---

## MD-08
**MD-08: Os dois mundos e a validade no tempo**  ·  [voltar para a nota](06-MD-08-os-dois-mundos.md)

1. No **Contrato indo para a Instalação**. É a única ligação entre os dois
   lados; todo o resto desce dentro do próprio mundo.
2. O **Objeto de Ligação**.
3. O desenho lista do **mais específico para o mais genérico**, e a hierarquia
   física vai do **prédio para o medidor**. São ordens inversas.
4. **Parceiro de Negócios** (período de validade), **Contrato** (vigência) e
   **Instalação** (vigência do tipo de tarifa).
5. Você pode ter **alterado o passado**: se a nova tarifa valer desde uma data
   antiga, o sistema vai querer refaturar meses já fechados.

---

## SV-01
**SV-01: Serviço de Campo (SVC) e os três blocos**  ·  [voltar para a nota](29-SV-01-servico-de-campo.md)

1. **WM / SVC**, **DM / GAT** e **Perdas**.
2. Manda gente para a rua.
3. Cuida do que fica pendurado na parede.
4. Descobre que o número estava errado e cobra a diferença.
5. Ela designa **os dois níveis**: é o nome do guarda-chuva, a área inteira, e
   também o apelido do Bloco 1.
6. É o que acontece quando WM e DM, **juntos**, descobrem que a medição não
   representava a realidade. A fiscalização é nota (WM), o medidor adulterado é
   ativo (DM), mas **o recálculo não é de nenhum dos dois**.
7. **Não.** Ela responde por onde o dado passa; os três blocos respondem quem
   senta junto.
8. **A cadeia é sequencial e responde por onde o dado passa. Os três blocos são
   paralelos e respondem quem senta junto.**
9. A **Ordem**. A etapa 5 diz "recebe a ordem" e o objeto nunca foi apresentado.

---

## WM-01
**WM-01: A nota de serviço e o ciclo do campo**  ·  [voltar para a nota](30-WM-01-nota-de-servico.md)

1. **Tipo de processo, motivo, prioridade e prazo.**
2. **Que trabalho é.**
3. **O relógio regulatório.**
4. Corte, religação, fiscalização, modificação, inspeção, ligação nova,
   substituição de medidor.
5. **O prazo regulatório estourado.** É infração com valor, não atraso
   administrativo.
6. **Parar o relógio** quando a culpa não é da concessionária.
7. A nota de **fiscalização**.
8. O **evento de paralisação** e a **suspensão** do prazo.
9. O relógio **continua correndo** e vira transgressão que não existiu.

---

## WM-02
**WM-02: Workflow e as quatro integrações do campo**  ·  [voltar para a nota](31-WM-02-workflow-e-integracoes.md)

1. **CRM, Dunning, Billing/FI-CA e Workflow.**
2. O **Workflow**. Os outros três são portas.
3. **Não.** Dunning decide e manda.
4. O **WM**, por nota de serviço.
5. **Sim.** O caso real desta nota tinha quatro workflows na mesma nota.
6. **Descompasso de relógios.** A régua rodou no ciclo dela, o pagamento entrou
   pelo ciclo do banco depois, e a nota de corte já tinha saído.
7. Que rodou **automático, em job**, sem pessoa envolvida. Se travou, ninguém
   percebeu até alguém reclamar.
8. **O workflow travado, não a nota.**

---

## DM-01
**DM-01: Ativos, movimentação e estoque**  ·  [voltar para a nota](32-DM-01-ativos-e-estoque.md)

1. Aqui é o **aparelho como bem patrimonial**; na `DM-02`, **o número que ele
   produz**.
2. Reduzem o sinal de cliente grande a uma escala que o medidor aguenta, e o
   sistema multiplica de volta por uma **constante**.
3. **Constante errada faz a conta errar por um fator**, não por um pouco.
4. Recebimento em estoque → transferência → instalação em campo → retirada →
   manutenção → volta ao estoque.
5. Na **manutenção**: o mesmo número de série é instalado de novo, em outro
   imóvel.
6. O **sucateamento**.
7. No **estoque**: reserva não feita ou não respeitada.
8. Ele prova **onde aquele aparelho esteve e por quanto tempo**, que é o que
   sustenta o recálculo de um período.

---

## DM-02
**DM-02: Leituras e registradores**  ·  [voltar para a nota](33-DM-02-leituras-e-registradores.md)

1. **Tipo, motivo e registrador.**
2. **Como o número foi obtido.**
3. **Por que foram ler.**
4. **O que foi medido.**
5. **Leitura informada.**
6. **Três**: de retirada (o velho), de instalação (o novo) e de troca (amarra o
   par).
7. O **consumo do mês fica sem dono**.
8. **Não.** Três dos cinco motivos são disparados por evento, não pelo ciclo.
9. O registrador de quem **gera** energia e manda o excedente para a rede.
   Existe porque o cliente virou gerador.
10. **Falta a relação registrador e tarifa.** Instalado tecnicamente, não
    instalado para faturamento.

---

## PE-01
**PE-01: Gestão de Perdas, fraude e defeito**  ·  [voltar para a nota](37-PE-01-fraude-e-defeito.md)

1. Descobre que o medidor não contava a verdade, **calcula quanto deveria ter
   sido cobrado** e cobra a diferença.
2. **Consumo atípico, análises estatísticas e monitoramento de indicadores.**
3. Fiscalizar milhões de imóveis a pé é inviável. Achar por padrão e mandar
   técnico só onde vale a pena é o que torna a área possível.
4. **Fraude é ação intencional. Defeito é falha técnica.**
5. As duas produzem **consumo medido menor que o real**.
6. Uma **ponte que contorna o medidor**.
7. A **troca de posição dos cabos**, que faz o medidor girar ao contrário ou
   registrar menos.
8. **Acusa de crime um cliente inocente.**
9. **Entrega dinheiro e não aplica sanção.**
10. Em **WM** como nota de fiscalização, e em **DM** como ativo adulterado. O
    recálculo, que é o produto, não é de nenhum dos dois.

---

## PE-02
**PE-02: Faturado da época x fatura revista**  ·  [voltar para a nota](38-PE-02-faturado-da-epoca.md)

1. `ISUBR_MANAGE_PROCESS`.
2. **Localização Brasil.** Os critérios regulatórios de recálculo são
   nacionais, e o SAP entrega a versão brasileira pronta.
3. O que o cliente **pagou** com o medidor errado.
4. O que ele **deveria ter pago**.
5. **Não.** Ela continua existindo, e a revisão é documento novo ao lado dela.
   O histórico precisa mostrar as duas versões.
6. O **período da irregularidade**.
7. Os **critérios regulatórios**, que limitam até onde se pode voltar no tempo.
8. **Receita recuperada, débito adicional e crédito ao cliente.**
9. Que defeito pode fazer o aparelho contar **a mais**. Uma área que só produz
   débito está calibrada errado.
10. Ela precisa mostrar **fórmulas, consumos considerados, períodos e
    memória do cálculo**, de forma que um terceiro refaça a conta.
11. Porque são **parcelas com alíquotas e destinos diferentes**, e o imposto
    entra separado por alíquota.

---

## DM-03
**DM-03: O cadastro do equipamento**  ·  [voltar para a nota](34-DM-03-cadastro-do-equipamento.md)

1. Material, Grupo de Registradores, Tipo de Equipamento, Equipamento.
2. `EG04`  ·  3. `EG01`  ·  4. `IQ01`  ·  5. `EG27`  ·  6. `EG31`  ·  7. `MM01`
8. **Grupo de Enrolamento**, transação `EGW1`.
9. **A instalação.** `IQ01` só cria o aparelho no cadastro; quem o coloca na
   instalação é `EG31`.
10. Quantos e quais registradores o tipo de equipamento terá.
11. **Tipo é o modelo, equipamento é o aparelho.** O tipo vale para todos os
    aparelhos daquele modelo; o equipamento tem número de série.

---

## DM-04
**DM-04: Planejamento de datas**  ·  [voltar para a nota](35-DM-04-planejamento-de-datas.md)

1. O **Conjunto de Contratos**.
2. A **Unidade de Leitura**.
3. `E41B`  ·  4. `E41H`  ·  5. `ES31` ou `EL59`  ·  6. `SCAL`  ·  7. `EL42`
8. `EL40`  ·  9. `E1DY` e `E2DY`  ·  10. `EL59P`
11. **Relativa à data do conjunto**, no material "2 dias antes do cálculo".
12. **Não.** A Unidade de Leitura é a rota do leiturista, e o corte é físico.
13. **O conjunto responde quando o dinheiro acontece, a unidade responde quando
    o técnico anda.**
14. **Distribuir a carga ao longo do mês.** Faturar a base inteira no mesmo dia
    não cabe em nenhuma janela de processamento.

---

## DM-05
**DM-05: O ciclo da leitura**  ·  [voltar para a nota](36-DM-05-ciclo-da-leitura.md)

1. `EL01`  ·  2. `EL09`  ·  3. `EL16`  ·  4. `ELMU`  ·  5. `EL28`  ·  6. `EL27`
7. `EL30`  ·  8. `EL18`  ·  9. `EL31`  ·  10. `EL37`  ·  11. `EG75`
12. A **leitura em campo** e a **coleta do resultado**. Quem lê é a empreiteira.
13. **Periódica** nasce do calendário de leitura. **Não periódica** nasce de
    outro processo do SAP: mudança, troca de medidor, fiscalização.
14. Independente fixa, independente variável e dependente.
15. **A dependente olha o resultado de outro registrador**, e por isso exige
    relação entre registradores.
16. Não existe ordem de leitura · o resultado não voltou do campo · a leitura
    está retida em validação esperando tratamento.

---

## BI-01
**BI-01: Cálculo e Faturamento**  ·  [voltar para a nota](39-BI-01-calculo-e-faturamento.md)

1. `EA00`  ·  2. `EA38`  ·  3. `EA19`  ·  4. `EA26`  ·  5. `EA40`  ·  6. `EA29`
7. `EA05`, a mesma para os dois tipos de anomalia.
8. `ETRG`, as ordens de cálculo.
9. `EITR`: saída do cálculo, entrada do faturamento.
10. `DFKKOP`, a partida em aberto de FI-CA, que só aparece na saída do
    faturamento.
11. **Cálculo age sobre o Contrato, faturamento sobre a Conta Contrato.**
12. O **documento de cálculo liberado**.
13. **Três.** Um por contrato.
14. **Uma.** É para isso que a Conta Contrato agrupa.
15. **"Saiu documento de cálculo?"** Se saiu, o problema é depois; se não, antes.

---

## BI-02
**BI-02: Os dados mestres de cálculo**  ·  [voltar para a nota](40-BI-02-dados-mestres-de-calculo.md)

1. `EA56`  ·  2. `ETRF`  ·  3. `ETTA`  ·  4. `ERTFND`  ·  5. `TE221`  ·  6. `TE069`
7. `ESCH` (cabeçalho) e `ESCHS` (etapas).
8. A **categoria de tarifa**.
9. A **categoria de tarifa** (da instalação) e o **tipo de tarifa** (do
   registrador ou do operando).
10. **Quais tarifas entram no cálculo.**
11. **Operando.**
12. Na **categoria de tarifa**, válidos para todo o grupo de clientes.
13. **Não.** A tarifa não mora na instalação, é resultado de determinação.
14. **A faixa de tempo.** O reajuste cria faixa nova e a antiga permanece, então
    o recálculo de janeiro acha a regra de janeiro.
15. **Tipo é o que o registrador ou o operando carrega. Categoria é o que a
    instalação carrega.** O cruzamento dos dois é que determina a tarifa.

---

## BI-03
**BI-03: Anomalias**  ·  [voltar para a nota](41-BI-03-anomalias.md)

1. `EA05`  ·  2. `ERCHO`  ·  3. `ERDO`
4. **Anomalia.**
5. **A emissão de conta errada.**
6. No cálculo, **desmarca e mantém o mesmo documento**. No faturamento, **cria
   um documento novo**, e depois disso não há nova verificação.
7. **Cancelar** o documento retido ou **liberá-lo**.
8. **Não existe ferramenta de liberação em massa.** O tratamento é individual,
   por decisão de produto.
9. **Nada.** Não há nova verificação de anomalia depois da liberação.

---

## BI-04
**BI-04: A impressão**  ·  [voltar para a nota](42-BI-04-impressao.md)

1. `EA40`  ·  2. `EA29`
3. **Spool.**  ·  4. **Output request.**  ·  5. **TemSe.**  ·  6. **SAPscript.**
7. **Spool é o conteúdo, output request é o envio.** Um spool pode gerar vários
   envios.
8. Por **arquivo TXT gerado por transação `Z`**, ou seja, código do projeto.
9. Que **é desenvolvimento do projeto**, não transação standard SAP.
10. **No formulário.** Se o valor está certo, o cálculo está certo.

---

## CS-06
**CS-06: A esteira do chamado, do protocolo ao fechamento**  ·  [voltar para a nota](22-CS-06-a-esteira-do-chamado.md)

1. O **Contrato**, criado no Move-In.
2. **Penúltimo.** Só depois de a estrutura física estar pronta.
3. Por **BILL**. Segunda via é reemissão do documento de impressão.
4. **DM** (leitura), **BILL** (cálculo) e **PE**, se houver irregularidade.
5. **Dunning decide e manda. Quem corta é o WM.**
6. Protocolo → nota de serviço → instalação do equipamento → Contrato.
7. Um **segundo chamado**, agora de reclamação de prazo, e esse tem peso com o
   regulador. O protocolo abre em segundos; a esteira leva semanas.
8. **FI-CA.** A religação depende da baixa do pagamento, não do comprovante.

---

## CS-07
**CS-07: Reclamação de conta alta, o roteiro de diagnóstico**  ·  [voltar para a nota](23-CS-07-reclamacao-de-conta-alta.md)

1. Leitura · anomalia liberada · tarifa errada · instalação incompleta ·
   irregularidade.
2. **Do mais barato de verificar para o mais caro.**
3. Na **irregularidade**. É a única em que reclamar sai mais caro que ficar
   calado, e por isso a classificação entre fraude e defeito é tão delicada.
4. `EG33` sem `EG34`: instalação técnica feita, sem a parte com efeito no
   cálculo.
5. Na **DM**, no ciclo da leitura: o resultado voltou do campo, passou na
   validação, ou foi estimativa?
6. **Tarifa errada corrige cadastro e refatura.** Irregularidade **cobra a
   mais**, com memória de cálculo, e quem executa é `PE`.
7. **Deslocamento de equipe** para descobrir algo que estava na tela. Se a causa
   era leitura estimada, gastou-se uma visita à toa.
8. **Leitura** ou **instalação incompleta.** Salto isolado em histórico estável
   não é consumo real nem irregularidade antiga.

---

## CS-08
**CS-08: Corte e religação, o descompasso que gera chamado**  ·  [voltar para a nota](24-CS-08-corte-e-religacao.md)

1. **Dunning.**
2. **WM.**
3. **FI-CA.**
4. Na **Conta Contrato**, não no Contrato.
5. Pagamento baixado? · bloqueio de corte? · a nota virou ordem executada? ·
   workflow travado?
6. A **religação tem prazo regulatório** e curto. O corte segue o prazo da
   régua.
7. **Descompasso de ciclos.** A régua roda no ciclo dela, o pagamento entra no
   ciclo do banco, e a nota de corte já saiu. Cada elo funcionou.
8. Que o **pagamento entrou no sistema**. Ele prova que o cliente pagou, e a
   religação depende da baixa em FI-CA.

---

## CS-09
**CS-09: O que o atendente vê, e onde mora o resto**  ·  [voltar para a nota](25-CS-09-o-que-o-atendente-ve.md)

1. Parceiro de Negócio · Conta Contrato · Objeto de Ligação · Ponto de Entrega.
2. O **Parceiro de Negócios**, `BUT000` dos dois lados.
3. `CRMM_BUAG`, de *Business Agreement*.
4. Em **produto contratado**, `COMM_PRODUCT`. A estrutura física fica no IS-U.
5. **Não.** O Contrato não está entre os quatro replicados.
6. No **IS-U**. Leitura não replica.
7. No **IS-U**. A partida em aberto é de FI-CA.
8. Que o **dado não existe**, e daí sai chamado de cadastro para um dado que
   está correto do outro lado.
9. Na **replicação**, não no cadastro. O caminho é a fila do middleware.
