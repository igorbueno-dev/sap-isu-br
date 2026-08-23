# WM-02: Workflow e as quatro integrações do campo
> O campo quase nunca decide sozinho o que fazer. O pedido chega de fora e
> anda sozinho por dentro. Este é o mapa de quem manda e de quem executa.

**Onde entra:** completa o Bloco 1, WM / SVC.
**Antes disto:** [WM-01-nota-de-servico](26-WM-01-nota-de-servico.md)

---

## As quatro integrações

São quatro as integrações que sustentam o serviço de campo, e cada uma tem um
papel diferente:

| Integração | Papel |
|---|---|
| **CRM** | **De onde o pedido vem.** Solicitações, reclamações, atendimentos |
| **Dunning** | **Quem manda cortar.** Cobrança que vira demanda operacional |
| **Billing / FI-CA** | **Para onde o dinheiro vai.** Taxas, faturas revistas, contas a receber |
| **Workflow** | **Como o pedido anda.** Aprovação, status, exceção |

**Três delas são portas, e uma é o motor.** CRM, Dunning e Billing conversam
com o campo de fora. Workflow é o mecanismo interno que faz a nota se mover.

---

## O par que mais gera chamado: Dunning e religação

A relação com Dunning vale nos dois sentidos: **inadimplência aciona nota de
corte, e regularização origina religação.** Ou seja, **a cobrança dispara
trabalho físico**, e a regra que organiza isso é curta: **Dunning decide e
manda; quem corta é o WM.**

**Por que isso quebra tanto:** são dois relógios diferentes. A régua de
cobrança roda no seu ciclo, o pagamento entra no ciclo do banco, e a nota de
corte já saiu. Cliente pagou e foi cortado é exatamente esse descompasso.
Ver [MD-05](10-MD-05-conta-contrato.md), onde mora o bloqueio de corte.

---

## O que o workflow faz

Cinco itens: **aprovações**, **encaminhamentos**, **troca de status**,
**geração de documentos** e **comunicação entre áreas**. Ou seja, o workflow é
o que faz a nota andar de uma etapa para a outra sem alguém empurrar.

**Consequência para quem atende chamado:** quando alguém diz *"a solicitação
foi registrada e nada aconteceu"*, o suspeito número um é o workflow travado,
não a nota. **A nota existe. O que não andou foi o fluxo.**

---

## Como isso aparece na tela

Um caso real que vi, de cliente com **micro e minigeração distribuída**: uma nota de
serviço tinha **quatro workflows ligados a ela ao mesmo tempo**, todos com a
tarefa "Processamento de Medidas" e encerrados no mesmo segundo. Dentro de um
deles, as etapas:

| Etapa | Status |
|---|---|
| Criar instância objeto mediante chave | encerrado |
| Referencia WF na nota de serviço | encerrado |
| Busca dados da Nota | encerrado |
| Busca Atividades do WorkFlow | encerrado |
| `027` Modificação Contratual | encerrado |
| `A016` Atualização de Operandos | encerrado |
| `A005` Atualiza Operando Micro Mini Geração | encerrado |

**Três coisas que essa tela ensina, e valem mais que a tela:**

1. **Uma nota pode ter vários workflows.** Não é um por nota
2. **As etapas são numeradas e nomeadas** (`027`, `A016`, `A005`). Numa
   investigação, o número da etapa é o que localiza onde parou
3. **O responsável é `WF BATCH`**, não uma pessoa. Rodou automático, de
   madrugada. Se travar, ninguém percebe até alguém reclamar

> **Fechado na Aula 04.** *Operando* é **dado mestre de cálculo**, a variável
> que o cálculo usa, com nó próprio de customizing. Ver
> [BI-02](36-BI-02-dados-mestres-de-calculo.md). Isso explica a estranheza: um
> workflow **de campo** atualiza operando porque o que o técnico encontra na
> rua muda a variável que o **faturamento** usa.

---

## O diagnóstico que vale levar

Quando o chamado for "pedi e não aconteceu", percorra nesta ordem:

1. **A nota existe?** Se não, o problema é na origem: CRM ou Dunning
2. **A nota tem workflow ligado?** Se não, o disparo falhou
3. **Em que etapa o workflow parou?** O nome e o número da etapa dizem o passo
4. **Quem é o responsável da etapa?** Se for `WF BATCH`, é job. Se for pessoa,
   está esperando aprovação humana

**Os passos 3 e 4 são o que separa "escalei o chamado" de "escalei com a causa
isolada".** Ver [`02-BANCADA.md`](../referencia/02-BANCADA.md).

---

## Recall

1. Quais são as quatro integrações do serviço de campo, e qual delas é o motor?
2. Dunning corta o cliente? Explique quem faz o quê.
3. Cliente pagou e foi cortado. Qual é o mecanismo por trás?
4. Uma nota pode ter mais de um workflow?
5. Você abre o workflow e o responsável da etapa travada é `WF BATCH`. O que isso te diz?
6. Alguém diz "registrei a solicitação e nada aconteceu". Qual seu primeiro suspeito?

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#wm-02)  ·  responda tudo antes de abrir.
