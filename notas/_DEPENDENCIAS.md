# MAPA DE DEPENDÊNCIAS
### A ordem real do aprendizado, e as lacunas que ela revela

> **Por que este arquivo existe.** A ordem de estudo de IS-U não é arbitrária:
> ela está embutida na estrutura do conteúdo. Ninguém entende Local de Consumo
> antes de Objeto de Ligação, porque um não existe sem o outro.
>
> **Bônus:** dependência detecta lacuna. Um conceito citado **sem o
> pré-requisito explicado** é evidência de que falta alguma coisa no material.

---

## O grafo

```mermaid
flowchart TD
    GE01["GE-01<br/>O que é o CCS"]
    GE02["GE-02<br/>Evolução do produto"]
    MD01["MD-01<br/>Mapa dos dados mestres"]
    MD08["MD-08<br/>Os dois mundos"]
    MD02["MD-02<br/>A tradução do prédio"]
    MD03["MD-03<br/>Parceiro de Negócios"]
    MD04["MD-04<br/>PN, dados e customizing"]
    MD05["MD-05<br/>Conta Contrato"]
    ST01["ST-01<br/>Objeto de Ligação"]
    ST02["ST-02<br/>Local de Consumo"]
    ST03["ST-03<br/>Instalação"]
    ST04["ST-04<br/>Equipamento"]
    MD06["MD-06<br/>CONTRATO"]

    GE01 --> GE02
    GE01 --> MD01
    MD01 --> MD08
    MD08 --> MD02
    MD02 --> MD03
    MD02 --> ST01
    MD03 --> MD04
    MD03 --> MD05
    ST01 --> ST02
    ST02 --> ST03
    ST03 --> ST04
    MD05 ==> MD06
    ST03 ==> MD06

    GE01 --> CS04
    CS01 --> CS02
    CS02 --> CS03
    CS03 --> CS04
    CS04 --> CS05
    CS04 --> AR01
    AR01 --> AR02
    AR02 --> AR03
    MD06 -.-> AR03

    CS01["CS-01<br/>O que e CRM"]
    CS02["CS-02<br/>Ciclo de vida"]
    CS03["CS-03<br/>Pilares do SAP CRM"]
    CS04["CS-04<br/>CRM em Utilities"]
    CS05["CS-05<br/>Processos e atividades"]
    AR01["AR-01<br/>Landscape e camadas"]
    AR02["AR-02<br/>Middleware"]
    AR03["AR-03<br/>Objetos replicados"]

    SV01["SV-01<br/>Servico de Campo"]
    WM01["WM-01<br/>Nota de servico"]
    WM02["WM-02<br/>Workflow e integracoes"]
    DM01["DM-01<br/>Ativos e estoque"]
    DM02["DM-02<br/>Leituras e registradores"]
    PE01["PE-01<br/>Fraude e defeito"]
    PE02["PE-02<br/>Faturado da epoca"]

    GE01 --> SV01
    SV01 --> WM01
    WM01 --> WM02
    SV01 --> DM01
    DM01 --> DM02
    SV01 --> PE01
    PE01 ==> PE02
    ST04 -.-> DM01
    WM01 -.-> PE01
    DM02 -.-> PE01
```

---

## A leitura mais importante do grafo

**O Contrato é o único conceito que exige os dois ramos completos.**

Todo o resto desce em linha reta: comercial de um lado, técnico do outro. O
Contrato é o único nó com **duas setas grossas entrando**, uma de cada mundo.

Três consequências:

1. **É por isso que ele costuma ser ensinado por último.** Não dá para ensinar antes.
2. **É por isso que ele é o mais difícil.** Exige tudo o que veio antes.
3. **É por isso que ele é o que mais cai.** É onde o entendimento se prova.

Se você entende o Contrato de verdade, entende os dados mestres inteiros. Se
não entende, o problema está em algum nó acima dele, não nele.

---

## Ordem de estudo derivada

`GE‑01` → `MD‑01` → `MD‑02` → então os dois ramos em paralelo:

| Ramo comercial | Ramo técnico |
|---|---|
| `MD‑03` Parceiro de Negócios | `ST‑01` Objeto de Ligação |
| `MD‑04` PN, dados | `ST‑02` Local de Consumo |
| `MD‑05` Conta Contrato | `ST‑03` Instalação |
| | `ST‑04` Equipamento |

