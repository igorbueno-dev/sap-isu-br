# BI-05: O que precisa existir para faturar, e o que fazer quando não faturou
> Oito coisas precisam estar no lugar para uma instalação faturar. O
> diagnóstico da fatura que não saiu é essa mesma lista, percorrida de trás
> para frente.

**Onde entra:** fecha o bloco de faturamento com o uso prático dele.
**Antes disto:** [BI-01](39-BI-01-calculo-e-faturamento.md), [BI-02](40-BI-02-dados-mestres-de-calculo.md), [DM-05](36-DM-05-ciclo-da-leitura.md)
**Origem:** **misto.** Cada item da lista vem de uma nota com fonte no
material. **A montagem em checklist e em árvore de decisão é minha**, e vinha
da bancada de consulta, onde ninguém estudava.

---

## Os oito pré-requisitos

```
[ ] 1  INSTALAÇÃO existe e está ativa
       └─ com categoria tarifária preenchida

[ ] 2  CONTRATO ativo cobrindo o período que se quer faturar
       └─ atenção às datas de início e de fim

[ ] 3  EQUIPAMENTO instalado TECNICAMENTE no local de instalação

[ ] 4  EQUIPAMENTO instalado PARA FATURAMENTO
       └─ relação registrador e tarifa configurada
       └─ ESTE É O ITEM QUE MAIS FALTA

[ ] 5  TARIFA vigente na data do período
       └─ atenção a reajuste que virou no meio do período

[ ] 6  FATOS obrigatórios preenchidos
       └─ os valores que a tarifa exige, por exemplo demanda contratada

[ ] 7  RESULTADO DE LEITURA válido para o período
       └─ ou uma estimativa gerada
       └─ leitura implausível NÃO conta como válida

[ ] 8  Período ainda não faturado
       └─ não existe documento emitido para as mesmas datas
```

**Repare que o cálculo não está na lista.** Os oito são condições de entrada.
Quando todas existem, o cálculo roda; quando uma falta, ele nem começa.

---

## A árvore de decisão

É a mesma lista de cabeça para baixo. **Comece pela leitura**, porque é a causa
mais frequente e a mais barata de verificar.

```
A fatura do contrato não saiu
        │
        ├─▶ Existe LEITURA válida para o período?
        │      NÃO ──▶ a ordem foi gerada? o leiturista passou? a leitura
        │               ficou implausível?  vai para MEDIÇÃO
        │      SIM ▼
        ├─▶ Existe TARIFA vigente na data do período?
        │      NÃO ──▶ problema de cadastro de tarifa. Costuma afetar
        │               MUITOS contratos ao mesmo tempo.  ESCALE
        │      SIM ▼
        ├─▶ O EQUIPAMENTO está instalado PARA FATURAMENTO?
        │      NÃO ──▶ falta a relação registrador e tarifa
        │      SIM ▼
        ├─▶ O CONTRATO estava ativo durante o período?
        │      NÃO ──▶ Move-In ou Move-Out com data errada
        │      SIM ▼
        └─▶ Faltam FATOS obrigatórios, ou já existe documento emitido
            para as mesmas datas.  Leia o log em `SLG1`
```

**A segunda pergunta é a que muda o encaminhamento.** Tarifa errada quase nunca
atinge um cliente só. Se a resposta for não, pare de investigar o caso
individual: você tem um problema de massa.

---

## Onde cada ramo termina

| Ramo | Área | Nota |
|---|---|---|
| Leitura ausente ou implausível | **DM** | [DM-05](36-DM-05-ciclo-da-leitura.md) |
| Tarifa não vigente | **BILL** | [BI-02](40-BI-02-dados-mestres-de-calculo.md) |
| Instalado tecnicamente, não para faturamento | **DM** | [ST-04](14-ST-04-equipamento.md) |
| Contrato com data errada | **CS + CRM** | [MD-07](16-MD-07-move-in-move-out.md) |
| Fatos ou documento duplicado | **BILL** | [BI-01](39-BI-01-calculo-e-faturamento.md) |

**Quatro dos cinco ramos terminam fora do faturamento.** É por isso que esta
nota fecha o bloco em vez de abrir: ela só faz sentido depois que as outras
áreas já têm nome.

---

## O erro que todo mundo comete

**Começar o diagnóstico pelo cálculo.**

A conta que não saiu quase nunca é falha do motor de cálculo. É dado mestre
faltando, e a lista dos oito diz exatamente qual. Abrir o log do cálculo antes
de conferir os pré-requisitos é gastar meia hora para descobrir que o
equipamento nunca foi instalado para faturamento.

**O item 4 é o que mais falta.** Alguém rodou `EG33`, viu o equipamento
aparecer na tela e considerou o trabalho feito. Sem `EG34` não existe relação
registrador e tarifa, e sem ela não há o que calcular.

---

## Na prática

**Duas técnicas resolvem a maior parte dos casos, e nenhuma delas é técnica.**

**Compare um caso que funciona com um que falha.** Dois clientes parecidos, um
que faturou e um que não, campo por campo. A diferença é a causa.

**Agrupe os erros por mensagem antes de abrir qualquer caso.** Se 2.400 de
3.100 erros são a mesma mensagem, você tem um problema, não 2.400. Isso muda a
prioridade e muda quem precisa ser avisado.

---

## No sistema

| Código | O que é | Onde entra no diagnóstico |
|---|---|---|
| `EG33` | Instalação **técnica** do equipamento | Item 3 da lista |
| `EG34` | Instalação **para cálculo**, com a relação registrador e tarifa | **Item 4, o que mais falta** |
| `SLG1` | Log de aplicação | Último ramo, quando os oito parecem certos |

As transações de cálculo e de faturamento estão na
[BI-01](39-BI-01-calculo-e-faturamento.md), e as de leitura na
[DM-05](36-DM-05-ciclo-da-leitura.md).

---

## Se sobrar uma coisa

Fatura que não saiu é um dos oito pré-requisitos faltando, e o mais provável é
o quarto.

---

## Recall

1. Nomeie os oito pré-requisitos de faturamento, na ordem.
2. Qual dos oito é o que mais falta na prática?
3. Qual transação faz a instalação técnica do equipamento?
4. Qual transação faz a instalação para cálculo?
5. Qual transação mostra o log de aplicação?
6. Descreva a árvore de diagnóstico da fatura que não saiu, do primeiro ao último ramo.
7. Por qual pergunta o diagnóstico começa?
8. Cite o que justifica essa ordem.
9. Qual resposta da árvore muda o encaminhamento de caso individual para problema de massa?
10. O que separa uma leitura implausível de uma leitura ausente, para efeito desta lista?
11. Uma fatura não saiu e o equipamento aparece instalado na tela. Cite a primeira hipótese.
12. Cite as duas técnicas de diagnóstico que resolvem a maior parte dos casos.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#bi-05)  ·  responda tudo antes de abrir.
