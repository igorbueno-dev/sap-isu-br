# DM-05: O ciclo da leitura, da ordem à validação
> A leitura sai do SAP como ordem, atravessa a fronteira para a empreiteira,
> volta como resultado e só depois é validada. Quem lê não é a concessionária.

**Onde entra:** o processo por trás dos tipos e motivos da `DM-02`.
**Antes disto:** [DM-02](29-DM-02-leituras-e-registradores.md), [DM-04](31-DM-04-planejamento-de-datas.md)

---

## A fronteira que organiza tudo

O material desenha o processo em **duas raias**, e é a leitura mais importante
do slide:

```
SAP                          │  EMPREITEIRA
                             │
cria a ordem      EL01/EL09  │
baixa a ordem     EL16    ───┼──▶  coletor recebe a Ordem de Leitura
                             │     técnico vai a campo
                             │     registra o Resultado de Leitura
sobe o resultado  ELMU    ◀──┼───
valida                       │
trata             EL27       │
calcula e fatura             │
```

**A leitura é terceirizada, e o slide diz isso com uma raia própria.** O par
baixar/subir é a fronteira entre duas empresas, não entre dois programas.

---

## Individual x massa, o par que se repete

Quase toda etapa tem duas transações: uma para tratar um caso, outra para
rodar o lote.

| Etapa | Individual | Massa |
|---|---|---|
| Criação da ordem de leitura | `EL01` | `EL09` |
| Download da ordem | | `EL16` |
| Estimativa de leitura | `EL30` | `EL18` |
| Entrada de leitura manual | `EL28` | |
| Upload do resultado | | `ELMU` |
| Tratamento de leitura | `EL27` | |
| Monitoramento de leitura | `EL31` | |
| Estorno de leitura | `EL37` | |

**Repare no que não tem par.** Download e upload só existem em massa, porque
são arquivo. Entrada manual e tratamento só existem individuais, porque são
decisão de gente.

---

## A ordem de leitura tem dois nascimentos

| Tipo | Nasce de |
|---|---|
| **Periódica** | O calendário de leitura, ou seja, da [DM-04](31-DM-04-planejamento-de-datas.md) |
| **Não periódica** | Outro processo do SAP: uma mudança, uma troca de medidor, uma fiscalização |

E há um detalhe que fecha a corrente: **a ordem e o resultado são por
registrador**, não por medidor. Um medidor com seis registradores gera seis
resultados.

---

## Os três tipos de validação

A leitura que volta do campo **não entra no faturamento direto**. Ela passa por
validação, e são três camadas:

| Tipo | Como funciona |
|---|---|
| **Independente fixa** | Sempre executada pelo sistema. Não se configura |
| **Independente variável** | Configurada por **classe de validação**, e a classe é atribuída **no nível do registrador** |
| **Dependente** | Olha o resultado de **outro registrador**. Exige que exista **relação entre registradores** |

**A validação dependente é o que explica a transação `EG75`.** "Relação entre
registradores" não é enfeite de cadastro: sem ela, a validação dependente
simplesmente não roda.

### O consumo esperado

A validação compara o que veio do campo com o que o sistema esperava. O
esperado sai de **resultados de leitura históricos** mais o **consumo no
período**, e a exceção prevista é a **modificação de consumo no período**.

---

## O erro que todo mundo comete

**Tratar leitura implausível como erro do leiturista.**

Às vezes é. Mas a leitura pode estar certa e a **expectativa** errada: cliente
que viajou, indústria que parou, casa que virou escritório. A validação não diz
que a leitura está errada, diz que **ela não bate com o histórico**. Quem
decide é quem trata, no `EL27`.

---

## Na prática

**"A conta não saiu" começa aqui em metade dos casos.** A ordem de leitura
existe, o resultado voltou, e a leitura está retida em validação esperando
tratamento. Sem resultado válido não há cálculo.

O caminho de diagnóstico é curto: **existe ordem? voltou resultado? passou na
validação?** Ver [DM-02](29-DM-02-leituras-e-registradores.md).

---

## No sistema

Além da tabela de individual e massa acima:

| Transação | O que faz |
|---|---|
| `EG75` | Cria a relação entre registradores, pré-requisito da validação dependente |

---

## Se sobrar uma coisa

Quem lê o medidor não é a concessionária, e a fronteira é um arquivo.

---

## Recall

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

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#dm-05)  ·  responda tudo antes de abrir.
