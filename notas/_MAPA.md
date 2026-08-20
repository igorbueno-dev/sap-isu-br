# O MAPA
### Os resumos das 31 notas, em fila

> **Arquivo gerado.** Nao edite aqui: edite a nota e rode
> `python ferramentas/gera-camadas.py`.
>
> **Como usar.** Esta e a camada de 4 minutos. Leia de ponta a ponta antes da
> aula. Onde voce nao conseguir completar a ideia sozinho, abra a nota.
>
> **A ordem aqui e a ordem da pasta**, e as duas sao a ordem de estudo.


---

## Fundacao, vale para qualquer trilha

**[GE-03: Do problema ao módulo](01-GE-03-do-problema-ao-modulo.md)**  
Cinco parágrafos de negócio, e o mapa de qual pedaço do CCS resolve cada um. Leia antes de qualquer sigla: é o "por quê" de todas elas.

**[GE-01: O que é o SAP IS-U CCS](02-GE-01-o-que-e-is-u-ccs.md)**  
O conjunto de módulos que roda o ciclo comercial de uma concessionária, do cadastro do cliente até o dinheiro entrar.

**[GE-02: A evolução do produto, do R/3 ao SaaS](03-GE-02-evolucao-do-produto.md)**  
Trinta e cinco anos em cinco marcos, e por que 2027 é a data que move o mercado inteiro.

**[GE-04: Os três setores, com peso igual](04-GE-04-os-tres-setores.md)**  
Energia, gás e saneamento rodam o mesmo núcleo. A diferença aparece em pontos específicos, e um exercício pode vir de qualquer um deles.

**[MD-01: As quatro divisões dos dados mestres](05-MD-01-mapa-dos-dados-mestres.md)**  
Antes de comparar qualquer coisa, saber o que é cada uma. São quatro divisões, não duas, e a quarta não é dado mestre.

**[MD-08: Os dois mundos e a validade no tempo](06-MD-08-os-dois-mundos.md)**  
O desenho que arruma comercial e técnico lado a lado, a ponte entre eles, e a armadilha de achar que a ordem do desenho é a hierarquia.

**[MD-02: A tradução do prédio](07-MD-02-a-traducao-do-predio.md)**  
O diagrama que converte o mundo real inteiro em vocabulário SAP, de uma vez.

**[MD-03: Parceiro de Negócios, categoria e função](08-MD-03-parceiro-de-negocios.md)**  
Quem é a pessoa, e qual papel ela cumpre. São duas perguntas diferentes, e o SAP guarda as duas em campos diferentes.

**[MD-04: Parceiro de Negócios, os dados e o customizing](09-MD-04-parceiro-de-negocios-dados.md)**  
O que cabe dentro da ficha do cliente, e onde se desenha a ficha.

**[MD-05: Conta Contrato](10-MD-05-conta-contrato.md)**  
A bolsa financeira do cliente. Reúne débitos e créditos, e é onde moram as regras de pagamento e de cobrança.

**[ST-01: Objeto de Ligação](11-ST-01-objeto-de-ligacao.md)**  
A edificação conectada à rede. O nível mais alto dos dados mestres técnicos, e onde mora o endereço.

**[ST-02: Local de Consumo](12-ST-02-local-de-consumo.md)**  
A unidade que recebe energia e é medida separadamente. O apartamento dentro do prédio.

**[ST-03: Instalação](13-ST-03-instalacao.md)**  
O objeto que efetivamente fatura. É aqui que moram a tarifa, a unidade de leitura e as regras de cálculo.

**[ST-04: Equipamento e Local de Instalação](14-ST-04-equipamento.md)**  
O aparelho físico e o lugar onde ele está parafusado. E as três formas de instalar, que explicam um chamado clássico.

**[MD-06: Contrato](15-MD-06-contrato.md)**  
A dobradiça do sistema. É o único objeto que toca o mundo comercial e o mundo técnico ao mesmo tempo.

