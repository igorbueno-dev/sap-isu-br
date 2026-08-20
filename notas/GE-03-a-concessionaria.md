# GE-03: A concessionária em cinco parágrafos
> O problema de negócio que o sistema inteiro existe para resolver.
> Leia antes de qualquer sigla.

**Onde entra:** é o "por quê" de tudo. Anterior até ao [GE-01-o-que-e-is-u-ccs](GE-01-o-que-e-is-u-ccs.md).
**Status:** contexto de negócio, escrito por mim. Material de produto não
cobre isto.
Contexto de negócio não é matéria de prova, é o que faz a matéria fazer sentido.

---

## 1. O produto é invisível e a venda é ao contrário

**Uma distribuidora de energia entrega um produto invisível pelo ar e cobra por
ele depois.** Não tem loja, não tem pedido, não tem vendedor. Tem fio, poste,
medidor e uma conta que chega todo mês.

O cliente **consome primeiro e paga depois**, e ninguém autorizou nada: você
liga o chuveiro e pronto, está comprando.

## 2. Isso cria um problema de contabilidade brutal

Três milhões de clientes. Cada um consumiu uma quantidade diferente, num
período diferente, com um preço que muda por classe de cliente, por horário,
por bandeira, e com impostos calculados de jeitos diferentes.

**Ninguém faz isso à mão.** É preciso um sistema que rode de madrugada e
produza três milhões de contas certas, sozinho.

## 3. As três perguntas que organizam tudo

Para o sistema fazer isso, ele precisa saber três coisas sobre cada cliente:

> **ONDE** ele está ligado na rede.
> **QUANTO** ele consumiu.
> **POR QUANTO** aquilo é cobrado.

**Guarde as três.** Toda a arquitetura do sistema existe para respondê-las.

## 4. Depois de calcular, começa a segunda metade: receber

A conta é emitida, o cliente paga ou não paga. Se não paga, existe uma escada:
aviso, carta, juros, e no fim, **corte**.

Cortar significa mandar uma pessoa de verdade até o poste. Religar também.
**Cada visita custa dinheiro, e cada erro (cortar quem pagou) vira processo
judicial e multa do regulador.**

## 5. Por fim, a empresa precisa se explicar

Para a diretoria, para o acionista e para o órgão regulador. Quanto faturamos,
quanto recebemos, quantos clientes ficaram sem luz e por quanto tempo, quanta
energia entrou na rede e sumiu no caminho.

---

## Por que isto importa

**Estes cinco parágrafos são o sistema inteiro.** Tudo o que vem depois é o
nome que a SAP deu a cada pedaço disto.

| O parágrafo | Vira, no SAP |
|---|---|
| Onde está ligado | Dados mestres técnicos, [ST-01-objeto-de-ligacao](ST-01-objeto-de-ligacao.md) a [ST-04-equipamento](ST-04-equipamento.md) |
| Quem é e quem paga | Dados mestres comerciais, [MD-03-parceiro-de-negocios](MD-03-parceiro-de-negocios.md) a [MD-06-contrato](MD-06-contrato.md) |
| Quanto consumiu | Meter Reading |
| Por quanto | Billing |
| Receber ou cortar | FI-CA e WM |
| Se explicar | BW, fora do CCS |

---

## O erro que todo mundo comete

**Aprender o vocabulário sem aprender o problema.** Dá para decorar que
`EVER` é a tabela de contrato e não fazer ideia de por que contrato existe.

Quem sabe as siglas responde à pergunta fácil. **Quem sabe o problema resolve
o chamado**, porque consegue perguntar "o que essa empresa está tentando
fazer aqui?" quando o sistema faz algo estranho.

---

## Recall

1. Quais são as três perguntas que o sistema inteiro existe para responder?
2. Por que errar no corte é mais caro que errar no faturamento?
3. O que torna a venda de energia diferente de uma venda comum?

> **Gabarito:** [`_GABARITOS.md`](_GABARITOS.md#ge-03)  ·  responda tudo antes de abrir.

---

## Ligações

[GE-01-o-que-e-is-u-ccs](GE-01-o-que-e-is-u-ccs.md) · [GE-04-os-tres-setores](GE-04-os-tres-setores.md)
