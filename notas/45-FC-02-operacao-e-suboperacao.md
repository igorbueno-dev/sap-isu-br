# FC-02: O documento do FI-CA, operação e suboperação
> Cada linha da fatura vira um documento com partidas, e um par de códigos
> decide o que aquele valor significa: para onde vai na contabilidade, em que
> ordem é baixado e se rende juros.

**Onde entra:** a unidade elementar do FI-CA. Tudo daqui para frente age sobre isto.
**Antes disto:** [FC-01](44-FC-01-arrecadacao-e-cobranca.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## A cadeia

```
ITEM DA FATURA ──▶ DOCUMENTO NO FI-CA ──▶ OPERAÇÃO E SUBOPERAÇÃO
consumo, tarifa,   cabeçalho mais         o par que diz o que
taxa ou serviço    partidas individuais   aquele valor significa
```

---

## O que o par decide

**São quatro coisas, e três delas não têm nada a ver com o nome do item.**

| O que o par define | Texto do material |
|---|---|
| **Operação principal** | *"Diz a natureza do valor: fatura de fornecimento, pagamento, juros, multa, parcelamento ou devolução"* |
| **Suboperação** | *"Detalha o item dentro daquela natureza: consumo, tarifa, taxa de iluminação, tributo ou serviço"* |
| **Conta contábil** | *"O par determina a conta e a divisão contábil no razão"* |
| **Comportamento** | *"Define regras de compensação, prioridade na baixa, incidência de juros e o que aparece na fatura"* |

*"Na prática: o mesmo valor cobrado muda completamente de tratamento quando muda
a operação ou a suboperação."*

---

## O exemplo do material

Fatura de energia de **R$ 300,00**:

| Item da fatura | Operação | Suboperação | Valor |
|---|---|---|---|
| Consumo de energia elétrica | 0100 Consumo periódica | 0100 Consumo | R$ 240,00 |
| Tarifa de disponibilidade | 0100 Consumo periódica | 0200 Tarifa | R$ 25,00 |
| Contribuição de iluminação pública | 0100 Consumo periódica | 0300 Tributo/COSIP | R$ 20,00 |
| Juros e multa da fatura anterior | 0040 Juros Fat. 02/2026 | 0020 Juros e multa | R$ 15,00 |

**Repare nas três primeiras linhas:** mesma operação, suboperações diferentes.
E na quarta: **operação diferente**, porque juros não é fornecimento.

**Um único documento, quatro partidas.**

---

## Para que isso serve, em três lugares

| Onde | Consequência |
|---|---|
| **Na cobrança** | Pagamento parcial **baixa na ordem que a operação define**, não na ordem da fatura |
| **Na contabilidade** | Cada operação leva o valor para uma conta contábil diferente na transferência ao FI |
| **No atendimento** | É pela operação que se identifica se a linha é consumo, tributo ou acréscimo por atraso |

---

## O erro que todo mundo comete

**Ler a fatura pelo nome do item em vez de pela operação.**

Duas linhas com nomes parecidos podem ter operações diferentes, e aí tudo muda:
vão para contas contábeis diferentes, baixam em ordens diferentes e uma rende
juros enquanto a outra não.

**O caso clássico é o pagamento parcial.** O cliente paga metade e reclama que
o sistema baixou "a linha errada". Não baixou: seguiu a prioridade da operação,
que é parametrização, não escolha do cliente.

---

## Na prática

Quando um cliente contesta **uma linha específica** da conta, a pergunta útil
não é "qual o valor", é **qual a operação**. Ela diz se aquilo é fornecimento,
tributo repassado a terceiro ou acréscimo por atraso, e isso decide quem pode
cancelar o quê.

---

## No sistema

**Não há transação desta nota.** A Aula 05 apresentou o FI-CA inteiro em 24
slides e **não mostrou um único código**, nem de transação nem de tabela.

Isso não é lacuna de captura, é característica da aula. **As transações de
FI-CA são pergunta para o instrutor**, e a [`_BANCADA.md`](_BANCADA.md) tem a
seção de FI-CA montada a partir do pôster de tabelas.

---

## Se sobrar uma coisa

O nome do item na fatura é para o cliente. O par operação e suboperação é para
o sistema, e é ele que decide o destino do valor.

---

## Recall

1. Descreva a cadeia que vai do item da fatura ao par de códigos.
2. Nomeie as quatro coisas que a operação e a suboperação definem.
3. Que pergunta a operação principal responde?
4. Que pergunta a suboperação responde?
5. Numa fatura com consumo, tarifa de disponibilidade e iluminação pública, quantas operações diferentes existem?
6. Cite o que faz a linha de juros ter operação diferente das outras três.
7. O que decide a ordem de baixa num pagamento parcial?
8. Um cliente pagou metade e diz que o sistema baixou a linha errada. Cite o que explicar.
9. Um cliente contesta uma linha da conta. Cite a pergunta mais útil antes de responder.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#fc-02)  ·  responda tudo antes de abrir.
