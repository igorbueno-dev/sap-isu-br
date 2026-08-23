# SAP IS-U CCS

Notas de estudo sobre **SAP IS-U CCS** (*Industry Solutions for Utilities /
Customer Care Service*), a solução setorial que roda o ciclo comercial de
concessionárias de energia, água e gás.

Material estruturado de IS-U é escasso, e o pouco que existe raramente sai do
inglês. Isto aqui é uma tentativa de mudar isso, em aberto, com correção de
quem conhece o módulo na prática.

| Tempo | Onde ir |
|---|---|
| **4 min** | A tabela abaixo, de cima para baixo. É o acervo inteiro resumido |
| **6 min** | [`MD‑02`](notas/07-MD-02-a-traducao-do-predio.md), que traduz um prédio de verdade nos objetos do sistema |
| **1 sessão** | [`_PISTAS.md`](notas/_PISTAS.md), as 382 perguntas em voz alta. O gabarito fica no fim do mesmo arquivo |
| **4 horas** | As 43 notas, na ordem da pasta |
| **Consulta** | [`02-BANCADA.md`](referencia/02-BANCADA.md), transações e tabelas. Use `Ctrl+F` |
| **Contribuir** | [`_projeto/`](_projeto/), o que falta e como escrever uma nota |

---

# As 43 notas

**O número no arquivo é a ordem de estudo.** Abra [`notas/`](notas/) e leia de
cima para baixo: nenhuma nota depende de uma que venha depois dela.

<!-- INICIO NOTAS -->

### Fundação

Valem para qualquer trilha. **A ordem é a ordem**: cada uma usa a anterior.

| # | Nota | O que é | Origem |
|---|---|---|---|
| **01** | [`GE-03` Do problema ao módulo](notas/01-GE-03-do-problema-ao-modulo.md) | Cinco parágrafos de negócio, e o mapa de qual pedaço do CCS resolve cada um. Leia antes de qualquer sigla: é o "por quê" de todas elas. | meu |
| **02** | [`GE-01` O que é o SAP IS-U CCS](notas/02-GE-01-o-que-e-is-u-ccs.md) | O conjunto de módulos que roda o ciclo comercial de uma concessionária, do cadastro do cliente até o dinheiro entrar. | slide |
| **03** | [`GE-02` A evolução do produto, do R/3 ao SaaS](notas/03-GE-02-evolucao-do-produto.md) | Trinta e cinco anos em cinco marcos, e por que 2027 é a data que move o mercado inteiro. | slide |
| **04** | [`GE-04` Os quatro mercados, com peso igual](notas/04-GE-04-os-quatro-mercados.md) | Luz, água, gás e saneamento rodam o mesmo núcleo. A diferença aparece em pontos específicos, e um exercício pode vir de qualquer um deles. | misto |
| **05** | [`MD-01` As quatro divisões dos dados mestres](notas/05-MD-01-mapa-dos-dados-mestres.md) | Antes de comparar qualquer coisa, saber o que é cada uma. São quatro divisões, não duas, e a quarta não é dado mestre. | slide |
| **06** | [`MD-08` Os dois mundos e a validade no tempo](notas/06-MD-08-os-dois-mundos.md) | O desenho que arruma comercial e técnico lado a lado, a ponte entre eles, e a armadilha de achar que a ordem do desenho é a hierarquia. | slide |
| **07** | [`MD-02` A tradução do prédio](notas/07-MD-02-a-traducao-do-predio.md) | O diagrama que converte o mundo real inteiro em vocabulário SAP, de uma vez. | slide |
| **08** | [`MD-03` Parceiro de Negócios, categoria e função](notas/08-MD-03-parceiro-de-negocios.md) | Quem é a pessoa, e qual papel ela cumpre. São duas perguntas diferentes, e o SAP guarda as duas em campos diferentes. | slide |
| **09** | [`MD-04` Parceiro de Negócios, os dados e o customizing](notas/09-MD-04-parceiro-de-negocios-dados.md) | O que cabe dentro da ficha do cliente, e onde se desenha a ficha. | slide |
| **10** | [`MD-05` Conta Contrato](notas/10-MD-05-conta-contrato.md) | A bolsa financeira do cliente. Reúne débitos e créditos, e é onde moram as regras de pagamento e de cobrança. | slide |
| **11** | [`ST-01` Objeto de Ligação](notas/11-ST-01-objeto-de-ligacao.md) | A edificação conectada à rede. O nível mais alto dos dados mestres técnicos, e onde mora o endereço. | slide |
| **12** | [`ST-02` Local de Consumo](notas/12-ST-02-local-de-consumo.md) | A unidade que recebe energia e é medida separadamente. O apartamento dentro do prédio. | slide |
| **13** | [`ST-03` Instalação](notas/13-ST-03-instalacao.md) | O objeto que efetivamente fatura. É aqui que moram a tarifa, a unidade de leitura e as regras de cálculo. | slide |
| **14** | [`ST-04` Equipamento e Local de Instalação](notas/14-ST-04-equipamento.md) | O aparelho físico e o lugar onde ele está parafusado. E as três formas de instalar, que explicam um chamado clássico. | misto |
| **15** | [`MD-06` Contrato](notas/15-MD-06-contrato.md) | A dobradiça do sistema. É o único objeto que toca o mundo comercial e o mundo técnico ao mesmo tempo. | slide |
| **16** | [`MD-07` Move-In e Move-Out](notas/16-MD-07-move-in-move-out.md) | O processo que cria e encerra o Contrato. | meu |

