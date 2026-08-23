# AR-02: Middleware e replicação
> Como um dado criado no CRM aparece no IS-U. Um caminho de cinco paradas, e
> as transações para olhar cada uma quando ele trava.

**Onde entra:** o mecanismo que a nota anterior deixou como caixa preta.
**Antes disto:** [AR-01-landscape-e-camadas](26-AR-01-landscape-e-camadas.md)
**Depois disto:** [AR-03-objetos-replicados](28-AR-03-objetos-replicados.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

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

## No sistema

| Transação | O que mostra |
|---|---|
| `SMW01` | O envelope: os BDocs, e se algum falhou |
| `SMQ1` | A fila de entrada, o que está parado chegando |
| `SMQ2` | A fila de saída, o que está parado saindo |
| `SM58` | Monitor de RFC, a chamada travada |
| `SM21` | Log do sistema |
| `ST22` | Dump, o erro de programa no destino |
| `R3AS` | Carga inicial, traz tudo na implantação |
| `R3AR2` | Repetição de carga, para o que não veio |

**A ordem de diagnóstico é a ordem da tabela**: envelope, fila, conexão, dump.

---

## Se sobrar uma coisa

O dado atravessa em envelope e em fila, e o diagnóstico segue essa ordem.

---

## Recall

1. Qual transação mostra os BDocs e se algum falhou?
2. Qual transação mostra a fila de entrada?
3. Qual transação mostra a fila de saída?
4. Qual transação monitora a conexão RFC?
5. Qual transação mostra o log do sistema?
6. Qual transação mostra o dump de programa?
7. Qual transação faz a carga inicial?
8. Qual transação repete a carga do que não veio?
9. O que significa BDoc?
10. O que significa qRFC?
11. Descreva o caminho de replicação de um Parceiro de Negócios, do CRM ao IS-U.
12. O que separa carga inicial de fluxo do dia?
13. Um cliente criado no CRM não chegou ao IS-U. Cite as quatro verificações, na ordem.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#ar-02)  ·  responda tudo antes de abrir.