**[MD-07: Move-In e Move-Out](16-MD-07-move-in-move-out.md)**  
O processo que cria e encerra o Contrato.


---

## Atendimento e relacionamento (CRM)

**[CS-01: O que é CRM](17-CS-01-o-que-e-crm.md)**  
A disciplina antes do produto. CRM é um jeito de organizar o relacionamento com o cliente, e só depois um sistema da SAP.

**[CS-02: Ciclo de vida do cliente](18-CS-02-ciclo-de-vida-do-cliente.md)**  
Seis etapas de um lado, três pilares do outro. São a mesma coisa vista de perto e de longe, e vale enxergar as duas juntas.

**[CS-03: SAP CRM e os três pilares](19-CS-03-sap-crm-e-os-pilares.md)**  
O produto. Marketing, Vendas e Serviço, cada um com sua fileira de módulos. E o nome novo que a SAP deu a tudo isso dentro do S/4HANA.

**[CS-04: CRM no contexto Utilities](20-CS-04-crm-no-contexto-utilities.md)**  
Onde exatamente o CRM se encaixa na cadeia que você já conhece. Ele é a primeira área, a porta por onde tudo entra.

**[CS-05: Processos e atividades no atendimento](21-CS-05-processos-e-atividades.md)**  
O que o atendente realmente faz o dia inteiro. Protocolo, atividade e a lista de processos que respondem por quase todo o volume de um call center de concessionária.


---

## Arquitetura e integracao

**[AR-01: O landscape e as cinco camadas](22-AR-01-landscape-e-camadas.md)**  
Dois desenhos da mesma coisa. Um simples, para entender; um detalhado, para se localizar. Comece pelo simples.

**[AR-02: Middleware e replicação](23-AR-02-middleware-e-replicacao.md)**  
Como um dado criado no CRM aparece no IS-U. Um caminho de cinco paradas, e as transações para olhar cada uma quando ele trava.

**[AR-03: Objetos replicados](24-AR-03-objetos-replicados.md)**  
Quatro objetos existem dos dois lados com nomes e tabelas diferentes. Este de-para é o que você consulta quando alguém diz "o dado está divergente".


---

## Servico de Campo (SVC)

**[SV-01: Serviço de Campo (SVC) e os três blocos](25-SV-01-servico-de-campo.md)**  
A área tem quatro nomes circulando e três blocos por dentro. Acertar o vocabulário aqui evita meia hora de conversa errada numa reunião.

**[WM-01: A nota de serviço e o ciclo do campo](26-WM-01-nota-de-servico.md)**  
Tudo que o campo faz começa numa nota de serviço. Ela carrega tipo, motivo, prioridade e prazo, e é o prazo que dá multa.

**[WM-02: Workflow e as quatro integrações do campo](27-WM-02-workflow-e-integracoes.md)**  
O campo quase nunca decide sozinho o que fazer. O pedido chega de fora e anda sozinho por dentro. Este é o mapa de quem manda e de quem executa.

**[DM-01: Ativos, movimentação e estoque](28-DM-01-ativos-e-estoque.md)**  
O medidor tem uma vida inteira antes e depois de estar na parede. Device Management é quem sabe onde cada um está, e onde esteve.

**[DM-02: Leituras e registradores](29-DM-02-leituras-e-registradores.md)**  
Seis tipos de leitura, cinco motivos e seis registradores. Parece lista de decorar, e não é: cada eixo responde uma pergunta diferente da investigação.

**[PE-01: Gestão de Perdas, fraude e defeito](30-PE-01-fraude-e-defeito.md)**  
A mesma consequência, dois mundos jurídicos diferentes. Classificar errado aqui é o erro que vira processo.

**[PE-02: Faturado da época x fatura revista](31-PE-02-faturado-da-epoca.md)**  
O cálculo que transforma uma irregularidade em valor a cobrar. Duas contas do mesmo período, e a diferença entre elas é a receita recuperada.

---

> 31 notas, 131 perguntas.