### Atendimento e relacionamento (CRM)

As quatro últimas cruzam o CRM com as outras áreas. **Elas são o motivo
de nada ser colapsado**: quem atende decide para onde o chamado vai.

| # | Nota | O que é | Origem |
|---|---|---|---|
| **17** | [`CS-01` O que é CRM](notas/17-CS-01-o-que-e-crm.md) | A disciplina antes do produto. CRM é um jeito de organizar o relacionamento com o cliente, e só depois um sistema da SAP. | slide |
| **18** | [`CS-02` Ciclo de vida do cliente](notas/18-CS-02-ciclo-de-vida-do-cliente.md) | Seis etapas de um lado, três pilares do outro. São a mesma coisa vista de perto e de longe, e vale enxergar as duas juntas. | slide |
| **19** | [`CS-03` SAP CRM e os três pilares](notas/19-CS-03-sap-crm-e-os-pilares.md) | O produto. Marketing, Vendas e Serviço, cada um com sua fileira de módulos. E o nome novo que a SAP deu a tudo isso dentro do S/4HANA. | slide |
| **20** | [`CS-04` CRM no contexto Utilities](notas/20-CS-04-crm-no-contexto-utilities.md) | Onde exatamente o CRM se encaixa na cadeia que você já conhece. Ele é a primeira área, a porta por onde tudo entra. | slide |
| **21** | [`CS-05` Processos e atividades no atendimento](notas/21-CS-05-processos-e-atividades.md) | O que o atendente realmente faz o dia inteiro. Protocolo, atividade e a lista de processos que respondem por quase todo o volume de um call center de concessionária. | slide |
| **22** | [`CS-06` A esteira do chamado, do protocolo ao fechamento](notas/22-CS-06-a-esteira-do-chamado.md) | Todo processo do CRM termina em outra área. O atendimento abre o protocolo e quem fecha é campo, medição, faturamento ou cobrança. | misto |
| **23** | [`CS-07` Reclamação de conta alta, o roteiro de diagnóstico](notas/23-CS-07-reclamacao-de-conta-alta.md) | O chamado mais comum da concessionária atravessa três áreas, e o atendimento decide qual delas investiga primeiro. | misto |
| **24** | [`CS-08` Corte e religação, o descompasso que gera chamado](notas/24-CS-08-corte-e-religacao.md) | Dunning decide, WM executa, FI-CA confirma o pagamento. São três relógios diferentes, e o cliente cortado depois de pagar mora entre eles. | misto |
| **25** | [`CS-09` O que o atendente vê, e onde mora o resto](notas/25-CS-09-o-que-o-atendente-ve.md) | O CRM não guarda a maior parte do que o cliente pergunta. Ele guarda uma cópia de alguns objetos, e o resto vive no IS-U. | misto |

### Arquitetura e integração

