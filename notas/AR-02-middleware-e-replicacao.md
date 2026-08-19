# AR-02: Middleware e replicação
> Como um dado criado no CRM aparece no IS-U. Um caminho de cinco paradas, e
> as transações para olhar cada uma quando ele trava.

**Onde entra:** o mecanismo que a nota anterior deixou como caixa preta.
**Antes disto:** [AR-01-landscape-e-camadas](AR-01-landscape-e-camadas.md)
**Depois disto:** [AR-03-objetos-replicados](AR-03-objetos-replicados.md)

---

## O problema que o middleware resolve

CRM e IS-U são sistemas separados, cada um com sua base. Mas o **mesmo
cliente** precisa existir nos dois: no CRM para ser atendido, no IS-U para ser
faturado.

Copiar na mão é impossível. **O middleware é o carteiro**, e ele é assíncrono:
o dado não aparece do outro lado no mesmo instante, ele entra numa fila.

Essa palavra, **fila**, é a origem de quase todo problema de integração.

---

## As três siglas da faixa

| Sigla | O que é |
|---|---|
| **BDoc** | *Business Document*. O envelope onde o dado viaja |
| **qRFC** | *queued Remote Function Call*. A fila, que garante ordem |
| **ALE** | *Application Link Enabling*. O mecanismo clássico SAP de troca entre sistemas |

---

## O caminho, parada por parada

```
CRM          SMW01        SMQ1        RFC          IS-U        BUT000
Criação  →   BDoc     →   Fila    →   Comuni-  →   Recebi-  →  BP
do BP        gerado       qRFC        cação        mento       criado
```

O exemplo clássico é a criação de um Parceiro de Negócios.

**Cada parada tem uma transação para olhar:**

| Parada | Transação | Para quê |
|---|---|---|
| O envelope | `SMW01` | Ver os BDocs, e se algum falhou |
| A fila de entrada | `SMQ1` | Ver o que está parado chegando |
| A fila de saída | `SMQ2` | Ver o que está parado saindo |
| A conexão | `SM58` | Monitor de RFC, ver chamada travada |
| O middleware | `R3AM1` | Monitoramento geral da replicação |

---

## Carga inicial versus fluxo do dia

Duas coisas diferentes que usam o mesmo encanamento:

| Situação | Transação |
|---|---|
| **Carga inicial**, trazer tudo de uma vez na implantação | `R3AS` |
| **Repetição de carga**, quando algo não veio | `R3AR2` |
| **Sites e conexões**, quem fala com quem | `SMOEAC`, `SMOEACPR`, `SMOEACLINK` |

E duas de sistema, que servem para qualquer problema, não só middleware:

| Transação | Para quê |
|---|---|
| `SM21` | Log do sistema |
| `ST22` | Dump, o erro de programa |

---

## A pegadinha mais útil desta nota

> **"Criei o cliente no CRM e ele não aparece no IS-U."**
>
> Isso quase nunca é bug. É fila. A ordem de investigação é:
>
> 1. `SMW01`, o BDoc foi gerado? Se não, o problema é no CRM
> 2. `SMQ1` e `SMQ2`, está parado numa fila?
> 3. `SM58`, a conexão caiu?
> 4. `ST22`, deu dump no destino?
>
> **Quatro transações resolvem a maioria dos chamados de integração.** Saber
> essa sequência de cor é o tipo de coisa que separa júnior de júnior.

---

## Recall

1. Por que existe middleware entre CRM e IS-U?
2. O que significam BDoc e qRFC?
3. Descreva o caminho de replicação de um BP, do CRM ao IS-U.
4. Um cliente criado no CRM não chegou ao IS-U. Qual sua sequência de
   investigação, com as transações?
5. Qual a diferença entre `R3AS` e `R3AR2`?

> **Gabarito:** [`_GABARITOS.md`](_GABARITOS.md#ar-02)  ·  responda tudo antes de abrir.

---

## Ligações

[AR-01-landscape-e-camadas](AR-01-landscape-e-camadas.md) · [AR-03-objetos-replicados](AR-03-objetos-replicados.md) · [02-BANCADA](../referencia/02-BANCADA.md)
