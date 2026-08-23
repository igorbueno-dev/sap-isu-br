# A BANCADA

### Consulta, não leitura

> **Este arquivo não é para ser estudado.** É uma caixa de ferramentas.
> Abra quando estiver diante do sistema ou quando precisar lembrar de uma sigla.
> Ler isto em sequência é a melhor forma de desperdiçar seu tempo de preparação.
>
> **Por que ele fica inteiro e não vira nota atômica:** isto é consulta, não
> revisão. Você procura aqui, não lê. Um `Ctrl+F` num arquivo vale mais que
> abrir oito. **Lookup quer ser grande e buscável.**

## Salto rápido: as transações que você mais vai usar


| Preciso de                                              | Transação                  |
| --------------------------------------------------------- | ------------------------------ |
| Criar / modificar / exibir **Parceiro de Negócios**     | `FPP1` `FPP2` `FPP3` ou `BP` |
| Criar / modificar / exibir **Conta Contrato**            | `CAA1` `CAA2` `CAA3`         |
| Modificar / exibir **Contrato**                          | `ES21` `ES22`                |
| Criar / modificar / exibir **Objeto de Ligação**       | `ES55` `ES56` `ES57`         |
| Criar / modificar / exibir **Local de Consumo**          | `ES60` `ES61` `ES62`         |
| Criar / modificar / exibir **Instalação**              | `ES30` `ES31` `ES32`         |
| Criar / modificar / exibir **Local de Instal. Equip.** | `ES65` `ES66` `ES67`         |
| **Instalar equipamento** (total / técnica / cálculo)  | `EG31` `EG33` `EG34`         |
| Parametrizar qualquer coisa                             | `SPRO`                       |
| Achar uma transação pelo nome                         | `SE93`                       |

**Menu em português:** `Serviços públicos`, não "Utilities".

**Índice**

