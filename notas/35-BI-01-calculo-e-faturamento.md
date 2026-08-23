# BI-01: Cálculo e Faturamento, a distinção que define o módulo
> Cálculo apura quanto. Faturamento acrescenta imposto, emite a conta e **cria
> a dívida**. São dois processos, dois documentos e dois objetos diferentes.

**Onde entra:** é a porta de Billing, e a pergunta que mais cai do módulo.
**Antes disto:** [MD-06](15-MD-06-contrato.md), [MD-05](10-MD-05-conta-contrato.md)

---

## A tabela que resolve a confusão

| | **Cálculo** (*Billing*) | **Faturamento** (*Invoicing*) |
|---|---|---|
| Age sobre | **Contrato** | **Conta Contrato** |
| Aplica | regras e preços | impostos e outras partidas |
| Entrada | ordem de cálculo calculável | documento de cálculo **liberado** |
| Saída | **documento de cálculo** | **documento de impressão** e **documentos FI-CA** |

**Leia a primeira linha duas vezes.** O cálculo é por contrato, o faturamento é
por conta contrato. Um cliente com três contratos na mesma conta tem **três
cálculos e uma fatura**. É por isso que a Conta Contrato existe, e é o que a
[MD-05](10-MD-05-conta-contrato.md) chama de agrupamento de fatura.

---

## Onde a dívida nasce

Repare na última célula da tabela: **só o Faturamento produz documento FI-CA.**

```
LEITURA ──▶ CÁLCULO ──▶ FATURAMENTO ──┬──▶ IMPRESSÃO
                                      └──▶ ARRECADAÇÃO ──▶ DUNNING ──▶ CARTAS
```

O cálculo apura valor e para. Ele não deve nada a ninguém: é uma conta feita,
não uma cobrança. **A dívida existe a partir do documento FI-CA**, e quem o
gera é o faturamento.

Isso tem consequência prática: **estornar um cálculo é barato, estornar um
faturamento mexe no contas a receber.**

---

## As definições do material, literais

> **Cálculo:** *"processo de aplicação de regras e preços para geração da conta
> (Billing document) para um Contrato ISU em um determinado mês com um
> determinado motivo"*. Gera e valora itens iguais às quantidades cobráveis
> multiplicadas pelos seus respectivos preços.

> **Faturamento:** *"agrega às informações do cálculo as cobranças de impostos e
> outras partidas referentes a uma Conta Contrato ISU gerando um documento de
> cobrança (Print document)"*.

**"Em um determinado mês com um determinado motivo"** não é enfeite: é o que
permite recalcular um mês fechado com motivo diferente, que é exatamente o
mecanismo da [PE-02](34-PE-02-faturado-da-epoca.md).

---

## O erro que todo mundo comete

**Usar "faturamento" para as duas coisas.**

Em português do dia a dia, faturar é calcular a conta. No IS-U, **faturar é a
segunda etapa**, e chamar a primeira de faturamento faz o interlocutor procurar
o problema no lugar errado.

Quando alguém disser "o faturamento não rodou", a primeira pergunta é: **saiu
documento de cálculo?** Se saiu, o problema está depois; se não, está antes.

---

## No sistema

| Etapa | Individual | Massa |
|---|---|---|
| Cálculo | `EA00` | `EA38` |
| Anomalias de cálculo | `EA05` | `EA05` |
| Faturamento | `EA19` | `EA26` |
| Anomalias de faturamento | `EA05` | `EA05` |
| Impressão | `EA40` | `EA29` |

### As tabelas

| Processo | Entrada | Saída |
|---|---|---|
| **Cálculo** | `ETRG` | `ERCH` `ERCHC` `DBERCHZ1` `DBERCHZ3` `DBERCHV` `ERCHO` `EITR` |
| **Faturamento** | `EITR` | `ERDK` `DBERDL` **`DFKKOP`** `DFKKEXTDOC` `ERCHC` `ERDO` `ERDB` `EITERDK` `DFKKZR` |

**`EITR` é a dobradiça:** saída do cálculo, entrada do faturamento.

**`DFKKOP` é a prova em dado.** É a partida em aberto de FI-CA, e ela só
aparece na saída do faturamento. Ver [02-BANCADA](../referencia/02-BANCADA.md).

---

## Recall

1. Cálculo age sobre qual objeto, e faturamento sobre qual?
2. Qual dos dois cria a dívida, e como se prova isso pela tabela?
3. Um cliente tem três contratos na mesma conta contrato. Quantos cálculos e quantas faturas?
4. Qual a entrada do faturamento?
5. Alguém diz "o faturamento não rodou". Qual sua primeira pergunta?

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#bi-01)  ·  responda tudo antes de abrir.
