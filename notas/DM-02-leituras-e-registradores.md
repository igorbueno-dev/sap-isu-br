# DM-02: Leituras e registradores
> Seis tipos de leitura, cinco motivos e seis registradores. Parece lista de
> decorar, e não é: cada eixo responde uma pergunta diferente da investigação.

**Onde entra:** segunda metade do Bloco 2, DM / GAT.
**Antes disto:** [DM-01-ativos-e-estoque](DM-01-ativos-e-estoque.md)

---

## Três eixos, não uma lista

São três quadrantes que parecem repetidos e não são:

| Eixo | Pergunta que responde |
|---|---|
| **Tipo de leitura** | **Como** o número foi obtido |
| **Motivo de leitura** | **Por que** alguém foi ler |
| **Registrador** | **O que** foi medido |

Uma mesma leitura tem os três: foi obtida de um jeito, por um motivo, sobre
uma grandeza. Separar os eixos é o que permite ler a tela e entender a história.

---

## Os seis tipos de leitura

| Tipo | O que aconteceu |
|---|---|
| **Real** | Alguém, ou o sistema de telemetria, leu o número no visor |
| **Estimada** | Ninguém leu. O sistema calculou pelo histórico |
| **Informada** | **O cliente** passou o número |
| **De troca** | A leitura tirada no momento de substituir o medidor |
| **De instalação** | O número em que o medidor começou naquele imóvel |
| **De retirada** | O número em que ele parou ao ser retirado |

**Os três primeiros são sobre quem leu. Os três últimos são sobre eventos do
equipamento.** Essa é a divisão interna do quadrante.

> **Leitura de troca, de instalação e de retirada andam juntas.** Trocar um
> medidor gera as três: retira o velho no número X, instala o novo no número
> Y, e a leitura de troca amarra o par. **Se uma das três faltar, o consumo do
> mês fica sem dono** e vira o clássico "trocaram o medidor e a conta veio
> absurda".

---

## Os cinco motivos de leitura

| Motivo | Quando |
|---|---|
| **Leitura periódica** | O ciclo mensal. O volume |
| **Troca de equipamento** | Ver acima |
| **Fiscalização** | Suspeita de irregularidade. **Porta de entrada de Perdas** |
| **Encerramento contratual** | O cliente está saindo. Move-Out |
| **Ligação nova** | O cliente está entrando |

**Repare que três dos cinco motivos não são o ciclo normal.** A leitura de
rotina é só um deles; os outros quatro são disparados por evento. Isso explica
por que uma instalação pode ter várias leituras no mesmo mês sem que nada
esteja errado.

O **encerramento contratual** amarra este bloco no Move-Out:
ver [MD-07](MD-07-move-in-move-out.md).

---

## Os seis registradores

O registrador é a grandeza que o aparelho acumula. Um medidor pode ter vários.

| Registrador | O que mede |
|---|---|
| **Energia ativa** | O consumo que todo mundo conhece. kWh |
| **Energia reativa** | A energia que o equipamento do cliente devolve à rede sem consumir. Cobrada de cliente industrial |
| **Demanda** | O **pico** de potência, não o total. Cliente grande paga por isto |
| **Energia injetada** | O que o cliente **gerou e mandou para a rede** |
| **Energia consumida** | O que ele puxou da rede |
| **Outros registradores** | ⟨não detalhados⟩ |

**Energia injetada é a novidade que muda o setor.** Ela só existe porque o
cliente virou gerador: painel solar no telhado, excedente indo para a rede e
virando crédito. **Consequência:** uma instalação com geração distribuída
**não tem um número, tem dois**, injetada e consumida, e a conta é a diferença
entre eles. Por isso existe o medidor bidirecional.

> Isto conecta com o caso de workflow de micro e minigeração.
> Ver [WM-02](WM-02-workflow-e-integracoes.md).

---

## O que amarra tudo: registrador e tarifa

Um registrador sozinho é um número sem significado. Ele só vira dinheiro
quando está **associado a um item da tarifa**, e essa associação vive na
Instalação. Ver [ST-03](ST-03-instalacao.md) e [ST-04](ST-04-equipamento.md).

**É a falha silenciosa mais comum de Device Management:** o medidor foi
instalado tecnicamente, está certo no cadastro, e ninguém fez a relação
registrador/tarifa. **A instalação simplesmente não fatura**, e o erro só
aparece na fila de faturamento, dias depois, num time diferente.

---

## Recall

1. Quais são os três eixos, e que pergunta cada um responde?
2. Um cliente ligou e passou o número do medidor. Que tipo de leitura é essa?
3. Trocaram um medidor. Quantas leituras isso gera, e o que acontece se faltar uma?
4. Uma instalação teve três leituras num mês. Isso é erro?
5. O que é energia injetada, e por que ela existe?
6. Uma instalação não faturou e o medidor está corretamente instalado. Qual sua primeira hipótese?

> **Gabarito:** [`_GABARITOS.md`](_GABARITOS.md#dm-02)  ·  responda tudo antes de abrir.

---

## Ligações

[DM-01-ativos-e-estoque](DM-01-ativos-e-estoque.md) · [ST-04-equipamento](ST-04-equipamento.md) · [ST-03-instalacao](ST-03-instalacao.md) · [MD-07-move-in-move-out](MD-07-move-in-move-out.md)
