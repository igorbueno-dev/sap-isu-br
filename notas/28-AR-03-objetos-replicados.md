# AR-03: Objetos replicados
> Quatro objetos existem dos dois lados com nomes e tabelas diferentes. Este
> de-para é o que você consulta quando alguém diz "o dado está divergente".

**Onde entra:** fecha a trilha de arquitetura.
**Antes disto:** [AR-02-middleware-e-replicacao](27-AR-02-middleware-e-replicacao.md)

---

## O de-para

| Objeto | IS-U / CCS | CRM |
|---|---|---|
| **Parceiro de Negócio** | `BUT000` | `BUT000` |
| **Conta Contrato** | `FKKVKP` | `CRMM_BUAG` |
| **Objeto de Ligação** | `EHAUISU` | `COMM_PRODUCT` |
| **Ponto de Entrega (PoD)** | `EUIHEAD` | `IBASE` / `COMM_PRODUCT` |

---

## As três coisas que esta tabela ensina

### 1. O Parceiro de Negócios é o mesmo dos dois lados

`BUT000` no CRM e `BUT000` no IS-U. **Mesmo nome de tabela.** Isso não é
acaso: o Business Partner é um objeto central do SAP, compartilhado, e é por
isso que ele é o primeiro a ser replicado numa implantação.

### 2. Do lado do CRM, coisa física vira produto

Repare que **Objeto de Ligação e Ponto de Entrega viram `COMM_PRODUCT`** no
CRM, a tabela de produtos.

Faz sentido do ponto de vista do CRM: para quem atende, o que existe é um
**produto contratado** naquele endereço. A caixa de luz na parede é
problema do IS-U.

**`IBASE`** é *Installed Base*, a base instalada: o que o cliente tem
instalado. É o conceito de CRM mais próximo do mundo técnico do IS-U.

### 3. Conta Contrato muda de nome, não de função

`FKKVKP` no IS-U vira `CRMM_BUAG` no CRM, de *Business Agreement*. É o mesmo
objeto da [MD-05](10-MD-05-conta-contrato.md), com nome de CRM.

> Se alguém falar em **Business Agreement** numa reunião, está falando de
> Conta Contrato.

---

## O que ainda está aberto

**As duas tabelas vieram do slide de replicação da Aula 02**, não de dedução,
e foram reconferidas no pôster de tabelas IS-U: `EHAUISU` é o *connection
object* e `EUIHEAD` é o *point of delivery*.

Encontrei **duas formas diferentes** para a tabela do Objeto de Ligação,
`EHAU` e `EHAUISU`, e nenhuma das duas fontes era boa o bastante para eu
escolher. **Se você sabe qual é, abra uma issue.**

O mesmo vale para `EUIHEAD` no Ponto de Entrega.

**Perguntar antes de usar.** Tabela errada em documento de projeto é o tipo de
erro que sobrevive por anos.

---

## O que esta nota fecha, e o que não fecha

O **Ponto de Entrega** era lacuna estrutural deste material: aparecia no menu
de dados mestres técnicos e nunca era desenvolvido. Agora ele tem **posição na
arquitetura e tabela**.

Continua faltando:

- As transações de criar, modificar e exibir
- A cardinalidade com Instalação e Local de Consumo
- Se é um dos cinco objetos técnicos padrão, como fontes públicas indicam

---

## No sistema

| Objeto | IS-U | CRM |
|---|---|---|
| Parceiro de Negócio | `BUT000` | `BUT000` |
| Conta Contrato | `FKKVKP` | `CRMM_BUAG` |
| Objeto de Ligação | `EHAUISU` | `COMM_PRODUCT` |
| Ponto de Entrega | `EUIHEAD` | `IBASE` / `COMM_PRODUCT` |

**Nenhuma transação é desta nota.** Ela é um de-para de tabelas; quem investiga
a replicação é a [AR-02](27-AR-02-middleware-e-replicacao.md).

---

## Se sobrar uma coisa

O CRM não copia a estrutura física: para ele, o endereço é um produto.

---

## Recall

1. Qual tabela guarda o Parceiro de Negócios no IS-U?
2. Qual tabela guarda o Parceiro de Negócios no CRM?
3. Qual tabela guarda a Conta Contrato no IS-U?
4. Qual tabela guarda a Conta Contrato no CRM?
5. Qual tabela guarda o Objeto de Ligação no IS-U?
6. Em que objeto o Objeto de Ligação se transforma no CRM?
7. Qual tabela guarda o Ponto de Entrega no IS-U?
8. O que significa `IBASE`?
9. Qual objeto tem o mesmo nome de tabela nos dois sistemas?
10. Alguém fala em Business Agreement. Do que está falando?
11. De onde vêm os nomes de tabela desta nota?

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#ar-03)  ·  responda tudo antes de abrir.
