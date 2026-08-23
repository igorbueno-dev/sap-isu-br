# FC-05: Bloqueios comerciais
> Três bloqueios diferentes, e eles impedem coisas diferentes. Escolher o
> errado é prometer ao cliente uma proteção que ele não recebeu.

**Onde entra:** é a ferramenta que o atendimento aciona quando o cliente contesta.
**Antes disto:** [FC-03](46-FC-03-status-e-motivo-de-compensacao.md), [CS-08](24-CS-08-corte-e-religacao.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## Os três, e o que cada um impede

| Bloqueio | Impede |
|---|---|
| **De lançamento** | Que **novos documentos** sejam lançados na conta contrato. Nenhum débito ou crédito novo é criado |
| **De compensação** | Que um débito ou crédito seja **compensado**. O crédito não abate o débito e o item não é baixado automaticamente |
| **De advertência** | Que a **régua de dunning** atue: nada de reaviso, negativação, protesto ou corte |

**O de advertência é o que o cliente quer quando liga.** Ele não quer que a
conta pare de existir, quer que parem de cobrar enquanto a contestação é
analisada.

---

## Como o bloqueio é definido

| Atributo | O que é |
|---|---|
| **Abrangência** | Vale para a **conta contrato inteira**, para o **contrato** ou para **um item específico** em aberto |
| **Motivo** | Um código registra a razão: contestação, análise técnica, acordo comercial, cliente em negociação ou determinação judicial |
| **Vigência** | **Sempre com data de início e fim.** Vencido o prazo, o item volta automaticamente ao fluxo normal |
| **Rastreabilidade** | Quem bloqueou, quando e por quê fica registrado |

**A abrangência é a decisão mais fina.** Bloquear a conta inteira porque o
cliente contesta uma linha de R$ 20,00 congela também os R$ 400,00 que ele não
contesta.

---

## O erro que todo mundo comete

**Bloquear sem data de fim.**

O material é explícito: *"bloquear não cancela a dívida nem suspende juros por
si só. Sem prazo de fim, o débito envelhece fora da régua e pode prescrever."*

O bloqueio parece uma solução gentil e é uma bomba-relógio. O débito continua
existindo, os juros continuam correndo em muitos casos, e a cobrança nunca mais
acontece porque ninguém lembra de destravar.

**Bloqueio é adiamento, não perdão.** Se a decisão é não cobrar, o instrumento
é outro: baixa de perdas, com motivo 04 ou 14. Ver
[FC-03](46-FC-03-status-e-motivo-de-compensacao.md).

---

## Na prática

O roteiro do atendimento diante de uma contestação:

1. **Qual bloqueio?** Advertência, quase sempre, se o objetivo é parar a régua
2. **Que abrangência?** O item contestado, não a conta inteira
3. **Que motivo?** Contestação, análise técnica, negociação ou judicial
4. **Até quando?** **Sempre preencher.** É o campo que evita o débito órfão

A `CS-08` cita bloqueio de corte como a verificação que mais resolve. **Este é
o mecanismo por trás dela.**

---

## No sistema

**Não há transação desta nota.** A Aula 05 apresentou o FI-CA inteiro em 24
slides e **não mostrou um único código**, nem de transação nem de tabela.

Isso não é lacuna de captura, é característica da aula. **As transações de
FI-CA são pergunta para o instrutor**, e a [`_BANCADA.md`](_BANCADA.md) tem a
seção de FI-CA montada a partir do pôster de tabelas.

---

## Se sobrar uma coisa

Bloqueio adia, não perdoa, e sem data de fim ele esconde a dívida até ela
prescrever.

---

## Recall

1. Nomeie os três tipos de bloqueio comercial.
2. O que o bloqueio de lançamento impede?
3. O que o bloqueio de compensação impede?
4. O que o bloqueio de advertência impede?
5. Qual dos três o cliente costuma querer quando contesta uma conta?
6. Nomeie os quatro atributos que definem um bloqueio.
7. Quais são os três níveis possíveis de abrangência?
8. Cite o que acontece quando um bloqueio é criado sem data de fim.
9. Bloquear suspende os juros?
10. A decisão é não cobrar mais aquele débito. Cite o instrumento correto.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#fc-05)  ·  responda tudo antes de abrir.
