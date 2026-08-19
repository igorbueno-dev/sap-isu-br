# AR-01: O landscape e as cinco camadas
> Dois desenhos da mesma coisa. Um simples, para entender; um detalhado, para
> se localizar. Comece pelo simples.

**Onde entra:** primeira nota de arquitetura. Explica onde cada sistema mora.
**Antes disto:** [CS-04-crm-no-contexto-utilities](CS-04-crm-no-contexto-utilities.md)
**Depois disto:** [AR-02-middleware-e-replicacao](AR-02-middleware-e-replicacao.md)

---

## O desenho simples: back end, middleware, front end

```
   ANALYSES          ┊              FRONT END
   ┌────────┐        ┊
   │ SAP BW │──┐     ┊         ┌──→ ITS ──→ WebClient
   └────────┘  │  ┌──┴───┐     │
               ├──│ MID- │──→ SAP CRM ──→ CTI ──→ Call Center
   ┌────────┐  │  │ DLE- │    System    │
   │SAP IS-U│──┘  │ WARE │              └──→ Canais Digitais
   │ / CCS  │     └──┬───┘
   └────────┘        ┊
   BACK END          ┊
```

Três leituras que este desenho entrega de uma vez:

1. **O CRM fica no meio, não no fundo.** O IS-U é back end para ele.
2. **O BW está do lado do back end**, junto com o IS-U, na área de análises.
   Mais uma confirmação de que BW não é área funcional, é camada de dados.
3. **Nada fala direto.** Tudo passa pelo Middleware, e isso é uma decisão de
   arquitetura, não um detalhe.

No miolo do CRM ficam os objetos de negócio: *business partner, activities,
contracts, products, sales and distribution projects*.

---

## O desenho detalhado: cinco camadas

O mesmo landscape se abre em cinco faixas horizontais, de cima para baixo:

| # | Camada | O que tem |
|---|---|---|
| 1 | **Canais** | Web/Portal, Call Center, Mobile, outros |
| 2 | **Camada CRM** (WebUI / IC WebClient) | Atividades, Protocolos/Reclamações, Serviços/Solicitações, Contratos, Marketing/Campanhas, Business Partner, Relatórios |
| 3 | **Middleware** | BDoc, qRFC, ALE |
| 4 | **Camada IS-U/CCS** | Business Partner, Conta Contrato, Instalação/Objeto de Ligação, Ponto de Entrega, e os módulos DM, Billing, FI-CA, WM/CS |
| 5 | **Integrações externas** | GIS, SCADA, IVR, CTI, Web Portal, Salesforce, bancos, agências, SAP BW |

**A leitura é de cima para baixo:** o cliente entra por um canal, cai na tela
do CRM, o dado desce pelo middleware e chega ao IS-U, que executa.

---

## O que a camada 5 revela

A lista de integrações externas diz muito sobre o setor:

- **GIS** é o mapa da rede. **SCADA** é a operação em tempo real.
- **IVR** e **CTI** são a telefonia: IVR atende, CTI joga a ligação na tela.
- **Bancos e agências** são arrecadação, o dinheiro voltando.

> **Uma concessionária não roda em um sistema, roda numa constelação.** O
> IS-U é o centro contábil e comercial, não o todo.

---

## O erro que todo mundo comete

> Achar que o CRM "é" o IS-U com outra tela. São **dois sistemas separados**,
> com bases próprias, e é exatamente por isso que existe middleware. Se fossem
> o mesmo sistema, replicar não faria sentido.

Este é o ponto que a próxima nota desenvolve.

---

## Recall

1. No landscape, o IS-U é back end ou front end em relação ao CRM?
2. Onde o BW aparece, e o que isso confirma?
3. Liste as cinco camadas da arquitetura, de cima para baixo.
4. O que ITS e CTI conectam, respectivamente?
5. Por que a existência de um middleware prova que CRM e IS-U são sistemas
   distintos?

> **Gabarito:** [`_GABARITOS.md`](_GABARITOS.md#ar-01)  ·  responda tudo antes de abrir.

---

## Ligações

[AR-02-middleware-e-replicacao](AR-02-middleware-e-replicacao.md) · [AR-03-objetos-replicados](AR-03-objetos-replicados.md) · [CS-04-crm-no-contexto-utilities](CS-04-crm-no-contexto-utilities.md)