| # | Nota | O que é | Origem |
|---|---|---|---|
| **26** | [`AR-01` O landscape e as cinco camadas](notas/26-AR-01-landscape-e-camadas.md) | Dois desenhos da mesma coisa. Um simples, para entender; um detalhado, para se localizar. Comece pelo simples. | slide |
| **27** | [`AR-02` Middleware e replicação](notas/27-AR-02-middleware-e-replicacao.md) | Como um dado criado no CRM aparece no IS-U. Um caminho de cinco paradas, e as transações para olhar cada uma quando ele trava. | slide |
| **28** | [`AR-03` Objetos replicados](notas/28-AR-03-objetos-replicados.md) | Quatro objetos existem dos dois lados com nomes e tabelas diferentes. Este de-para é o que você consulta quando alguém diz "o dado está divergente". | slide |

### Serviço de Campo e Equipamento (SVC / DM)

| # | Nota | O que é | Origem |
|---|---|---|---|
| **29** | [`SV-01` Serviço de Campo (SVC) e os três blocos](notas/29-SV-01-servico-de-campo.md) | A área tem quatro nomes circulando e três blocos por dentro. Acertar o vocabulário aqui evita meia hora de conversa errada numa reunião. | misto |
| **30** | [`WM-01` A nota de serviço e o ciclo do campo](notas/30-WM-01-nota-de-servico.md) | Tudo que o campo faz começa numa nota de serviço. Ela carrega tipo, motivo, prioridade e prazo, e é o prazo que dá multa. | misto |
| **31** | [`WM-02` Workflow e as quatro integrações do campo](notas/31-WM-02-workflow-e-integracoes.md) | O campo quase nunca decide sozinho o que fazer. O pedido chega de fora e anda sozinho por dentro. Este é o mapa de quem manda e de quem executa. | misto |
| **32** | [`DM-01` Ativos, movimentação e estoque](notas/32-DM-01-ativos-e-estoque.md) | O medidor tem uma vida inteira antes e depois de estar na parede. Device Management é quem sabe onde cada um está, e onde esteve. | misto |
| **33** | [`DM-02` Leituras e registradores](notas/33-DM-02-leituras-e-registradores.md) | Seis tipos de leitura, cinco motivos e seis registradores. Parece lista de decorar, e não é: cada eixo responde uma pergunta diferente da investigação. | misto |
| **34** | [`DM-03` O cadastro do equipamento, do material ao medidor instalado](notas/34-DM-03-cadastro-do-equipamento.md) | Um medidor não nasce medidor. Ele nasce material, ganha um tipo, vira equipamento, e só então pode ser instalado. | slide |
| **35** | [`DM-04` Planejamento de datas, quem carrega o calendário](notas/35-DM-04-planejamento-de-datas.md) | O cliente não escolhe quando é faturado. Quem carrega a data é o Conjunto de Contratos, e quem carrega a rota é a Unidade de Leitura. | slide |
| **36** | [`DM-05` O ciclo da leitura, da ordem à validação](notas/36-DM-05-ciclo-da-leitura.md) | A leitura sai do SAP como ordem, atravessa a fronteira para a empreiteira, volta como resultado e só depois é validada. Quem lê não é a concessionária. | slide |
| **37** | [`PE-01` Gestão de Perdas, fraude e defeito](notas/37-PE-01-fraude-e-defeito.md) | A mesma consequência, dois mundos jurídicos diferentes. Classificar errado aqui é o erro que vira processo. | misto |
| **38** | [`PE-02` Faturado da época x fatura revista](notas/38-PE-02-faturado-da-epoca.md) | O cálculo que transforma uma irregularidade em valor a cobrar. Duas contas do mesmo período, e a diferença entre elas é a receita recuperada. | misto |

### Cálculo e Faturamento (BILL)