1. [Glossário de siglas](#1-glossário-de-siglas)
2. [Como achar qualquer transação sem chutar](#2-como-achar-qualquer-transação-sem-chutar)
3. [Transações por módulo](#3-transações-por-módulo)
4. [Tabelas](#4-tabelas)
5. [Roteiro do exercício: criar um cliente do zero](#5-roteiro-do-exercício-criar-um-cliente-do-zero)

**O que saiu daqui**, porque não era consulta:

| Foi para | O quê |
|---|---|
| [`BI-05`](../notas/43-BI-05-o-que-precisa-para-faturar.md) | Os oito pré-requisitos de faturamento e a árvore da fatura que não saiu |
| [`GE-01`](../notas/02-GE-01-o-que-e-is-u-ccs.md) | IS-U não é sistema separado, e a pergunta "isso é padrão ou é nosso" |
| [`_projeto/PREPARACAO.md`](../_projeto/PREPARACAO.md) | O que costuma ser cobrado, os tipos de exercício e o que se escala |
| As notas, na zona *O erro que todo mundo comete* | As armadilhas de iniciante. **14 das 19 já tinham dono** |

---

# 1. Glossário de siglas


| Sigla         | Nome completo em inglês                   | Em português                                                  | O que faz                                                                                           |
| --------------- | -------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **IS-U**      | Industry Solution for Utilities            | Solução Setorial para Concessionárias                       | O conjunto de módulos SAP para cadastro, medição, faturamento e cobrança de serviços públicos |
| **BP**        | Business Partner                           | Parceiro de Negócios                                          | Quem é a pessoa ou empresa: nome, documento, endereço, contatos                                   |
| **CA**        | Contract Account                           | Conta Contrato                                                 | Como o cliente paga: forma de pagamento, régua de cobrança, agrupamento de fatura                 |
| **PoD**       | Point of Delivery                          | Ponto de Entrega                                               | Identificador padronizado do ponto de fornecimento, para troca de dados entre agentes de mercado    |
| **DM**        | Device Management                          | Gestão de Dispositivos                                        | Ciclo de vida do medidor: instalação, troca, remoção, aferição, registradores                 |
| **EDM**       | Energy Data Management                     | Gestão de Dados de Energia                                    | Medição em intervalos (curva de carga), perfis, faturamento por intervalo                         |
| **WM**        | Work Management                            | Gestão de Serviços de Campo                                  | Planeja, despacha e confirma trabalho em campo.<br />**Não confundir com Warehouse Management**    |
| **FI-CA**     | Contract Accounts Receivable and Payable   | Contas a Receber e a Pagar por Conta Contrato                  | Contas a receber de alto volume: partidas, pagamentos, cobrança, repasse ao razão                 |
| **IDE**       | Intercompany Data Exchange                 | Troca de Dados entre Empresas                                  | Processos de mercado desregulamentado: troca de fornecedor, envio de medição entre agentes        |
| **MDUS**      | Meter Data Unification and Synchronization | Unificação e Sincronização de Dados de Medição           | Integração entre o SAP e o sistema de telemetria                                                  |
| **AMI**       | Advanced Metering Infrastructure           | Infraestrutura de Medição Avançada                          | Medidores inteligentes, rede de comunicação e concentradores                                      |
| **RTP**       | Real Time Pricing                          | Preço em Tempo Real                                           | Tarifa que varia por intervalo, faturada a partir de curva de carga                                 |
| **MRU**       | Meter Reading Unit                         | Unidade de Leitura                                             | Agrupamento geográfico: a rota do leiturista                                                       |
| **CRM**       | Customer Relationship Management           | Gestão do Relacionamento com o Cliente                        | Atendimento: contatos, solicitações, reclamações                                                |
| **BW**        | Business Warehouse                         | Armazém de Dados de Negócio                                  | Extrai, armazena e reporta dados para análise                                                      |
| **FI**        | Financial Accounting                       | Contabilidade Financeira                                       | Razão contábil e balanço. Recebe totais do FI-CA                                                 |
| **CO**        | Controlling                                | Controladoria                                                  | Custos e centros de custo. Recebe custo das ordens de serviço                                      |
| **PM**        | Plant Maintenance                          | Manutenção de Ativos                                         | Manutenção de equipamentos. Base técnica do dispositivo e do WM                                  |
| **EAM**       | Enterprise Asset Management                | Gestão de Ativos Empresariais                                 | Nome moderno do PM, mesma função                                                                  |
| **CS**        | Customer Service                           | Serviço ao Cliente                                            | Ordens e notas voltadas ao cliente. Parte do WM                                                     |
| **MM**        | Materials Management                       | Gestão de Materiais                                           | Compras e estoque. Fornece o material da ordem de serviço                                          |
| **SD**        | Sales and Distribution                     | Vendas e Distribuição                                        | Vendas convencionais. Pouco usado no ciclo de utilities                                             |
| **CIC**       | Customer Interaction Center                | Central de Interação com o Cliente                           | Tela unificada de atendimento no IS-U clássico                                                     |
| **IDoc**      | Intermediate Document                      | Documento Intermediário                                       | Formato padrão SAP de mensagem para sistemas externos                                              |
| **BAPI**      | Business Application Programming Interface | Interface de Programação de Aplicação                      | Função padrão chamável por sistemas externos                                                    |
| **BAdI**      | Business Add-In                            | Complemento de Negócio                                        | Ponto de extensão onde o projeto insere lógica própria                                           |
| **CDS**       | Core Data Services                         | Serviços de Dados Centrais                                    | Camada de views do S/4HANA usada em analytics e Fiori                                               |
| **SAC**       | SAP Analytics Cloud                        | SAP Analytics Cloud                                            | Visualização e planejamento em nuvem                                                              |
| **NF3e**      | (não é sigla em inglês)                 | Nota Fiscal de Energia Elétrica eletrônica                   | Documento fiscal eletrônico brasileiro de energia. É localização, não padrão global           |
| **ANEEL**     | (não é sigla em inglês)                 | Agência Nacional de Energia Elétrica                         | Regulador brasileiro do setor elétrico                                                             |
| **TUSD / TE** | (não é sigla em inglês)                 | Tarifa de Uso do Sistema de Distribuição / Tarifa de Energia | As duas parcelas da tarifa brasileira. Componentes distintos na estrutura tarifária                |

---

# 2. Como achar qualquer transação sem chutar

**Esta seção vale mais que a próxima.** Códigos de transação mudam entre versões, e no S/4HANA muitos foram substituídos por apps Fiori. Saber achar é melhor que saber decorar.


| O que fazer                               | Como                                                                                                                    |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Pesquisar transação por descrição** | Transação `SE93`. Digite parte do nome e veja os códigos                                                              |
| **Navegar pelo menu**                     | O SAP Easy Access tem a árvore inteira em Utilities Industry. É o caminho oficial e sempre correto para a sua versão |
| **Ver onde você está**                  | O código da transação atual costuma aparecer no rodapé ou no campo de comando                                       |
| **Perguntar a quem já roda o módulo**      | O melhor método. Peça a lista das transações que o time usa no dia a dia                                            |

> **Regra de honestidade deste material:** tudo marcado com **(confirmar)** é algo cujo código exato eu não garanto. Prefiro deixar em branco a dar um código errado que alguém vai digitar na frente de um cliente.

## De onde vêm estes códigos

Cruzamento feito em **20/08/2026** contra a transcrição das aulas 1 a 3.

| Origem | Quantos | Confiança |
|---|---|---|
| **Vistos em slide** | **48 de 76** | Alta. Vieram das árvores de menu e dos exercícios das aulas |
| Não vistos em slide | 28 | **Não repita sem conferir** |

Os 28 sem respaldo são de duas famílias, e nenhuma é de dados mestres:

- **Básis e técnico**, que ninguém cobra de júnior de módulo: `SE11` `SE16`
  `SE16N` `SE93` `SM37` `SP01` `SU53` `SLG1`
- **Módulos vizinhos ainda não dados**: manutenção (`IW*` `IL*` `IE0*` `IQ0*`),
  BW (`RSA*`) e a parte de FI-CA que não foi apresentada (`FPE*` `FPL9`)

**Os códigos de dados mestres, que são os que caem em exercício, estão todos
no grupo confirmado:** `FPP1` `CAA1` `ES21` `ES55` `ES60` `ES30` `ES65` `EG31`
e as famílias em volta deles.

---

# 3. Transações por módulo

## Diagnóstico geral (serve para todas as trilhas)


| Transação       | O que faz                                                                             |
| ------------------- | --------------------------------------------------------------------------------------- |
| `SE16N` ou `SE16` | Exibe o conteúdo de qualquer tabela. **Sua ferramenta mais usada como júnior**       |
| `SE11`            | Dicionário de dados: ver a estrutura e os campos de uma tabela                       |
| `SE93`            | Pesquisar transações por descrição                                                |
| `SM37`            | Monitorar processamentos em background. Os jobs de faturamento e cobrança rodam aqui |
| `SLG1`            | Log de aplicação. Onde muitos processos IS-U gravam o motivo real do erro           |
| `ST22`            | Dumps de programa (erros graves)                                                      |
| `SU53`            | Verificar falha de autorização depois de um "sem permissão"                        |
| `SP01`            | Fila de impressão. Útil para conferir emissão de faturas                           |

## Dados mestres

> **Verificado.** Todos os códigos desta seção foram conferidos no menu do
> sistema. Nenhum leva marca `(confirmar)`.
>
> **Menu em português:** `Serviços públicos`, não "Utilities".
> Comerciais em `Dados mestre comerciais`, técnicos em `Dados mestre técnicos`.

### Comerciais


| Transação              | O que faz                                        |
| -------------------------- | -------------------------------------------------- |
| `FPP1` ou `BP`           | **Criar** Parceiro de Negócios                  |
| `FPP2` ou `BP`           | **Modificar** Parceiro de Negócios              |
| `FPP3` ou `BP`           | **Exibir** Parceiro de Negócios                 |
| `FPCR1`&nbsp;/&nbsp;`FPCR2`        | Exibir / modificar solvência (creditworthiness) |
| `FP05BNKD`               | Copiar dados bancários                          |
| `FPP2A`                  | Ativar modificações planejadas                 |
| `CAA1`&nbsp;/&nbsp;`CAA2`&nbsp;/&nbsp;`CAA3` | Criar / modificar / exibir Conta Contrato        |
| `ES21`                   | **Modificar** Contrato                           |
| `ES22`                   | **Exibir** Contrato                              |
| `ES27`                   | Modificar todos os contratos                     |
| `ES28`                   | Exibir todos os contratos                        |

> **Não existe transação de criar Contrato.** Ele nasce do **Move In**.
> Quem procura "criar contrato" no menu não acha, e conclui errado que falta
> autorização. Ver [MD-06-contrato](../notas/15-MD-06-contrato.md).

### Técnicos


| Transação              | O que faz                                                          |
| -------------------------- | -------------------------------------------------------------------- |
| `ES55`&nbsp;/&nbsp;`ES56`&nbsp;/&nbsp;`ES57` | Criar / modificar / exibir **Objeto de Ligação**                  |
| `ES60`&nbsp;/&nbsp;`ES61`&nbsp;/&nbsp;`ES62` | Criar / modificar / exibir Local de Consumo                        |
| `ES30`&nbsp;/&nbsp;`ES31`&nbsp;/&nbsp;`ES32` | Criar / modificar / exibir Instalação                            |
| `ES65`&nbsp;/&nbsp;`ES66`&nbsp;/&nbsp;`ES67` | Criar / modificar / exibir **Local de Instalação de Equipamento** |

> **Vocabulário.** Em português o sistema usa **Objeto de Ligação** (traduzido
> em alguns materiais como "Objeto de Conexão") e **Equipamento** ("Dispositivo"
> em outros). Este material adota os termos do menu em português.
>
> **Cuidado com códigos parecidos.** Para criar, os corretos são `ES60` (local
> de consumo) e `ES30` (instalação). `ES53` e `ES33` não pertencem a eles.

### Customizing de dados mestres


| Transação | O que faz                                                  |
| ------------- | ------------------------------------------------------------ |
| `SPRO`      | O IMG inteiro. A porta de entrada de toda parametrização |
| `BUPT`      | Customizing de Parceiro de Negócios                       |
| `BUMR`      | Customizing de relacionamentos de PN                       |
| `CAWM`      | Customizing de Conta Contrato                              |

Detalhe fino de PN: `BUCF` faixas de numeração · `BUC2` agrupamentos ·
`BUCD` tipos de PN · `BUCG` campos por função · `BUC4` tipo de endereço
padrão · `BUC0` formas de tratamento · `BUCM` tipos de legitimação ·
`SA13` formatação de nome · `BUCK` estado civil · `BUCL` profissões ·
`BUCA` ramos · `BUC8` formas jurídicas · `BUC9` entidade legal ·
`BUSO` categoria de PN · `BUBA` categorias de relacionamento ·
`BUS5` layout de tela · `BUB9` faixas de relacionamento

### Ainda em aberto


| Item                                 | Situação                                                                                                               |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Move-In / Move-Out                   | **(confirmar)**. É o processo que cria o Contrato. **Lacuna prioritária a fechar**                                    |
| Visão geral do cliente              | **(confirmar)**. A transação que mostra a hierarquia inteira numa tela                                                |
| Nós `Ligação` e `Ponto de entrega` | Aparecem no menu de dados mestre técnicos e ainda não explorei. **(confirmar)**                                        |

## Move-In / Move-Out


| Transação                      | O que faz                                                                                                                                               |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Move-In / Move-Out / Move-In-Out | **(confirmar)**. Ficam na área de Customer Service do menu IS-U. São os três códigos mais usados em exercício prático                     |

## Equipamento (Device Management)


| Transação              | O que faz                                                           |
| -------------------------- | --------------------------------------------------------------------- |
| `IQ01`&nbsp;/&nbsp;`IQ02`&nbsp;/&nbsp;`IQ03` | Criar / alterar / exibir Equipamento (a camada de ativo do medidor) |
| `IE03`                   | Exibir equipamento pela visão de manutenção                      |

> **Verificado.** Caminho:
> `Serviços públicos > Gerência de equipamentos > Instalação > Instalação`


| Transação | O que faz                                                                  |
| ------------- | ---------------------------------------------------------------------------- |
| `EG31`      | Instalação **Total** (técnica **e** com efeito no faturamento)           |
| `EG33`      | Instalação **Técnica** (coloca o aparelho, **sem** mexer no faturamento) |
| `EG34`      | Instalação **com efeito no cálculo da fatura**                           |
| `EG51`      | **Estorno técnico**                                                       |

> **A pegadinha mais útil do módulo.** Medidor trocado no campo e conta
> ainda vindo com o antigo? Quase sempre alguém fez `EG33` (técnica) e não
> fez `EG34` (efeito no cálculo). Ver [ST-04-equipamento](../notas/14-ST-04-equipamento.md).
>
> **Equipamento não é só o medidor.** O Transformador de Corrente (TC)
> também é cadastrado como Equipamento.

## Leitura


| Transação   | O que faz                                                                                                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Família `EL*` | Criação de ordem de leitura, entrada de resultado, correção de leitura implausível, upload e download de arquivo, monitoramento. **(confirmar)** os códigos. Os três que importam: **criar ordem, informar resultado, corrigir leitura** |

## Faturamento e emissão


| Transação          | O que faz                                                                                                                                                                                                                         |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Família `EA*`        | Simulação de faturamento, faturamento individual, exibição do documento, emissão de fatura, estorno. **(confirmar)** os códigos. Os cinco que importam: **simular, faturar, exibir documento, emitir a fatura, estornar** |
| Faturamento em massa | Roda como atividade em massa, não como transação individual. Monitorada por `SM37`. **(confirmar)** o monitor específico                                                                                                       |

## Finanças e cobranças (FI-CA)


| Transação                      | O que faz                                                                                                                                |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `FPL9`                           | **Exibir a conta do cliente:** todas as partidas, abertas e compensadas. **A transação mais importante de toda a trilha de cobrança** |
| `FPE1`&nbsp;/&nbsp;`FPE2`&nbsp;/&nbsp;`FPE3`         | Criar / alterar / exibir documento FI-CA                                                                                                 |
| Lote de pagamento                | Família `FP0*`. **(confirmar)**                                                                                                          |
| Cobrança: proposta e execução | Família `FPV*`. **(confirmar)** qual é a proposta e qual é a execução                                                                |
| Plano de parcelamento            | **(confirmar)**                                                                                                                          |

## Campo (Work Management)


| Transação                              | O que faz                                             |
| ------------------------------------------ | ------------------------------------------------------- |
| `IW21`&nbsp;/&nbsp;`IW22`&nbsp;/&nbsp;`IW23`                 | Criar / alterar / exibir Nota                         |
| `IW31`&nbsp;/&nbsp;`IW32`&nbsp;/&nbsp;`IW33`                 | Criar / alterar / exibir Ordem                        |
| `IW41`                                   | Confirmar execução da ordem                         |
| `IL03`                                   | Exibir Local de Instalação (visão de manutenção) |
| Documentos de desligamento e religação | Família `EC8*`. **(confirmar)**                       |

## CRM e Middleware

> **Verificado.** Estes códigos foram conferidos. O entendimento do fluxo está
> em [`notas/AR‑02`](../notas/27-AR-02-middleware-e-replicacao.md).

### Replicação e carga

| Transação | O que faz |
|---|---|
| `SMW01` | **BDocs.** O envelope em que o dado viaja. Primeira parada de qualquer investigação |
| `R3AS` | **Carga inicial.** Traz tudo de uma vez, na implantação |
| `R3AR2` | **Repetição de carga.** Para o que não veio |
| `SMOEAC` | Sites e conexões: quem fala com quem |
| `SMOEACPR` | Sites, perfis |
| `SMOEACLINK` | Sites, vínculos |

### Monitoramento

| Transação | O que faz |
|---|---|
| `SMQ1` | **Filas qRFC de entrada.** O que está parado chegando |
| `SMQ2` | **Filas qRFC de saída.** O que está parado saindo |
| `SM58` | **RFC Monitor.** Chamada remota travada |
| `R3AM1` | Monitoramento geral do middleware |
| `SM21` | Log do sistema |
| `ST22` | **Dump.** Erro de programa no destino |

### Business Partner no CRM

| Transação | O que faz |
|---|---|
| `BUT000` | Parceiro de Negócio |
| `BUPA_MAIN` | Dados complementares do parceiro |

> **A sequência que resolve a maioria dos chamados de integração.**
> "Criei no CRM e não apareceu no IS-U":
>
> `SMW01` (o BDoc saiu?) → `SMQ1` e `SMQ2` (parou na fila?) →
> `SM58` (a conexão caiu?) → `ST22` (deu dump?)
>
> Quase nunca é bug. Quase sempre é fila.

### O de-para de objetos entre os dois sistemas

| Objeto | IS-U / CCS | CRM |
|---|---|---|
| Parceiro de Negócio | `BUT000` | `BUT000` |
| Conta Contrato | `FKKVKP` | `CRMM_BUAG` |
| Objeto de Ligação | `EHAUISU` **(confirmar)** | `COMM_PRODUCT` |
| Ponto de Entrega (PoD) | `EUIHEAD` **(confirmar)** | `IBASE` / `COMM_PRODUCT` |

> **As duas marcas `(confirmar)` acima são reais.** Encontrei `EHAU` e
> `EHAUISU` para o Objeto de Ligação e não sei qual é a correta.
> **Se você sabe, abra uma issue.**

---

## BW e analytics


| Transação     | O que faz                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------- |
| `RSA1`          | Data Warehousing Workbench: onde vive toda a modelagem do BW                           |
| `RSA3`          | Extractor Checker: testar um extrator no sistema de origem e ver os dados que ele traz |
| `RSA5`&nbsp;/&nbsp;`RSA6` | Ativar e visualizar DataSources de conteúdo padrão                                   |

---

# 4. Tabelas

> **Origem.** Os nomes e o papel de cada tabela foram conferidos contra o
> pôster *"A selection of useful ISU tables"*, o mesmo que apareceu na Aula 04.
> As marcas `(confirmar)` que havia aqui **caíram todas**.

## Dados mestres comerciais

| Tabela | Conteúdo |
|---|---|
| `BUT000` | Parceiro de Negócios, dados gerais |
| `BUT020` | Endereços do Parceiro de Negócios |
| `BUT050` | **Relacionamentos entre parceiros** |
| `BUT100` | **Funções do parceiro** (as funções da `MD-03`) |
| `BUT0BK` | Dados bancários do parceiro |
| `ADRC` | Endereços |
| `EKUN` | Dados IS-U do parceiro de negócios |
| `FKKVK` | Conta Contrato, cabeçalho |
| `FKKVKP` | Conta Contrato, dados dependentes do parceiro |
| `EVER` | **Contrato de utilities. A tabela central que liga cliente e instalação** |

## Dados mestres técnicos

| Tabela | Conteúdo |
|---|---|
| `EHAUISU` | **Objeto de Ligação.** Chave `HAUS` |
| `EVBS` | Local de Consumo. Chave `VSTELLE` |
| `EANL` | Instalação. Chave `ANLAGE` |
| `EANLH` | Instalação, faixa de tempo (as versões com validade) |
| `EUIHEAD` | **Ponto de Entrega (PoD)** |
| `EUIINSTLN` | Instalação ↔ PoD |
| `EQUI` | Equipamento. **É tabela do PM**, não do IS-U |
| `ETYP` | Categoria de equipamento e dados de material |
| `EASTL` | Instalação ↔ equipamento |
| `EASTS` | Instalação ↔ registrador |

## Registradores

| Tabela | Conteúdo |
|---|---|
| `ETDZ` | Registradores |
| `EZWG` | **Grupo de registradores** (o `EG04`) |
| `EASTI` | **Relação entre registradores** (o `EG75`, pré-requisito da validação dependente) |
| `EADZ` | Dados de registrador para instalação com faturamento múltiplo |

## Planejamento de datas e leitura

| Tabela | Conteúdo |
|---|---|
| `TE420` | **Porções.** Provável tabela do *Conjunto de Contratos* |
| `TE422` | **Unidades de leitura.** A *Unidade de Leitura* da Aula 04 |
| `TE417` | Registros de agenda das porções |
| `TE418` | Registros de agenda das unidades de leitura |
| `TE419` | Registros de parâmetros. Chave `TERMSCHL` |
| `ETRG` | **Ordens de cálculo.** É o input do cálculo, ver `img-28` |
| `EABL` | **Documento de leitura** |
| `EABLG` | **Motivos de leitura.** Os cinco motivos da `DM-02` |

> **Inferência, não fato do slide:** o par *Conjunto de Contratos* e *Unidade de
> Leitura* da Aula 04 corresponde ao par **Portion** e **Meter Reading Unit**
> do vocabulário SAP em inglês. A evidência é forte (são os dois únicos
> objetos com exatamente esses papéis, e o pôster dá agenda para os dois), mas
> **o material nunca fez a ligação em voz alta.** Confirmar.

## Cálculo e faturamento

| Tabela | Conteúdo |
|---|---|
| `ERCH` | **Documento de cálculo, cabeçalho** |
| `DBERCHZ1` a `DBERCHZ8` | Linhas do documento de cálculo. **As variantes numeradas existem mesmo** |
| `ERCHC` | Histórico de faturamento e estorno |
| `ERCHO` | **Anomalia do documento de cálculo** (*outsorting*) |
| `ERDK` | **Documento de impressão, a fatura, cabeçalho** |
| `DBERDL` | Linhas do documento de impressão |
| `ERDO` | **Anomalia da fatura** (*outsorting*) |
| `ERDB` | Documento FI-CA do documento de impressão |

> **`outsorting` é o nome em inglês do que a Aula 04 chamou de anomalia.**
> Duas tabelas separadas, `ERCHO` para o cálculo e `ERDO` para a fatura, é a
> mesma assimetria que o fluxo do `img-27` mostra.

## Tarifa e preço

| Tabela | Conteúdo |
|---|---|
| `ETRF` | Tarifas |
| `EKDI` | Fatos da tarifa |
| `ETTA` | Categoria de tarifa |
| `ETTAF` | Fatos da categoria de tarifa |
| `TE069` | Tipos de tarifa |
| `ERTFND` | **Determinação de tarifa** (a regra `CT3 + TT4 = T2, T9, T22`) |
| `ESCH` | Esquema de cálculo, cabeçalho |
| `ESCHS` | Etapas do esquema |
| `EPREI` | Preços, cabeçalho |
| `EPREIH` | Histórico de preços |
| `TE221` | **Operandos** |

## FI-CA

| Tabela | Conteúdo |
|---|---|
| `DFKKKO` | Documento FI-CA, cabeçalho |
| `DFKKOP` | **Partidas do documento FI-CA. A tabela do contas a receber** |
| `DFKKOPK` | Partidas de razão |
| `FKKMAKO` | Histórico de dunning |
| `FKKMAZE` | Itens de dunning |
| `DFKKZK` / `DFKKZP` | Lote de pagamento, cabeçalho e dados |
| `DFKKRK` / `DFKKRP` | Lote de devolução |
| `FKK_INSTPLN_HEAD` | Plano de parcelamento |
| `EABP` | Plano de consumo estimado (*budget billing plan*) |

## Estrutura regional e postal

**A divisão 1 dos dados mestres finalmente tem substância.**

| Tabela | Conteúdo |
|---|---|
| `ADRCITY` | Cidades |
| `ADRPSTCODE` | **Códigos postais** |
| `ADRCITYPRT` | **Distritos postais** |
| `ADRSTREET` | Logradouros |
| `ADRCITYMRU` | **Unidades de leitura por cidade** |
| `ADRSTRTMRU` | **Unidades de leitura por logradouro** |
| `ADRCITYCCS` / `ADRSTRTCCS` | Dados de setor por cidade e por logradouro |
| `ADRCITYKON` / `ADRSTRTKON` | Contratos de concessão por cidade e por logradouro |

> **Isto explica por que a Estrutura Postal abre a lista dos dados mestres.**
> As duas tabelas `*MRU` ligam o endereço à **unidade de leitura**: é a
> estrutura postal que diz qual rota atende cada rua. Sem ela, não há
> roteirização, e sem roteirização não há leitura nem faturamento.
>
> Continua valendo perguntar ao instrutor o que o projeto chama de Estrutura
> Postal e quais transações a mantêm. **O que se sabe agora é onde ela mora.**
>
> **Esta tabela também está na nota**, em
> [`05-MD-01`](../notas/05-MD-01-mapa-dos-dados-mestres.md), seção 1, com a
> leitura de por que a Estrutura Postal abre a lista dos dados mestres. Aqui
> ela fica como consulta; lá, como argumento.

## O exercício de navegação que fixa a arquitetura

Vale mais que dez horas de teoria. Pegue um contrato qualquer no sandbox e percorra:

```
Caminho 1, o cadastro
  EVER  ──▶  EANL  ──▶  EVBS
  o contrato  a instalação  o local de consumo

Caminho 2, o dinheiro, pelo mesmo contrato
  ERCH  ──▶  ERDK  ──▶  DFKKOP
  o cálculo   a fatura     a dívida
```

**Faça isso três vezes com clientes diferentes.** Na terceira, a arquitetura para de ser abstrata.

---

# 5. Roteiro do exercício: criar um cliente do zero

Este é o exercício prático mais cobrado em SAP Utilities, e frequentemente cronometrado. **Faça pelo menos cinco vezes, e nas últimas duas sem olhar este roteiro.**

```
PARTE A: a estrutura física
  Pode já existir no sandbox. Confirme antes de criar.

  1  OBJETO DE LIGAÇÃO ......... ES55   endereço, dados de conexão
        │
        ▼
  2  LOCAL DE CONSUMO .......... ES60   vinculado ao objeto de ligação
        │
        ├──▶ 3  LOCAL DE INSTALAÇÃO DE EQUIPAMENTO ... ES65
        │
        └──▶ 4  INSTALAÇÃO ...... ES30   vinculada ao local de consumo
                 ATENÇÃO: preencher a categoria tarifária.
                 Errar aqui não dá erro, dá conta errada depois.

PARTE B: o cliente
  5  PARCEIRO DE NEGÓCIOS ...... BP     pessoa física, nome, documento
        │
        ▼
  6  CONTA CONTRATO ............ CAA1   forma de pagamento, régua

PARTE C: o medidor
  7  Criar ou localizar o EQUIPAMENTO, com o tipo correto
        │
        ▼
  8  INSTALAR o equipamento. SÃO DOIS PASSOS, não pule o segundo:
        a. instalação TÉCNICA, no local de instalação
        b. instalação PARA FATURAMENTO, com a relação registrador e tarifa

PARTE D: a amarração
  9  MOVE-IN: conta contrato + instalação, data de início e LEITURA
     INICIAL. Isto cria o CONTRATO.
        ▲
        └── depende de 4, de 6 e de 8

PARTE E: o ciclo, a continuação natural
  10 Informar RESULTADO DE LEITURA ..... família EL
  11 Rodar o FATURAMENTO ............... família EA
  12 Emitir a FATURA ................... família EA
  13 Conferir a partida em aberto ...... FPL9
```

## Os cinco erros mais comuns neste exercício

1. **Esquecer a instalação para faturamento** no passo 8. Tudo parece certo e nada fatura.
2. **Errar a ordem.** Tentar fazer o Move-In antes de a Instalação existir.
3. **Data de Move-In posterior à data da leitura** que você quer usar.
4. **Categoria tarifária em branco ou errada** no passo 4.
5. **Criar um segundo BP** por não ter procurado antes se ele já existia.

---
