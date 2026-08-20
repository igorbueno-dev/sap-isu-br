# CS-03: SAP CRM e os três pilares
> O produto. Marketing, Vendas e Serviço, cada um com sua fileira de módulos.
> E o nome novo que a SAP deu a tudo isso dentro do S/4HANA.

**Onde entra:** onde o conceito de CRM vira software.
**Antes disto:** [CS-02-ciclo-de-vida-do-cliente](18-CS-02-ciclo-de-vida-do-cliente.md)
**Depois disto:** [CS-04-crm-no-contexto-utilities](20-CS-04-crm-no-contexto-utilities.md)

---

## O que é o SAP CRM

Solução SAP de gerenciamento do relacionamento com clientes, que suporta as
áreas de negócio focadas no cliente, **segmentada em três pilares: Marketing,
Vendas e Serviço.**

O que a ferramenta faz:

- Identificar e **segmentar** os melhores clientes
- Gerenciar **campanhas** de marketing
- Gerenciar **leads e oportunidades** de vendas
- Tratar do **pós-venda**: ordens de serviço, atendimento ao cliente

Repare que a lista percorre os três pilares na ordem, e na mesma ordem do
ciclo de vida da nota anterior.

---

## A matriz funcional

Cada pilar é uma fileira de módulos. Não decore a matriz inteira: **entenda
que cada célula é um módulo que pode ou não ser implantado.**

**Marketing**
> Marketing Resource Management · Segmentation & List Management ·
> Campaign Management · Real-Time Offer Management · **Lead Management** ·
> Loyalty Management

**Sales**
> Sales Planning & Forecasting · Sales Performance Management ·
> Territory Management · Accounts & Contacts · **Opportunity Management** ·
> Quotation & Order Management · Pricing & Contracts ·
> Incentive & Commission Management · Time & Travel

**Service**
> Service Sales & Marketing · Service Contracts & Agreements ·
> Installations & Maintenance · **Customer Service & Support** ·
> Field Service Management · Returns & Depot Repair ·
> Warranty & Claims Management · Service Logistics & Finance ·
> Service Collaboration, Analytics, Optimization

Atravessando as três fileiras, faixas verticais de canal:
**Web Channel**, **Interaction Center**, **Partner Channel Management**,
e nas bordas **Business Communication Management** e
**Trade Promotion Management**.

> **As faixas verticais são canais, não pilares.** É por onde o atendimento
> entra, e vale para os três. O **Interaction Center** é a que mais importa em
> utilities.

---

## O que cada pilar faz

| Pilar | Resumo |
|---|---|
| **Marketing** | Analisa, planeja, desenvolve e executa as atividades de marketing durante as integrações com clientes e leads |
| **Sales** | Adquirir, crescer e manter relacionamentos lucrativos: previsão de vendas, territórios, contas e contatos, oportunidades, cotações, pedidos, preços e contratos de venda |
| **Service** | Receita e lucratividade de serviços: contratos de serviço, serviço de campo, e-service, gestão de força de trabalho. Call center, campo e e-service como canais de entrega |

---

## O nome novo: S/4 Customer Engagement

O CRM clássico é um sistema separado. Dentro do S/4HANA, a SAP embutiu uma
**versão simplificada**, chamada **S/4 Customer Engagement**, que aproveita a
tecnologia do **CRM Web UI** e entrega o **S/4HANA Interaction Center**.

> O S/4HANA Interaction Center é o canal especializado de atendimento ao
> cliente, dando acesso a vários setores, processos e funções.

**Por que isso importa:** é o mesmo movimento da linha do tempo do produto.
O que era sistema separado vira componente embutido. Quem sabe CRM clássico
sabe o Customer Engagement, e essa é a resposta certa quando perguntarem se o
conhecimento de CRM continua valendo no S/4HANA.

---

## Recall

1. Quais os três pilares, e qual carrega o setor de utilities?
2. Qual a diferença entre um pilar e uma faixa vertical da matriz?
3. Cite um módulo de cada pilar.
4. O que é o S/4 Customer Engagement, e qual sua relação com o CRM clássico?

> **Gabarito:** [`_GABARITOS.md`](_GABARITOS.md#cs-03)  ·  responda tudo antes de abrir.
