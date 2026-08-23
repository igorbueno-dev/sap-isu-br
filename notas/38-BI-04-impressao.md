# BI-04: A impressão, do spool ao papel na casa do cliente
> A fatura sai do SAP como spool, vira formulário no SAPscript e atravessa para
> a empreiteira como arquivo. Imprimir também é fora de casa.

**Onde entra:** a última etapa antes do cliente ver a conta.
**Antes disto:** [BI-01](35-BI-01-calculo-e-faturamento.md)

---

## Os dois conceitos de saída

| Termo | O que é |
|---|---|
| **Spool** | A saída para impressão de algum documento SAP |
| **Output Request** | Envia os dados de um spool para um dispositivo de saída específico |

**Spool é o conteúdo, output request é o envio.** Um spool pode gerar vários
envios, e é por isso que reimprimir não recalcula nada.

```
Document ──▶ Spool Request  ──┐
             Spool Data      ─┴──▶ Output Request ──▶ SAP Spool System
             (em TemSe)                                      │
                                                    Host Spool System ──▶ 🖨
```

**`TemSe`** é onde os dados do spool ficam guardados. O nome vem de *temporary
sequential*, e é objeto de Basis, não de IS-U.

---

## SAPscript, quem desenha a conta

*"Funcionalidade para construção de formulários para impressão no SAP"*, com
cinco recursos: **editor** de textos, **formulários e estilos**, **composer**,
**interface de programação** e **tabelas de controle**, todos em volta do banco
de dados.

**A conta de energia que chega na casa do cliente é um formulário SAPscript**,
ou o sucessor dele. O layout, os campos, a posição do código de barras: tudo
sai daqui.

---

## A fronteira, de novo

Assim como a leitura, **a impressão física não é da concessionária**:

```
SAP: calcula ─▶ fatura ─▶ EA40 / EA29 imprime ─▶ transação Z gera TXT
                                                        │
EMPREITEIRA: ◀──────────────────────────────────────────┘
             imprime as faturas e entrega
```

A ponte é um **arquivo TXT gerado por transação `Z`**, ou seja, **código escrito
pelo projeto**, não standard SAP.

---

## O erro que todo mundo comete

**Achar que reimprimir corrige a conta.**

Não corrige. O spool é uma cópia do documento de impressão que já existe. Se o
valor está errado, o problema está no documento, e o caminho é estorno e
refaturamento, não impressão. **Reimprimir só resolve papel perdido.**

---

## Na prática

**Este é o pedaço de Billing que mais encosta em ABAP**, e a semana 3 foi
anunciada como ABAP e rotina de júnior. Formulário, spool e transação `Z` são
exatamente o território onde um analista funcional precisa saber ler código
para conversar com quem escreve.

Se a conta saiu com campo em branco ou layout quebrado, **o defeito quase nunca
está no cálculo**: está no formulário.

---

## Recall

1. Qual a diferença entre spool e output request?
2. O que é o SAPscript, e o que ele produz?
3. Como a fatura chega à empreiteira que imprime?
4. Por que a transação que gera o arquivo começa com `Z`?
5. Uma conta saiu com valor certo e um campo em branco. Onde está o defeito?

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#bi-04)  ·  responda tudo antes de abrir.
