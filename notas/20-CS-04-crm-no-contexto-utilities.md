# CS-04: CRM no contexto Utilities
> Onde exatamente o CRM se encaixa na cadeia que você já conhece. Ele é a
> primeira área, a porta por onde tudo entra.

**Onde entra:** liga a área de CRM ao IS-U que você já viu.
**Antes disto:** [CS-03-sap-crm-e-os-pilares](19-CS-03-sap-crm-e-os-pilares.md), [GE-01-o-que-e-is-u-ccs](02-GE-01-o-que-e-is-u-ccs.md)
**Depois disto:** [CS-05-processos-e-atividades](21-CS-05-processos-e-atividades.md)

---

## A frase que define o encaixe

> SAP CRM é frequentemente utilizado como a **camada de atendimento ao
> cliente, integrada ao SAP IS-U/CCS**.

Guarde "camada". Não é um módulo dentro do IS-U, é um sistema **por cima** do
IS-U, integrado a ele. Isso vai importar quando chegarmos na arquitetura.

---

## O que ele permite

- Registro de **protocolos de atendimento**
- Gestão de **atividades e solicitações**
- Controle de contratos e **parceiros de negócio** (Business Partner)
- **Integração com Salesforce** e outros sistemas de CRM
- Execução de processos comerciais e de relacionamento

> **A quarta linha é a mais reveladora.** O SAP CRM se integra a *outros* CRMs.
> Na vida real é comum a concessionária ter Salesforce na ponta e SAP CRM no
> meio. Não assuma que existe um CRM só.

---

## A posição na cadeia

A cadeia de cinco áreas da [`GE‑01`](02-GE-01-o-que-e-is-u-ccs.md), agora detalhada:

```
CS + CRM  →  WM  →  DM  →  BILL  →  FI-CA
Customer     Work   Device  Billing  Credit and
Service      Mgmt   Reading  and     Collection
                            Invoicing
─────────────────────────────────────────────
        BW - Business Warehouse
```

**CS + CRM é a primeira.** É onde o pedido nasce, antes de virar ordem de
campo, antes de virar leitura, antes de virar conta.

O que a área faz:

| Responsabilidade | Tradução |
|---|---|
| Front-end interface to Customer Services | É a tela do atendente |
| Maintain customer interactions and contacts | Registra quem falou o quê, quando |
| Offers the customers services (new connection, reconnection, etc) | **É aqui que ligação nova e religação entram no sistema** |
| Maintain the activities of call agents and business agents | Gerencia o trabalho de quem atende |

---

## Onde o BW entra

O mesmo desenho traz **BW como uma faixa única atravessando as cinco áreas**,
não como sexta caixa na fila.

**BW não é uma das áreas funcionais**, é a camada de informação que lê todas elas.

---

## O erro que todo mundo comete

> Achar que CRM e Customer Service são coisas diferentes porque têm nomes
> diferentes. Na cadeia, a caixa se chama **CS + CRM**, com o sinal de mais.
> É uma área só, e o CRM é a tecnologia que a sustenta.

---

## Recall

1. CRM é um módulo dentro do IS-U? Justifique com uma palavra.
2. Qual a posição do CS + CRM na cadeia das cinco áreas?
3. Onde uma ligação nova entra no sistema?
4. Por que BW não conta como área funcional?
5. O que significa dizer que o SAP CRM integra com Salesforce?

> **Gabarito:** [`_GABARITOS.md`](_GABARITOS.md#cs-04)  ·  responda tudo antes de abrir.