| # | Nota | O que é | Origem |
|---|---|---|---|
| **39** | [`BI-01` Cálculo e Faturamento, a distinção que define o módulo](notas/39-BI-01-calculo-e-faturamento.md) | Cálculo apura quanto. Faturamento acrescenta imposto, emite a conta e **cria a dívida**. São dois processos, dois documentos e dois objetos diferentes. | slide |
| **40** | [`BI-02` Os dados mestres de cálculo, como o sistema escolhe a tarifa](notas/40-BI-02-dados-mestres-de-calculo.md) | A instalação não guarda a tarifa. Ela guarda uma **categoria**, e a tarifa é **determinada** pelo cruzamento dessa categoria com o tipo que cada registrador carrega. | slide |
| **41** | [`BI-03` Anomalias, dois fluxos que parecem iguais e não são](notas/41-BI-03-anomalias.md) | Anomalia é a trava que impede conta errada de sair. No cálculo ela só marca o documento; no faturamento ela **cria um documento novo**. | slide |
| **42** | [`BI-04` A impressão, do spool ao papel na casa do cliente](notas/42-BI-04-impressao.md) | A fatura sai do SAP como spool, vira formulário no SAPscript e atravessa para a empreiteira como arquivo. Imprimir também é fora de casa. | slide |
| **43** | [`BI-05` O que precisa existir para faturar, e o que fazer quando não faturou](notas/43-BI-05-o-que-precisa-para-faturar.md) | Oito coisas precisam estar no lugar para uma instalação faturar. O diagnóstico da fatura que não saiu é essa mesma lista, percorrida de trás para frente. | misto |
<!-- FIM NOTAS -->

Cerca de **258 minutos** no total. A coluna *O que é* é o resumo da própria
nota, gerado a partir dela, então nunca diverge.

---

# Por que esta ordem

A numeração é linear, o modelo não é. Os dois ramos descem em paralelo e se
encontram num ponto só:

```
COMERCIAL, quem paga        TÉCNICO, onde se consome
08 Parceiro de Negócios     11 Objeto de Ligação
09 PN, dados                12 Local de Consumo
10 Conta Contrato           13 Instalação
                            14 Equipamento
        └───────── 15 CONTRATO ─────────┘
                   16 Move-In, o processo que o cria
```

**O Contrato é o único conceito que exige os dois ramos completos**, e por isso
é a nota 15, não a sexta dos dados mestres comerciais. É onde o entendimento se
prova: se você o entende de verdade, entende os dados mestres inteiros. Se não,
o problema está em algum nó acima dele, não nele.

**As áreas não são independentes, e nenhuma delas sai do acervo.** Quem atende
decide para onde o chamado vai, quem fatura depende da leitura, e quem corta
depende da cobrança. As quatro notas de `CS‑06` a `CS‑09` existem justamente
para atravessar essas fronteiras.

---

# De onde vem cada nota

Nada aqui pede confiança cega. A coluna *Origem* diz o grau:

<!-- INICIO ORIGEM -->
| Origem | Significa | Quantas |
|---|---|---|
| **slide** | O material da academia sustenta a nota inteira | 27 |
| **misto** | As listas e os nomes são do material. **O raciocínio em volta é meu** | 14 |
| **meu** | O material dá o gancho, o desenvolvimento é meu. **Confirme antes de repetir** | 2 |
| `⟨confirmar⟩` no texto | Código ou nome de tabela de que não tenho certeza | |
<!-- FIM ORIGEM -->

A regra por trás disso está em [`PADRAO.md`](_projeto/PADRAO.md): **conteúdo não
confirmado nunca ocupa posição estrutural.** Não vira item de lista numerada
nem linha de tabela de taxonomia, porque a posição afirma mais que o rótulo.
Ela nasceu de um erro real, registrado em [`EM-ABERTO.md`](_projeto/EM-ABERTO.md).

---

# Como contribuir

**Todo `⟨confirmar⟩` é um convite.** Se você roda IS-U em produção, sua
resposta vale mais que uma semana de leitura minha.

- **[Corrigir conteúdo](../../issues/new?template=correcao-de-conteudo.yml)**,
  quando algo está errado, incompleto ou confuso
- **[Confirmar transação](../../issues/new?template=confirmar-transacao.yml)**,
  quando você sabe um código marcado como duvidoso
- **[Ver o que está aberto](../../issues)** · [`CONTRIBUTING.md`](.github/CONTRIBUTING.md) para o resto

Se você leu uma nota e não entendeu, **a nota está mal escrita**. Isso também
vale issue, e é o defeito que eu não consigo enxergar sozinho.

---

Trabalho independente, sem vínculo com a SAP nem com qualquer empregador.
SAP, SAP IS-U e S/4HANA são marcas da SAP SE. Nada aqui reproduz material de
treinamento proprietário, e este repositório não é fonte oficial: para decisão
de projeto, consulte a documentação da SAP.
