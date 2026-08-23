# FC-06: O registro da cobrança, e por que ele decide tudo
> Cobrança registrada baixa sozinha. Cobrança não registrada precisa de gente.
> Essa única diferença atravessa boleto, Pix e o custo da operação.

**Onde entra:** o que separa conciliação automática de esclarecimento manual.
**Antes disto:** [FC-01](44-FC-01-arrecadacao-e-cobranca.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## As seis formas de pagamento

| Forma | O que é |
|---|---|
| **Código de barras** | Leitura da linha digitável em bancos, lotéricas e apps |
| **Boleto bancário** | **Título registrado**, com retorno bancário que confirma o pagamento |
| **Pix** | Instantâneo por QR Code ou chave, com baixa quase imediata |
| **Pix Automático** | Cobrança recorrente autorizada uma vez no app do banco, confirmada por API |
| **Débito automático** | Débito em conta no vencimento, por troca de arquivos com o banco |
| **Cartão de crédito ou débito** | Avulso ou recorrente, liquidado pela adquirente |

---

## O par que se repete duas vezes

**O material monta a mesma oposição em dois lugares diferentes, e é essa
simetria que vale decorar:**

| | **Sem registro** | **Com registro** |
|---|---|---|
| No papel | **Código de barras** | **Boleto registrado** |
| No digital | **Pix estático**, o PIX PURO | **Pix dinâmico** |
| O que carrega | Só quem recebe | Valor, vencimento e identificador da fatura |
| Quem paga decide | O valor | Nada, já vem tudo |
| Conciliação | Precisa ser tratada depois | **Automática** |
| Duplicidade | Possível | **Bloqueada** |

*"O registro da cobrança é o que garante a conciliação: no boleto, o título
registrado; no Pix, o QR dinâmico com identificador da fatura."*

**O Pix dinâmico é o boleto registrado do mundo digital.** O material declara
a equivalência com essas palavras.

---

## O que o registro compra

Do slide do boleto registrado, quatro ganhos:

| Ganho | Como funciona |
|---|---|
| **Evita pagamento em duplicidade** | O banco dá baixa no título ao quitá-lo e **recusa a segunda tentativa** |
| **Bloqueia erro de digitação** | O título precisa existir no banco: número errado simplesmente não é aceito |
| **Controla valor e vencimento** | O banco confere contra o registrado, aplicando desconto, juros e multa combinados |
| **Conciliação automática** | O retorno traz o nosso número, que liga o pagamento à conta contrato |

---

## E o que ele custa

**A tarifa de arrecadação se forma de dois jeitos opostos**, e isso é decisão
de negócio, não detalhe técnico:

| | **Código de barras** | **Boleto registrado** |
|---|---|---|
| Quem cobra | **Quem recebeu o pagamento**, seja qual for o canal | O banco do convênio |
| Quando incide | No pagamento | **No registro**, antes de o cliente pagar |
| Valor | **Varia por canal**: agência, autoatendimento, internet banking, lotérica | Pré-acordado por faixa de volume |
| Previsibilidade | **Só se sabe depois**, quando o arquivo de retorno informa por onde entrou | Previsível, independe do canal |

---

## O erro que todo mundo comete

**Tratar Pix como sinônimo de baixa automática.**

Pix é rápido, e rapidez não é identificação. O **Pix estático** chega quase
instantâneo e **sem saber a que fatura pertence**: alguém vai ter que descobrir
depois, exatamente como no código de barras.

Prometer ao cliente que "pagando por Pix cai na hora" é meia verdade. Cai na
hora **na conta da empresa**; na conta contrato dele, depende de a cobrança ter
sido registrada.

---

## Na prática

Pagamentos por **Pix, Pix Automático e cartão chegam por API**, não por
arquivo. O provedor notifica cada confirmação quase em tempo real, o SAP acumula
e monta o lote.

Isso muda o relógio do problema: no arquivo, o atraso é de um ciclo diário; na
API, o atraso é de minutos, e quando algo não aparece a suspeita muda de
natureza. Ver [CS-08](24-CS-08-corte-e-religacao.md).

---

## No sistema

**Não há transação desta nota.** A Aula 05 apresentou o FI-CA inteiro em 24
slides e **não mostrou um único código**, nem de transação nem de tabela.

Isso não é lacuna de captura, é característica da aula. **As transações de
FI-CA são pergunta para o instrutor**, e a [`_BANCADA.md`](_BANCADA.md) tem a
seção de FI-CA montada a partir do pôster de tabelas.

---

## Se sobrar uma coisa

O que garante baixa automática não é o canal nem a velocidade: é a cobrança ter
sido registrada.

---

## Recall

1. Nomeie as seis principais formas de pagamento.
2. O que separa o código de barras do boleto registrado?
3. O que separa o Pix estático do Pix dinâmico?
4. A qual meio de pagamento em papel o Pix dinâmico equivale, segundo o material?
5. Nomeie os quatro ganhos do boleto registrado.
6. Como o boleto registrado evita pagamento em duplicidade?
7. Onde incide a tarifa no boleto registrado?
8. O que faz a tarifa do código de barras ser imprevisível?
9. Quais formas de pagamento chegam ao FI-CA por API, e não por arquivo?
10. Um cliente pagou por Pix e o débito continua em aberto. Cite a primeira hipótese.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#fc-06)  ·  responda tudo antes de abrir.
