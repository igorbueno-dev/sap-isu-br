# CS-09: O que o atendente vê, e onde mora o resto
> O CRM não guarda a maior parte do que o cliente pergunta. Ele guarda uma
> cópia de alguns objetos, e o resto vive no IS-U.

**Onde entra:** por que certas respostas exigem trocar de sistema.
**Antes disto:** [AR-03](28-AR-03-objetos-replicados.md), [CS-04](20-CS-04-crm-no-contexto-utilities.md)
**Origem:** **misto.** O de-para de objetos replicados é do material.
**A leitura pelo lado do atendimento é minha.**

---

## Os quatro que existem dos dois lados

| Objeto | No IS-U | No CRM |
|---|---|---|
| Parceiro de Negócio | `BUT000` | `BUT000` |
| Conta Contrato | `FKKVKP` | `CRMM_BUAG` |
| Objeto de Ligação | `EHAUISU` | `COMM_PRODUCT` |
| Ponto de Entrega | `EUIHEAD` | `IBASE` / `COMM_PRODUCT` |

**Repare no que não está na lista:** Contrato, Instalação, Local de Consumo,
Equipamento, leitura, documento de cálculo, fatura, partida em aberto.

**Ou seja: quase tudo que o cliente pergunta.**

---

## A pergunta do cliente e o lado que responde

| O cliente pergunta | Responde |
|---|---|
| "Meus dados estão certos?" | **CRM.** O Parceiro de Negócios é o mesmo dos dois lados |
| "Como eu pago?" | **CRM.** A Conta Contrato tem cópia |
| "Desde quando eu sou titular?" | **IS-U.** O Contrato não replica |
| "Quanto eu consumi?" | **IS-U.** Leitura não replica |
| "Por que a conta veio assim?" | **IS-U.** Documento de cálculo não replica |
| "Estou devendo?" | **IS-U.** A partida em aberto é de FI-CA |

**O padrão é claro: o CRM replica quem é o cliente, e não replica o que
aconteceu com ele.**

---

## Por que o Objeto de Ligação vira produto

Do lado do CRM, o que existe naquele endereço é um **produto contratado**. A
estrutura física, com prédio, apartamento e medidor, é problema do IS-U.

Isso explica uma frustração comum do atendimento: **o CRM não tem o desenho do
prédio.** Se a pergunta envolve qual apartamento tem qual medidor, a resposta
está do outro lado. Ver [MD-02](07-MD-02-a-traducao-do-predio.md).

---

## O erro que todo mundo comete

**Concluir que o dado não existe porque não apareceu na tela do CRM.**

Não aparecer no CRM quase nunca significa ausência. Significa que aquele objeto
não replica, e a resposta está no IS-U. **A conclusão errada gera abertura de
chamado de cadastro para um dado que está correto do outro lado.**

O sintoma inverso também existe: dado divergente entre os dois sistemas é
problema de **replicação**, não de cadastro. Ver
[AR-02](27-AR-02-middleware-e-replicacao.md).

---

## Na prática

**Antes de abrir chamado de "dado faltando", pergunte se aquele objeto
replica.** A lista tem quatro itens e cabe na memória.

Quando o dado existe dos dois lados mas está diferente, o caminho é a fila de
replicação, e as transações que resolvem isso estão na
[AR-02](27-AR-02-middleware-e-replicacao.md).

---

## No sistema

| Tabela | Onde vive | O quê |
|---|---|---|
| `BUT000` | **Os dois lados** | Parceiro de Negócios |
| `FKKVKP` / `CRMM_BUAG` | IS-U / CRM | Conta Contrato |
| `EHAUISU` / `COMM_PRODUCT` | IS-U / CRM | Objeto de Ligação |
| `EUIHEAD` / `IBASE` | IS-U / CRM | Ponto de Entrega |

As transações que investigam a fila de replicação estão na
[AR-02](27-AR-02-middleware-e-replicacao.md).

---

## Se sobrar uma coisa

O CRM replica quem é o cliente, não o que aconteceu com ele.

---

## Recall

1. Nomeie os quatro objetos que existem dos dois lados.
2. Qual objeto tem o mesmo nome de tabela nos dois sistemas?
3. Qual o nome da Conta Contrato no CRM?
4. Em que o Objeto de Ligação se transforma do lado do CRM?
5. O Contrato replica para o CRM?
6. Em qual sistema está a resposta para "quanto eu consumi"?
7. Em qual sistema está a resposta para "estou devendo"?
8. Um dado não aparece na tela do CRM. Cite a conclusão errada que isso costuma gerar.
9. Um dado existe nos dois sistemas com valores diferentes. Cite onde está o problema.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#cs-09)  ·  responda tudo antes de abrir.