E os dois convergem em **`MD‑06` Contrato**.

`GE‑02` (evolução do produto) é folha solta: útil, sem dependente.

---

# PONTOS EM ABERTO

O método: procurar conceito **citado mas nunca desenvolvido**, ou nó de menu
**visível mas nunca aberto**. Cada um é um buraco no modelo.

## Fechados por nota própria

| Conceito | Por que era lacuna | Situação |
|---|---|---|
| **Move In** | O Contrato "é criado durante o Move In", mas o processo é tratado à parte dos dados mestres | Coberto por [MD-07-move-in-move-out](MD-07-move-in-move-out.md). **Falta confirmar a transação** |
| **Registrador** | Citado junto de equipamento, quase nunca definido | Coberto dentro de [ST-04-equipamento](ST-04-equipamento.md) |

> **As duas notas são de autoria própria, não de fonte oficial.** Trate como
> hipótese bem fundamentada e confirme na documentação SAP. A transação de
> Move-In continua em aberto.

## Estruturais: fazem parte do modelo e ainda não cobri

| Conceito | Evidência | Situação |
|---|---|---|
| ~~**Ponto de Entrega (PoD)**~~ | Aparecia no menu de dados mestres técnicos e nunca era desenvolvido | **PARCIALMENTE COBERTO** por [AR-03-objetos-replicados](AR-03-objetos-replicados.md): tem posição na arquitetura e tabela `EUIHEAD` ⟨confirmar⟩. **Faltam as transações e a cardinalidade** |
| **Ligação** | Nó no menu, entre Objeto de Ligação e Local de Consumo | Não explorado |
| **Estrutura Postal** | Divisão 1 de 4 dos dados mestres (slide `img-05` da A01), e WM "mantém estruturas políticas e postais" (A02) | **Nomeada e nunca desenvolvida.** Conteúdo e transações em aberto |
| **Estrutura Regional** | Nó no menu | Não desenvolvida |

## Próximos temas

| Conceito | Onde se encaixa |
|---|---|
| **Dados Transacionais** | Divisão 4 de 4, entra com leitura e faturamento |
| **Planejamento de datas** | MRU e porções |
| **CIC** | Interface centralizada de atendimento, área de CS/CRM |
| **EDM** | Gestão de dados de medição |

---

## Pontos em aberto de CRM e arquitetura

| Conceito | Situação |
|---|---|
| **Prospect, Lead e Oportunidade** | Os três termos que mais se confundem em CRM, e ainda não escrevi a nota. **Contribuição muito bem-vinda** |
| **`EHAUISU` x `EHAU`** | Duas formas para a tabela do Objeto de Ligação. Não sei qual é a correta |
| **`FOP`** | Sigla que aparece em "Processos/FOPs" e que não consegui expandir |
| **Webclient, modelagem de processos, validações, vínculos, estrutura organizacional** | Temas de CRM que este material ainda não cobre |

---

## Como manter isto

A cada tema novo:

1. Acrescentar os nós novos ao grafo, ligando ao pré-requisito
2. Procurar **conceito citado sem definição** e **nó de menu não aberto**
3. Verificar se alguma lacuna anterior **foi fechada** e riscar da lista

**O sinal de saúde:** lacuna que fecha logo é sequência normal de estudo.
Lacuna que atravessa o material inteiro é assunto que a fonte não cobre, e aí
você decide se estuda por fora.

---

**Fontes públicas consultadas para validar o modelo padrão:**

- [SAP IS-U data model, Business and Technical Master Data](https://blogs.sap.com/2012/03/26/sap-is-u-data-model-business-and-technical-master-data/)
- [SAP ISU Technical Master Data, dimplethoughts](https://dimplethoughts.wordpress.com/2018/07/19/sap-isu-technical-master-data/)
- [ISU Data Model Information, Sachin H Patil](https://sachinhpatil.com/sapis-utilities/isu-data-model-information/)
- [SAP IS-U, Wikipedia](https://en.wikipedia.org/wiki/SAP_IS-U)
- [Tabela EVER, SAP Datasheet](https://www.sapdatasheet.org/abap/tabl/ever.html)
