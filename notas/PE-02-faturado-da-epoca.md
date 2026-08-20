# PE-02: Faturado da época x fatura revista
> O cálculo que transforma uma irregularidade em valor a cobrar. Duas contas
> do mesmo período, e a diferença entre elas é a receita recuperada.

**Onde entra:** fecha o Bloco 3, e fecha o Serviço de Campo.
**Antes disto:** [PE-01-fraude-e-defeito](PE-01-fraude-e-defeito.md)

---

## A ideia central, em uma linha

A definição: **a comparação entre o valor cobrado na época e o valor
recalculado corretamente.**

| | O que é |
|---|---|
| **Faturado da época** | O que o cliente **realmente pagou**, com o medidor errado |
| **Fatura revista** | O que ele **deveria ter pago**, se a medição estivesse certa |
| **Diferença apurada** | A conta a cobrar, ou a devolver |

**Não se apaga a fatura antiga.** Ela continua existindo, e a revisão é um
documento novo ao lado dela. Isso importa: o histórico precisa mostrar as duas
versões para a cobrança se sustentar.

---

## Os cinco insumos do cálculo

| Insumo | Para que serve |
|---|---|
| **Histórico de consumo** | A base de comparação. Como esse cliente consumia antes |
| **Período da irregularidade** | **De quando até quando** recalcular |
| **Critérios regulatórios** | A regra que o regulador obriga a usar |
| **Energia estimada** | Quanto ele deveria ter consumido |
| **Energia faturada** | Quanto foi cobrado de fato |

**O período é o insumo mais disputado.** Ele decide o tamanho da conta e
raramente é óbvio: ninguém sabe o dia exato em que o lacre foi violado. Por
isso existem critérios regulatórios, limitando até onde se pode voltar no tempo.

> **Critério regulatório não é sugestão.** Ele impede que a concessionária
> escolha o período que dá mais dinheiro. Fora do critério, a cobrança volta.

---

## A diferença apurada tem três saídas

| Saída | Quando |
|---|---|
| **Receita recuperada** | O caso normal. O cliente pagou menos e deve a diferença |
| **Débito adicional** | Valores acessórios além do consumo |
| **Crédito ao cliente** (quando aplicável) | **O recálculo deu a favor dele** |

**A terceira saída é a que dá credibilidade à área.** Um defeito de medidor
pode fazer o aparelho contar **a mais**. Quando isso acontece, a revisão gera
crédito. Uma área de Perdas que só produz débito está calibrada errado.

---

## A memória de cálculo

Quatro itens: **fórmulas utilizadas**, **consumos considerados**, **períodos
analisados** e **critérios regulatórios**. É o documento que explica a conta
linha por linha, e não é anexo burocrático: **é a prova**, lida quando o
cliente contesta na ouvidoria, no regulador ou na justiça.

**Regra prática:** se a memória não permite que um terceiro refaça o cálculo e
chegue no mesmo número, a cobrança não se sustenta.

---

## Como isso aparece no sistema

Um caso real de "Documento de defeito", com três meses recalculados.
A **tabela de cálculo** traz uma linha por mês e por parcela da tarifa: o
período (mês, classificação, dias), a especificação (**Consumo TE** e **Consumo
TUSD**), o consumo em três colunas (faturado, revisto, **diferença**) e os
valores já com imposto. O **resumo** fecha por mês, com ICMS separado por
alíquota e PIS/COFINS à parte.

**Duas leituras que essa tela ensina:**

1. **O recálculo é por parcela da tarifa, não por total.** TE e TUSD são
   recalculadas separadamente porque têm alíquotas e destinos diferentes
2. **O imposto entra no cálculo, e separado por alíquota.** Perdas não é só
   energia: é energia mais tributo, e o tributo tem regra própria

> **Vocabulário do setor elétrico brasileiro:** `TE` é Tarifa de Energia e
> `TUSD` é Tarifa de Uso do Sistema de Distribuição.

---

## A transação

**`ISUBR_MANAGE_PROCESS`** é a transação standard citada: gerenciamento dos
processos, tratamento das irregularidades e execução dos cálculos. O prefixo
`ISUBR` indica **localização Brasil**, o que faz sentido: os critérios
regulatórios de recálculo são nacionais, e o SAP entrega a versão brasileira
pronta em vez de deixar cada projeto construir a sua.

---

## Recall

1. O que é faturado da época, e o que é fatura revista?
2. A fatura antiga é cancelada no processo de revisão?
3. Qual é o insumo mais disputado do cálculo, e o que limita a disputa?
4. Quais são as três saídas da diferença apurada, e por que a terceira importa?
5. O que precisa ser verdade sobre a memória de cálculo para a cobrança se sustentar?
6. Por que o recálculo separa TE e TUSD, e o que o prefixo `ISUBR` indica?

> **Gabarito:** [`_GABARITOS.md`](_GABARITOS.md#pe-02)  ·  responda tudo antes de abrir.

---

## Ligações

[PE-01-fraude-e-defeito](PE-01-fraude-e-defeito.md) · [SV-01-servico-de-campo](SV-01-servico-de-campo.md) · [DM-02-leituras-e-registradores](DM-02-leituras-e-registradores.md) · [WM-02-workflow-e-integracoes](WM-02-workflow-e-integracoes.md)
