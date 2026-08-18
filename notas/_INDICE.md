# ÍNDICE DAS NOTAS

### A porta de entrada. Você navega por aqui, nunca pela pasta.

> **Regra da nota atômica:** uma nota é um conceito que você revisaria
> sozinho. 5 a 10 minutos de leitura, teto de 120 linhas, terminando em
> raciocínio fechado. **Se crescer, vira duas.**

---

## Como usar

| Situação | O que fazer |
|---|---|
| **Saber em que ordem estudar** | [`_DEPENDENCIAS.md`](_DEPENDENCIAS.md), o grafo de pré-requisitos |
| **Saber o que ainda falta** | [`_DEPENDENCIAS.md`](_DEPENDENCIAS.md), seção de pontos em aberto |
| Revisar antes de uma prova | Ler só a seção **Recall** de cada nota, na ordem |
| Estudar um tema | Abrir a nota, ler inteira, fazer o recall no fim |
| Achar uma transação | [`02-BANCADA.md`](../02-BANCADA.md) |
| Ver o mapa geral | [`00-NUCLEO.md`](../00-NUCLEO.md) |

---

## A coluna Status, e por que ela existe

| Marca | Significa |
|---|---|
| **verificado** | Conferido contra o sistema ou material de produto |
| **a confirmar** | Escrito por mim a partir de leitura e raciocínio. Bem fundamentado, **mas ainda não conferido na documentação SAP** |

Nota `a confirmar` não é pior, é **não conferida**. Duas delas cobrem pontos
que o material de produto trata mal, e por isso valem muito. Mas não recite
conteúdo `a confirmar` como se fosse fonte oficial.

---

## Dados Mestres

### Geral

| Código | Tema | Status | O gancho | Tempo |
|---|---|---|---|---|
| [`GE-03`](GE-03-a-concessionaria.md) | **A concessionária em 5 parágrafos** | a confirmar | O problema de negócio. **Leia primeiro de tudo** | 5 min |
| [`GE-01`](GE-01-o-que-e-is-u-ccs.md) | O que é o SAP IS-U CCS | verificado | As duas siglas, as cinco áreas, e por que BW não é uma delas | 6 min |
| [`GE-02`](GE-02-evolucao-do-produto.md) | A evolução do produto | verificado | Do R/3 ao SaaS, e a data de 2027 que gera projeto | 4 min |
| [`GE-04`](GE-04-os-tres-setores.md) | Os três setores | a confirmar | Energia, gás e água. Muda a resposta do exercício | 5 min |

### Dados mestres comerciais

| Código | Tema | Status | O gancho | Tempo |
|---|---|---|---|---|
| [`MD-01`](MD-01-mapa-dos-dados-mestres.md) | O mapa dos dados mestres | verificado | Quatro divisões, dois mundos, e validade no tempo | 7 min |
| [`MD-02`](MD-02-a-traducao-do-predio.md) | **A tradução do prédio** | verificado | O diagrama que converte o mundo real em SAP. **A nota mais importante** | 6 min |
| [`MD-03`](MD-03-parceiro-de-negocios.md) | Parceiro de Negócios | verificado | Categoria é o que ele é, função é o papel. Sem Parceiro de Contrato, não fatura | 7 min |
| [`MD-04`](MD-04-parceiro-de-negocios-dados.md) | PN, dados e customizing | verificado | Os seis blocos, os endereços, e as 17 transações de configuração | 8 min |
| [`MD-05`](MD-05-conta-contrato.md) | Conta Contrato | verificado | A bolsa financeira. E onde mora o bloqueio de corte | 7 min |
| [`MD-06`](MD-06-contrato.md) | **Contrato** | verificado | A dobradiça, as oito regras, e por que não existe "criar contrato" | 6 min |
| [`MD-07`](MD-07-move-in-move-out.md) | **Move-In e Move-Out** | a confirmar | O processo que cria o Contrato. **Fecha a maior lacuna do modelo** | 6 min |

### Dados mestres técnicos

| Código | Tema | Status | O gancho | Tempo |
|---|---|---|---|---|
| [`ST-01`](ST-01-objeto-de-ligacao.md) | Objeto de Ligação | verificado | O prédio. Nível mais alto, e onde mora o endereço | 5 min |
| [`ST-02`](ST-02-local-de-consumo.md) | Local de Consumo | verificado | O apartamento. Onde mora o complemento, não o endereço | 5 min |
| [`ST-03`](ST-03-instalacao.md) | **Instalação** | verificado | O objeto que fatura. Tarifa, unidade de leitura, validação | 6 min |
| [`ST-04`](ST-04-equipamento.md) | Equipamento e Registrador | misto | O medidor, o TC, as três formas de instalar. A parte do Registrador é a confirmar | 8 min |

**15 notas, cerca de 91 minutos lendo tudo. Cerca de 15 minutos lendo só os
recalls.**

---

## As quatro notas que mais valem

1. **[`GE-03`](GE-03-a-concessionaria.md)**, a concessionária. Sem o problema
   de negócio, o resto vira decoreba.
2. **[`MD-02`](MD-02-a-traducao-do-predio.md)**, a tradução do prédio.
   Metade da matéria num diagrama só.
3. **[`MD-06`](MD-06-contrato.md)**, o Contrato. O tema mais denso em regra.
4. **[`ST-03`](ST-03-instalacao.md)**, a Instalação. O objeto que fatura.

---

## Roteiro na ordem do aprendizado

`GE-03` → `GE-01` → `MD-01` → `MD-02` → então os dois ramos:

| Comercial | Técnico |
|---|---|
| `MD-03` → `MD-04` → `MD-05` | `ST-01` → `ST-02` → `ST-03` → `ST-04` |

E os dois convergem em **`MD-06`**, seguido de **`MD-07`**.

`GE-02` e `GE-04` são folhas soltas: leia quando quiser.

---

## Códigos de área

| Prefixo | Área |
|---|---|
| `GE` | Geral, negócio, produto |
| `MD` | Dados mestres comerciais |
| `ST` | Estrutura e dados mestres técnicos |
| `DM` `BI` `IN` `FI` `CS` `WM` | Reservados para os próximos temas |
