# FC-07: Do pagamento à compensação, o caminho do dinheiro
> O banco manda um arquivo, o SAP lê 44 posições de código de barras, acha a
> conta contrato e baixa as partidas. Cada elo desse caminho é um lugar onde o
> pagamento some.

**Onde entra:** o mecanismo por trás de "eu paguei e não consta".
**Antes disto:** [FC-06](49-FC-06-o-registro-da-cobranca.md), [FC-03](46-FC-03-status-e-motivo-de-compensacao.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## O formulário de pagamento não é uma fatura

**Esta é a confusão mais cara desta nota.**

> *"Não é um débito novo: é o agrupamento dos itens em aberto da conta contrato
> em um único documento de cobrança."*

O exemplo do material, um formulário de **R$ 437,50**:

```
Fatura de maio ................  R$ 187,45
Fatura de abril em atraso .....  R$ 162,30
Juros e multa sobre abril .....  R$   4,85
Parcela 2/6 do parcelamento ...  R$  90,00
Item de convênio ..............  R$  12,90
Crédito de devolução ..........  R$ -20,00
                                 ─────────
Código de barras ..............  R$ 437,50
```

| Regra | O que diz |
|---|---|
| **Ele espelha, não cria débito** | Os débitos continuam sendo as partidas em aberto; o formulário só as representa |
| **O agrupamento segue regras** | Entram vencidos e a vencer, **já líquidos dos créditos**. Itens bloqueados ou em contestação **ficam de fora** |
| **No pagamento, a baixa é dos itens** | A compensação recai sobre **cada partida**, com motivo 01 |

**A segunda regra é o gancho com a [FC-05](48-FC-05-bloqueios-comerciais.md):**
bloquear um item o tira do formulário.

---

## As 44 posições

O padrão FEBRABAN de arrecadação, no exemplo do material:

| Posições | Exemplo | O que é |
|---|---|---|
| **01 a 04** | 8364 | Produto, segmento, tipo de valor e dígito verificador |
| **05 a 15** | 00000018745 | **Valor em centavos**, lido como R$ 187,45 |
| **16 a 19** | 0074 | **Identificação da empresa** junto à FEBRABAN |
| **20 a 44** | livre | Campo definido pela empresa, **normalmente a conta contrato e o número da fatura** |

**Duas leituras que valem para a prova:**

A **segunda posição classifica o segmento**, e o dígito **3 é energia elétrica
e gás**. Por isso o código diz, antes de qualquer coisa, que tipo de conta é
aquela.

O **campo livre é onde mora a conta contrato**. É ele que faz o pagamento achar
o cliente, e é por isso que ele é livre: cada empresa decide o que põe ali.

---

## O caminho do arquivo

```
1 ARQUIVO DE RETORNO ──▶ 2 DIRETÓRIO NO SAP ──▶ 3 UMA LINHA POR ──▶ 4 LOTE DE
  o banco envia            depositado num          PAGAMENTO           PAGAMENTO
  diariamente com          diretório lido pelo     data, agência,      identifica a
  todos os pagamentos      FI-CA, importado        código de barras    conta contrato,
  capturados               por job                 e valor pago        compensa e separa
                                                                       o que não casa
```

**A etapa 4 tem duas saídas, e a segunda é a que gera chamado:** o que não casa
é separado para esclarecimento manual.

---

## Por que existe a FEBRABAN

> *"Sem o padrão FEBRABAN, cada banco entregaria um arquivo diferente e a
> conciliação automática no FI-CA não seria viável."*

Ela padroniza três coisas: os **meios de cobrança**, os **arquivos** trocados
em remessa e retorno, e as **regras de negócio** de registro, confirmação,
devolução e estorno.

*"No fluxo de arrecadação, o padrão FEBRABAN é o contrato entre banco e
empresa."*

---

## O erro que todo mundo comete

**Achar que o pagamento entra no sistema no momento em que o cliente paga.**

Entre o clique do cliente e a partida baixada existem quatro etapas e pelo
menos um ciclo diário de arquivo. O comprovante prova a primeira etapa; a
compensação acontece na quarta.

**É exatamente o descompasso que a [CS-08](24-CS-08-corte-e-religacao.md)
descreve**, agora com o mecanismo à vista: o arquivo é diário, e a régua de
cobrança roda no ciclo dela.

---

## No sistema

**Não há transação desta nota.** A Aula 05 apresentou o FI-CA inteiro em 24
slides e **não mostrou um único código**, nem de transação nem de tabela.

Isso não é lacuna de captura, é característica da aula. **As transações de
FI-CA são pergunta para o instrutor**, e a [`_BANCADA.md`](_BANCADA.md) tem a
seção de FI-CA montada a partir do pôster de tabelas.

---

## Se sobrar uma coisa

O formulário de pagamento espelha os débitos, não os cria, e quem baixa são as
partidas por trás dele.

---

## Recall

1. O formulário de pagamento cria um débito novo?
2. Nomeie as três regras do formulário de pagamento.
3. Quais itens ficam de fora do agrupamento do formulário?
4. Quantas posições tem o código de barras de arrecadação no padrão FEBRABAN?
5. Que informação está nas posições 05 a 15?
6. Que informação está nas posições 16 a 19?
7. O que costuma ocupar o campo livre do código de barras?
8. Qual dígito do código identifica o segmento de energia elétrica e gás?
9. Descreva as quatro etapas do arquivo de retorno, da emissão pelo banco ao lote.
10. Nomeie as três coisas que a FEBRABAN padroniza.
11. Um cliente pagou hoje e o débito consta em aberto. Cite o que explicar.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#fc-07)  ·  responda tudo antes de abrir.
