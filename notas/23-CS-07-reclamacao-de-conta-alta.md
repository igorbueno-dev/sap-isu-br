# CS-07: Reclamação de conta alta, o roteiro de diagnóstico
> O chamado mais comum da concessionária atravessa três áreas, e o atendimento
> decide qual delas investiga primeiro.

**Onde entra:** o caso concreto da esteira da `CS-06`.
**Antes disto:** [CS-06](22-CS-06-a-esteira-do-chamado.md)
**Origem:** **misto.** Cada causa abaixo vem de uma nota com fonte no material.
**O roteiro que as ordena é meu.**

---

## Por que este chamado é o teste do analista

"Minha conta veio alta" não diz nada sobre onde está o problema. Pode ser
leitura, cálculo, cadastro, irregularidade **ou consumo real**, e as cinco
exigem respostas diferentes.

**Fechar como "consumo real" sem verificar é o erro caro**, porque se havia
defeito o cliente volta, agora com o regulador junto.

---

## As cinco causas, na ordem de investigação

A ordem não é arbitrária: vai **do mais barato de verificar para o mais caro**.

| # | Causa | Onde se verifica | Nota |
|---|---|---|---|
| 1 | **Leitura errada ou estimada** | O resultado voltou do campo? passou na validação? foi estimativa? | [DM-05](36-DM-05-ciclo-da-leitura.md) |
| 2 | **Documento retido em anomalia** | O sistema já desconfiou e alguém liberou sem olhar | [BI-03](41-BI-03-anomalias.md) |
| 3 | **Tarifa errada na instalação** | Categoria de tarifa na faixa de tempo, e o Indicador de Baixa Renda | [BI-02](40-BI-02-dados-mestres-de-calculo.md), [ST-03](13-ST-03-instalacao.md) |
| 4 | **Medidor trocado sem completar a instalação** | Houve `EG33` sem `EG34`? A conta está lendo o aparelho antigo | [ST-04](14-ST-04-equipamento.md) |
| 5 | **Irregularidade** | Fraude ou defeito, com perícia e recálculo | [PE-01](37-PE-01-fraude-e-defeito.md), [PE-02](38-PE-02-faturado-da-epoca.md) |

**Só depois das cinco a resposta "consumo real" fica de pé.**

---

## O que muda em cada saída

| Se a causa for | O cliente recebe | Quem executa |
|---|---|---|
| Leitura | Refaturamento com a leitura corrigida | `DM` e `BILL` |
| Anomalia liberada errada | Estorno e novo faturamento | `BILL` |
| Tarifa | Correção de cadastro e refaturamento do período | dados mestres e `BILL` |
| Instalação incompleta | Correção técnica e refaturamento | `DM` |
| Irregularidade | **Cobrança adicional**, com memória de cálculo | `PE` |
| Consumo real | Explicação, e possivelmente parcelamento | `FI-CA` |

**Repare na quinta linha.** É a única em que o cliente **paga mais** depois de
reclamar, e é por isso que a classificação entre fraude e defeito é a decisão
mais delicada de todo o fluxo. Ver [PE-01](37-PE-01-fraude-e-defeito.md).

---

## O erro que todo mundo comete

**Abrir fiscalização como primeiro passo.**

Fiscalização é nota de serviço: custa deslocamento, e se a causa era leitura
estimada, gastou-se uma equipe para descobrir algo que estava na tela. **A
ordem existe para não mandar gente à rua antes de olhar o sistema.**

O inverso também erra: fechar como consumo real sem ter olhado as quatro
primeiras causas.

---

## Na prática

**Peça o histórico antes de qualquer coisa.** Consumo alto isolado num
histórico estável aponta para leitura ou instalação. Consumo alto crescendo há
meses aponta para consumo real ou irregularidade antiga.

É o mesmo raciocínio que o sistema faz sozinho na validação, com o **consumo
esperado**. Ver [DM-05](36-DM-05-ciclo-da-leitura.md).

---

## No sistema

Esta nota **não tem transação própria**: ela roteia para as áreas que têm. Os
dois códigos que o atendimento precisa reconhecer no histórico do equipamento
são estes:

| Transação | O que significa ver isto no histórico |
|---|---|
| `EG33` | Instalação **técnica**. Sozinha, o aparelho não fatura |
| `EG34` | A parte **com efeito no cálculo**. É ela que liga o aparelho à tarifa |

**Ver `EG33` sem `EG34` é a causa 4 confirmada.**

---

## Se sobrar uma coisa

Olhe o sistema inteiro antes de mandar alguém à rua.

---

## Recall

1. Nomeie as cinco causas de conta alta, na ordem de investigação.
2. Qual o critério que ordena essa lista?
3. Em qual das saídas o cliente paga mais depois de reclamar?
4. Qual par de transações, se incompleto, faz a conta usar o medidor antigo?
5. Onde se verifica se a leitura foi estimada?
6. O que separa a causa "tarifa errada" da causa "irregularidade" quanto a quem executa a correção?
7. Um atendente abre fiscalização como primeiro passo. Cite o desperdício.
8. Um cliente reclama de conta alta e o histórico está estável. Cite as duas causas mais prováveis.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#cs-07)  ·  responda tudo antes de abrir.
