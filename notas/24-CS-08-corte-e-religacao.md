# CS-08: Corte e religação, o descompasso que gera chamado
> Dunning decide, WM executa, FI-CA confirma o pagamento. São três relógios
> diferentes, e o cliente cortado depois de pagar mora entre eles.

**Onde entra:** o segundo caso concreto da esteira da `CS-06`.
**Antes disto:** [CS-06](22-CS-06-a-esteira-do-chamado.md), [MD-05](10-MD-05-conta-contrato.md)
**Origem:** **misto.** A regra "Dunning decide e manda, quem corta é o WM" e o
descompasso vêm da [WM-02](31-WM-02-workflow-e-integracoes.md). **O roteiro de
atendimento em volta é meu.**

---

## A regra curta

**Dunning decide e manda. Quem corta é o WM. Quem confirma o pagamento é FI-CA.**

Três áreas, e nenhuma delas fala com o cliente. **Quem fala é o CRM**, e é por
isso que esta é a situação em que o atendimento mais precisa entender o que não
executa.

---

## Por que o cliente é cortado depois de pagar

Não é falha de sistema, é **descompasso de ciclos**:

```
régua de cobrança   roda no ciclo dela      →  emite a nota de corte
pagamento           entra no ciclo do banco →  chega depois
nota de corte       já saiu                 →  o técnico vai
```

A régua rodou na terça, o cliente pagou na terça à noite, o arquivo do banco
entrou na quinta, e a equipe cortou na quarta. **Cada elo funcionou, e o
resultado é errado.**

---

## O que o atendimento verifica, na ordem

| # | Pergunta | Onde | Nota |
|---|---|---|---|
| 1 | O pagamento **entrou** e foi baixado? | `FI-CA`, partida em aberto | [BI-01](39-BI-01-calculo-e-faturamento.md) |
| 2 | Existe **bloqueio de corte** na Conta Contrato? | dados mestres comerciais | [MD-05](10-MD-05-conta-contrato.md) |
| 3 | A nota de corte já virou **ordem executada**? | `WM` | [WM-01](30-WM-01-nota-de-servico.md) |
| 4 | Existe **workflow travado** entre corte e religação? | `WM` | [WM-02](31-WM-02-workflow-e-integracoes.md) |

**A pergunta 2 é a que mais resolve.** O bloqueio de corte existe justamente
para casos de negociação, contestação e cliente protegido, e ele mora na **Conta
Contrato**, não no Contrato.

---

## Corte e religação não são simétricos

| | Corte | Religação |
|---|---|---|
| Dispara | Inadimplência, pela régua | Regularização, pelo pagamento |
| Quem manda | Dunning, automático | Depende de confirmação em `FI-CA` |
| Prazo | O da régua | **Regulado**, e curto |
| Peso do erro | Alto | **Mais alto**: cliente sem energia com dívida quitada |

**A religação tem prazo regulatório**, e é o tipo de descumprimento que vira
multa. Por isso ela costuma ter workflow próprio e prioridade acima da fila
normal de campo.

---

## O erro que todo mundo comete

**Prometer religação imediata ao ver o comprovante do cliente.**

O comprovante prova que ele pagou, **não que o pagamento entrou no sistema**. A
religação depende da baixa em FI-CA, e entre uma coisa e outra existe o ciclo
do banco. Prometer imediato cria o terceiro chamado do mesmo caso.

O que dá para fazer com o comprovante é **acionar o bloqueio de corte**, que é
outra coisa e depende de política do projeto.

---

## Na prática

**Este é o par que mais gera chamado do acervo inteiro**, e a razão é
estrutural: é o único ponto em que **cobrança dispara trabalho físico**. Todo o
resto do fluxo mexe com dado; aqui alguém vai à casa de alguém.

Quando o caso travar, o número da etapa do workflow é o que localiza onde
parou. Ver [WM-02](31-WM-02-workflow-e-integracoes.md).

---

## Se sobrar uma coisa

O comprovante do cliente não é a baixa do pagamento.

---

## Recall

1. Quem decide o corte?
2. Quem executa o corte?
3. Quem confirma o pagamento?
4. Em qual objeto mora o bloqueio de corte?
5. Nomeie as quatro verificações do atendimento, na ordem.
6. O que separa corte de religação quanto a prazo?
7. Um cliente pagou e foi cortado. Cite a causa estrutural.
8. Um cliente apresenta o comprovante e pede religação imediata. Cite o que o comprovante não prova.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#cs-08)  ·  responda tudo antes de abrir.
