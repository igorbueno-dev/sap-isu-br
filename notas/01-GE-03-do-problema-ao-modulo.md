# GE-03: Do problema ao módulo
> Cinco parágrafos de negócio, e o mapa de qual pedaço do CCS resolve cada um.
> Leia antes de qualquer sigla: é o "por quê" de todas elas.

**Onde entra:** é o "por quê" de tudo. Anterior até ao [GE-01-o-que-e-is-u-ccs](02-GE-01-o-que-e-is-u-ccs.md).
**Origem:** raciocínio meu, e de propósito. **Não afirma nada sobre o SAP**,
descreve o negócio que o produto atende. A única parte que toca o produto é a
tabela final, que mapeia cada problema no módulo correspondente.

---

## 1. O produto é invisível e a venda é ao contrário

**Uma concessionária de energia entrega um produto invisível pelo ar e cobra
por ele depois.** Não tem loja, não tem pedido, não tem vendedor. Tem fio,
poste, medidor e uma conta que chega todo mês.

> **Concessionária** é a empresa que recebeu do poder público a concessão para
> distribuir energia numa região. É o nome que o material inteiro usa para ela,
> e daqui para a frente é sempre este.

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

## O mapa: cada parágrafo vira um pedaço do CCS

**Esta tabela é o produto da nota.** Os cinco parágrafos acima são o sistema
inteiro; tudo o que vem depois é o nome que a SAP deu a cada pedaço deles.

| O parágrafo | Vira, no SAP |
|---|---|
| Onde está ligado | Dados mestres técnicos, [ST-01-objeto-de-ligacao](11-ST-01-objeto-de-ligacao.md) a [ST-04-equipamento](14-ST-04-equipamento.md) |
| Quem é e quem paga | Dados mestres comerciais, [MD-03-parceiro-de-negocios](08-MD-03-parceiro-de-negocios.md) a [MD-06-contrato](15-MD-06-contrato.md) |
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

## Se sobrar uma coisa

O sistema existe para responder três perguntas: onde está ligado, quanto consumiu, por quanto é cobrado.

---

## Recall

1. Quais são as três perguntas que o sistema inteiro existe para responder?
2. O que separa a venda de energia de uma venda comum?
3. Uma concessionária corta o fornecimento de quem já havia pagado. Cite o que torna esse erro mais caro que um erro de faturamento.
4. Qual pedaço do CCS resolve o problema de receber o dinheiro?

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#ge-03)  ·  responda tudo antes de abrir.
