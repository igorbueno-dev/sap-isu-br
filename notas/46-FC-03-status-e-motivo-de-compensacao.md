# FC-03: Status e motivo de compensação
> Status responde se o débito foi quitado. Motivo responde como. São duas
> perguntas diferentes, e só as duas juntas contam a história.

**Onde entra:** é o vocabulário que o atendimento usa sem saber o nome.
**Antes disto:** [FC-02](45-FC-02-operacao-e-suboperacao.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## As duas perguntas

| Conceito | A pergunta que responde | Texto do material |
|---|---|---|
| **Status de compensação** | *"Este débito foi compensado?"* | *"Indica a situação do item no documento: se ainda está em aberto, se já foi compensado e por qual documento"* |
| **Motivo de compensação** | *"Baixou como?"* | *"Um código que explica por que o item saiu do aberto: pagamento, estorno, baixa de perdas ou encontro de contas"* |

---

## Os cinco motivos principais

| Código | Motivo | O que é |
|---|---|---|
| **01** | **Pagamento** | Entrada de recurso do cliente por boleto, Pix, débito automático ou cartão |
| **05** | **Estorno** | Reverte uma compensação anterior, **devolvendo o item à condição de aberto** |
| **14** | **Perdas massivo** | Baixa de perdas em lote, pelo processo automático de write-off |
| **04** | **Perdas manual** | Baixa de perdas individual, com análise caso a caso |
| **08** | **Encontro de contas** | Abate do débito contra um crédito do próprio cliente, **sem entrada de caixa** |

**Só o 01 é dinheiro entrando.** Os outros quatro tiram o item do aberto sem
que um centavo tenha circulado.

**Repare no 05:** ele é o único que anda para trás. Compensar com motivo 05 não
quita nada, reabre.

---

## O exemplo do material, lido devagar

Fatura de março estornada e reemitida, com R$ 220,00 recebidos:

| Item | Status | Motivo |
|---|---|---|
| Fatura de março, original | Compensado | **05 Estorno** |
| Fatura de março, revisada | Compensado | 01 Pagamento, Pix |
| Fatura de abril | Compensado | 01 Pagamento, Débito Automático |
| Fatura de maio | Compensado | **08 Encontro de contas** |
| Crédito por pagamento em duplicidade | Compensado | **08 Encontro de contas** |
| Juros e multa de março | **Em aberto** | |

**Duas leituras importam aqui.**

A primeira: o cliente pagou R$ 220,00 e **quatro faturas ficaram compensadas**.
Maio foi quitada pelo crédito de duplicidade, sem dinheiro novo.

A segunda: **os juros de março continuam em aberto**, mesmo com março
resolvido. Estornar a fatura principal não carrega os acessórios junto.

---

## O erro que todo mundo comete

**Dizer ao cliente que a fatura foi paga porque o status é "compensado".**

Compensado significa **saiu do aberto**, e há cinco formas de sair. Se o motivo
for 14 ou 04, o item saiu por **baixa de perdas**: a empresa desistiu de
receber, e o cliente não pagou nada.

Responder "consta pago" nesse caso é errado, e num processo é pior que errado.

**A pergunta certa é sempre a segunda:** compensado com qual motivo?

---

## Na prática

O par status e motivo é o que sustenta a resposta a *"eu já paguei"*. E é o que
evita o inverso, que é cobrar de novo um item já quitado.

Quando o cliente apresenta comprovante e o item está em aberto, o caminho é o
ciclo do banco. Ver [CS-08](24-CS-08-corte-e-religacao.md) e
[FC-07](50-FC-07-do-pagamento-a-compensacao.md).

---

## No sistema

**Não há transação desta nota.** A Aula 05 apresentou o FI-CA inteiro em 24
slides e **não mostrou um único código**, nem de transação nem de tabela.

Isso não é lacuna de captura, é característica da aula. **As transações de
FI-CA são pergunta para o instrutor**, e a [`_BANCADA.md`](_BANCADA.md) tem a
seção de FI-CA montada a partir do pôster de tabelas.

---

## Se sobrar uma coisa

Compensado não quer dizer pago. Quer dizer que saiu do aberto, e existem cinco
formas de sair.

---

## Recall

1. Que pergunta o status de compensação responde?
2. Que pergunta o motivo de compensação responde?
3. Nomeie os cinco motivos principais de compensação, com o código de cada um.
4. Qual dos cinco é o único que representa dinheiro entrando?
5. Qual dos cinco devolve o item à condição de aberto?
6. O que separa o motivo 14 do motivo 04?
7. O que o motivo 08 indica sobre a entrada de caixa?
8. Uma fatura consta compensada com motivo 14. Cite o que responder ao cliente.
9. Uma fatura foi estornada e reemitida. Cite o que acontece com os juros da fatura original.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#fc-03)  ·  responda tudo antes de abrir.
