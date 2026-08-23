# FC-08: Débito automático e Pix Automático
> A mesma ideia com dois trilhos: uma adesão vinculada à conta contrato
> autoriza a cobrança recorrente. Um trilho é arquivo bancário, o outro é API.

**Onde entra:** a forma de pagamento que mais reduz inadimplência, e a que mais depende de cadastro.
**Antes disto:** [FC-06](49-FC-06-o-registro-da-cobranca.md), [MD-05](10-MD-05-conta-contrato.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## O cadastro nasce em dois lugares

| Origem | Como funciona |
|---|---|
| **Pelo banco** | O cliente autoriza no app ou na agência, e o banco valida agência, conta e titularidade no ato. A empresa recebe o retorno com a adesão já confirmada |
| **Pela empresa**, site ou atendimento | O cliente informa os dados no canal da empresa, que não consegue validá-los sozinha. É preciso enviar arquivo de cadastro ao banco e aguardar aceite ou rejeição |

**Só após o aceite a conta contrato fica apta.** Alguns bancos aceitam as duas
origens, outros só a adesão feita no próprio banco.

**A consequência para o atendimento:** quando o cadastro nasce na empresa, o
cliente não está aderido no momento em que desliga o telefone. Existe uma
viagem de ida e volta ao banco antes disso, e ela pode voltar rejeitada.

---

## O ciclo de cobrança

```
1 FATURA ELEGÍVEL ──▶ 2 ORDEM DE PAGAMENTO ──▶ 3 BANCO ──▶ 4 RETORNO
  o FI-CA seleciona     agrupa os itens por      tenta        traz pagos e
  contas com adesão     conta bancária e data    debitar no   não pagos; o SAP
  ativa e separa as     de vencimento. É ela     vencimento.  compensa as pagas
  faturas em aberto     que origina o arquivo    Sem saldo,   e mantém as demais
                        de débito                volta        em aberto
                                                 rejeitado
```

**Pontos de atenção que o material lista:** prazo mínimo entre envio e
vencimento definido por cada banco, tratamento de rejeição para não gerar
cobrança indevida, cancelamento da adesão quando o cliente desiste ou troca de
conta, e conciliação do enviado contra o que voltou pago.

---

## Pix Automático: mesma ideia, outro trilho

| | **Débito automático** | **Pix Automático** |
|---|---|---|
| Onde o cliente autoriza | Banco ou empresa | App do banco, sempre |
| Como a cobrança vai | Arquivo de débito | Enviada ao arranjo do Pix |
| Como a confirmação volta | Retorno CNAB | API, tempo quase real |
| Cliente pode pausar sozinho | Depende | Sim, no app, a qualquer momento |
| No FI-CA | Adesão é dado de cadastro da conta contrato | Igual |

*"O conceito é o mesmo: uma adesão ativa vinculada à conta contrato autoriza a
cobrança recorrente sem ação do cliente a cada mês. Muda o trilho."*

---

## O erro que todo mundo comete

**Cadastrar o débito automático com o número errado da fatura.**

O dado é **sempre a conta contrato**, e ela vem impressa na própria fatura,
destacada como o número para débito automático. **Qualquer outro número serve
para outra coisa**: referência, número do documento, instalação.

O que acontece com o dado errado, nas palavras do material: *"faz o cadastro
voltar rejeitado ou vincular o débito à conta de outro cliente, gerando cobrança
indevida e retrabalho de cancelamento."*

**Vincular ao cliente errado é o pior desfecho possível**, porque ninguém
percebe até o outro cliente reclamar de um débito que não é dele.

A orientação literal ao atendimento: *"pedir sempre o número destacado na
fatura como conta contrato, conferindo os dígitos antes de enviar o arquivo de
cadastro ao banco."*

---

## O cartão, terceiro trilho

O cartão de crédito e débito no site e no app segue a mesma lógica de API do
Pix Automático: autorização pelo gateway ou adquirente, confirmação individual
sem arquivo, acúmulo em lote e compensação.

**A diferença dele é o dinheiro:** há taxa da adquirente, o repasse financeiro
cai em data diferente do pagamento, e existe estorno depois da compensação, o
chargeback. Nenhum outro meio tem isso.

---

## No sistema

**Não há transação desta nota.** A Aula 05 apresentou o FI-CA inteiro em 24
slides e **não mostrou um único código**, nem de transação nem de tabela.

Isso não é lacuna de captura, é característica da aula. **As transações de
FI-CA são pergunta para o instrutor**, e a [`_BANCADA.md`](_BANCADA.md) tem a
seção de FI-CA montada a partir do pôster de tabelas.

---

## Se sobrar uma coisa

O dado do débito automático é sempre a conta contrato, e cadastrar outro número
pode debitar do cliente errado.

---

## Recall

1. Nomeie as duas origens possíveis do cadastro de débito automático.
2. O que a origem pelo banco valida que a origem pela empresa não valida?
3. Quando a conta contrato fica apta ao débito automático no cadastro feito pela empresa?
4. Descreva as quatro etapas do ciclo de cobrança do débito automático.
5. Qual etapa dá origem ao arquivo de débito enviado ao banco?
6. O que separa o Pix Automático do débito automático tradicional?
7. Onde o cliente autoriza o Pix Automático?
8. Qual é o dado de cadastro correto do débito automático?
9. Cite o que acontece quando se cadastra o número errado.
10. O cartão tem uma característica financeira que nenhum outro meio tem. Cite qual.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#fc-08)  ·  responda tudo antes de abrir.
