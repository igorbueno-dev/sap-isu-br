# DM-04: Planejamento de datas, quem carrega o calendário
> O cliente não escolhe quando é faturado. Quem carrega a data é o Conjunto de
> Contratos, e quem carrega a rota é a Unidade de Leitura.

**Onde entra:** fecha a lacuna que o acervo chamava de "planejamento de datas".
**Antes disto:** [MD-06](15-MD-06-contrato.md), [ST-03](13-ST-03-instalacao.md)

---

## Os dois objetos

| Objeto | Carrega | Responde |
|---|---|---|
| **Conjunto de Contratos** | Data de **cálculo** e data de **faturamento** | *Quando este cliente é calculado e cobrado* |
| **Unidade de Leitura** | Data de **leitura** e **localização** | *Quando e onde o medidor é lido* |

**A data da Unidade de Leitura é relativa à do conjunto**, não absoluta. No
material ela aparece como *"2 dias antes do cálculo"*. É esse encadeamento que
faz o calendário inteiro funcionar sem ninguém recalcular data à mão.

---

## Como eles se encaixam nos dois mundos

```
COMERCIAL                        TÉCNICO
Contrato  ─────────────────────  Instalação
    ▲                                │
    ┊ atribuição                  Medidor
    ┊
Conjunto de Contratos ──▶ Unidade de Leitura ──▶ volta para a Instalação
```

**O Conjunto de Contratos atribui-se ao Contrato**, do lado comercial. **A
Unidade de Leitura liga-se à Instalação**, do lado técnico. E o conjunto aponta
para a unidade.

É a segunda ponte entre os dois mundos, depois do Contrato. Ver
[MD-08](06-MD-08-os-dois-mundos.md).

---

## O exemplo do material, em números

Três conjuntos, com datas diferentes de propósito:

| Conjunto | Cálculo | Faturamento | Unidades de Leitura |
|---|---|---|---|
| `CJ001` | 1º dia útil | 1º dia útil | `SPBT0101` Centro · `SPBT0102` Sé |
| `CJ002` | 2º dia útil | 2º dia útil | `SPBT0201` Centro · `SPBT0202` Sé |
| `CJ003` | 1º dia útil | 1º dia útil | `SPMT0101` Centro · `SPMT0102` Sé |

**Por que datas diferentes:** faturar três milhões de clientes no mesmo dia não
cabe em nenhuma janela de processamento. Os conjuntos **distribuem a carga ao
longo do mês**, e é por isso que a conta do vizinho vence em outro dia.

---

## A Unidade de Leitura é geografia

No material ela é desenhada sobre o mapa do Recife: **Casa Forte** é `CJ001`,
**Casa Amarela** é `CJ002`, **Tamarineira** é `CJ003`. Dentro de cada bairro,
de três a cinco Unidades de Leitura.

E o corte é físico: numa rua com casas dos dois lados, **a metade de cá é uma
Unidade de Leitura e a metade de lá é outra**. É a rota do leiturista, não uma
divisão administrativa.

**O número de unidades por conjunto varia.** Não é cardinalidade fixa, é
desenho de operação.

---

## O erro que todo mundo comete

**Confundir os dois objetos porque os dois "têm data".**

Eles respondem perguntas diferentes: **o conjunto responde quando o dinheiro
acontece, a unidade responde quando o técnico anda.** Trocar um pelo outro num
chamado leva a mexer na régua de faturamento inteira quando o problema era só
uma rota.

---

## No sistema

| Passo | Transação |
|---|---|
| Cadastrar feriados e calendários | `SCAL` |
| Criar Conjunto de Contratos | `E41B` |
| Criar Unidade de Leitura | `E41H` |
| **Atribuir Instalação** | `ES31` ou `EL59` |
| Definir Grupo de Parâmetros | `EL59P` |
| Criar e atualizar Registro de Datas | `E1DY` e `E2DY` |
| Modificar Sequência de Leitura | `EL40` |
| Exibir Unidades de Leitura | `EL42` |

**O material destaca "Atribuir Instalação" em vermelho.** É o passo que liga o
planejamento ao objeto que fatura, e sem ele o resto é cadastro morto.

> **Inferência, a confirmar:** no vocabulário SAP em inglês estes dois objetos
> provavelmente são **Portion** e **Meter Reading Unit (MRU)**, tabelas `TE420`
> e `TE422`. O material nunca fez essa ligação em voz alta.

---

## Recall

1. Qual objeto carrega a data de faturamento, e qual carrega a data de leitura?
2. Por que existem vários Conjuntos de Contratos com datas diferentes?
3. Como a data da Unidade de Leitura é definida?
4. Qual transação cria o Conjunto de Contratos, e qual cria a Unidade de Leitura?
5. Duas casas na mesma rua estão em Unidades de Leitura diferentes. Isso é erro?

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#dm-04)  ·  responda tudo antes de abrir.
