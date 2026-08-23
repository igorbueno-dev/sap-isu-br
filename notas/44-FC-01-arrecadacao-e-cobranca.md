# FC-01: Arrecadação e Cobrança, os dois processos do FI-CA
> Arrecadação faz o dinheiro entrar e encontrar a fatura certa. Cobrança trata
> o que não entrou. Toda a área é essas duas coisas.

**Onde entra:** a quinta e última área da cadeia, e a que fecha o ciclo do dinheiro.
**Antes disto:** [BI-01](39-BI-01-calculo-e-faturamento.md), [MD-05](10-MD-05-conta-contrato.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## Os dois processos, na definição do material

> **Arrecadação:** *"É a entrada do dinheiro: recebimento por lotes, débito
> automático em conta, arquivos de retorno bancário, caixa e agentes
> arrecadadores. Cada pagamento é ligado à fatura correspondente na conta
> contrato, tratando pagamentos parciais, créditos, devoluções e estornos."*

> **Cobrança:** *"É o tratamento do que não foi pago: aviso de débito (dunning),
> juros e multas, parcelamento, corte e religação e envio a assessorias."*

O material fecha assim: *"um garante a entrada do caixa faturado, o outro
recupera o que ficou em aberto."*

---

## As quatro etapas da arrecadação

```
1 RECEBIMENTO  ──▶  2 IDENTIFICAÇÃO  ──▶  3 COMPENSAÇÃO  ──▶  4 COBRANÇA
  pagamentos        o documento de       a fatura é         o que sobra
  entram por        pagamento acha       baixada e o        em aberto entra
  banco, caixa      a fatura correta     saldo do cliente   na régua
  e agentes                              é atualizado
```

**A etapa 2 é onde tudo pode dar errado.** O dinheiro entrou, e agora o sistema
precisa descobrir de quem é e a que fatura pertence. É essa pergunta que
organiza metade do material desta área.

**A etapa 4 não é fim de fluxo, é entrada de outro.** O que não compensou vira
insumo da cobrança.

---

## Por que a Conta Contrato é o dado mestre mais importante daqui

O material lista quatro razões, e nenhuma delas é sobre cadastro:

| Razão | O que significa |
|---|---|
| **Ponto de encontro do dinheiro** | Fatura, pagamento, juros e parcelamento **nascem e são compensados nela** |
| **Base do saldo do cliente** | O que está em aberto, vencido ou pago é sempre lido por ela |
| **Governa a cobrança** | Forma de pagamento, ciclo de faturamento e regras de dunning são parâmetros dela |
| **Chave de integração** | É ela que leva o resultado da arrecadação para a contabilidade no FI |

*"Sem conta contrato não há fatura, pagamento nem cobrança: ela é o coração do
FI-CA."* Ver [MD-05](10-MD-05-conta-contrato.md).

---

## O erro que todo mundo comete

**Achar que o FI-CA cobra, e que o BILL só calcula.**

A fronteira é outra. **Quem cria a dívida é o Faturamento**, dentro do BILL, e
ele o faz gerando o documento FI-CA. O FI-CA recebe a dívida já criada, e o que
ele faz é **receber ou perseguir**.

Dito de outro jeito: quando você abre a partida em aberto de um cliente, está
olhando algo que o BILL criou e que o FI-CA administra. Ver
[BI-01](39-BI-01-calculo-e-faturamento.md).

---

## Na prática

**Este é o módulo com mais integração externa do IS-U inteiro.** Bancos,
agentes arrecadadores, adquirentes de cartão, o arranjo do Pix, bureaus de
crédito, cartórios e assessorias de cobrança. Nenhuma outra área conversa com
tanta gente de fora.

Consequência para quem atende: **quando um pagamento não aparece, a causa
muitas vezes não está no SAP.** Está no ciclo de um terceiro.

---

## No sistema

**Não há transação desta nota.** A Aula 05 apresentou o FI-CA inteiro em 24
slides e **não mostrou um único código**, nem de transação nem de tabela.

Isso não é lacuna de captura, é característica da aula. **As transações de
FI-CA são pergunta para o instrutor**, e a [`_BANCADA.md`](_BANCADA.md) tem a
seção de FI-CA montada a partir do pôster de tabelas.

---

## Se sobrar uma coisa

O FI-CA não cria a dívida. Ele recebe ou persegue a dívida que o faturamento
criou.

---

## Recall

1. Nomeie os dois grandes processos do FI-CA.
2. Em uma linha, o que é a Arrecadação?
3. Em uma linha, o que é a Cobrança?
4. Descreva as quatro etapas da arrecadação, na ordem.
5. Qual das quatro etapas concentra o risco, e por quê?
6. Nomeie as quatro razões que fazem a Conta Contrato ser o dado mestre central do FI-CA.
7. Quem cria a dívida, o BILL ou o FI-CA?
8. Um pagamento não aparece no sistema e o cadastro está correto. Cite onde a causa costuma estar.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#fc-01)  ·  responda tudo antes de abrir.
