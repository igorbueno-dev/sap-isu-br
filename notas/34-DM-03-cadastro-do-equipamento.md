# DM-03: O cadastro do equipamento, do material ao medidor instalado
> Um medidor não nasce medidor. Ele nasce material, ganha um tipo, vira
> equipamento, e só então pode ser instalado.

**Onde entra:** é a profundidade que a `DM-01` e a `DM-02` não tinham.
**Antes disto:** [DM-01](32-DM-01-ativos-e-estoque.md), [ST-04](14-ST-04-equipamento.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## Os quatro objetos, e o que cada um decide

| Objeto | O que é | O que decide |
|---|---|---|
| **Grupo de Registradores** | O conjunto de grandezas que o aparelho vai medir | **Quantos e quais registradores** o tipo terá |
| **Material** | O item de estoque, do lado do `MM` | De onde vem o aparelho fisicamente |
| **Tipo de Equipamento** | O modelo: fabricante, características técnicas | O que vale para **todos** os aparelhos daquele modelo |
| **Equipamento** | O aparelho individual, com número de série | O que vale para **aquele** aparelho |

**Registrador** é a grandeza que o aparelho acumula, e um equipamento pode ter
vários. Os seis tipos estão na [DM-02](33-DM-02-leituras-e-registradores.md).

---

## A corrente do cadastro

O material vem de um lado e o grupo de registradores do outro. Os dois se
encontram no tipo, o tipo gera o equipamento, e o equipamento entra na
instalação.

```
MEDIDOR                             TRANSFORMADOR
Grupo de Registradores  EG04        Grupo de Enrolamento  EGW1
Material                MM01        Material              MM01
        └──────┬──────┘                     └──────┬──────┘
   Tipo de Equipamento  EG01          Tipo de Equipamento  EG01
               │                                   │
        Medidor         IQ01          Transformador        IQ01
               └───────────────┬───────────────────┘
                  Grupo de Equipamentos   EG27
                  Instalação Total        EG31
                        ▼
                    INSTALAÇÃO
```

**Linha cheia é hierarquia, tracejada é sequência do processo.** É a legenda
do próprio slide, e a distinção importa: o tipo **está acima** do equipamento,
mas o grupo de equipamentos **vem depois** dele no tempo.

---

## Por que o transformador tem caminho próprio

**A coluna do transformador é igual à do medidor, com uma troca.** No lugar do
Grupo de Registradores entra o **Grupo de Enrolamento**. Faz sentido: o
transformador não acumula consumo, ele transforma tensão ou corrente, e o que
o caracteriza é o enrolamento, não o mostrador.

O resto é idêntico, inclusive a transação: **`IQ01` cria os dois**, porque para
o SAP os dois são equipamento.

> **Em aberto:** o que exatamente é um Grupo de Enrolamento. O termo apareceu
> só nesta caixa e não foi explicado. **Perguntar.**

---

## O erro que todo mundo comete

**Achar que criar o equipamento coloca ele em algum lugar.** Não coloca.

`IQ01` cria o aparelho no cadastro. Ele existe, tem número de série, e **não
está em lugar nenhum**. Quem o coloca na instalação é `EG31`, e mesmo assim só
se a modalidade for a certa. Ver [DM-04](35-DM-04-planejamento-de-datas.md) e
[ST-04](14-ST-04-equipamento.md).

---

## Na prática

**Chamado clássico:** "o medidor está no sistema mas não aparece na
instalação". Quase sempre é isso: alguém rodou `IQ01` e parou ali.

A sequência tem quatro paradas, e pular qualquer uma quebra a seguinte:
**material → tipo → equipamento → instalação.**

---

## No sistema

| Transação | O que cria |
|---|---|
| `EG04` | Grupo de Registradores |
| `EGW1` | Grupo de Enrolamento |
| `MM01` | Material |
| `EG01` | Tipo de Equipamento |
| `IQ01` | Equipamento: medidor ou transformador |
| `EG27` | Grupo de Equipamentos |
| `EG31` | Instalação total, que põe o equipamento na instalação |

---

## Se sobrar uma coisa

Criar o equipamento não instala o equipamento.

---

## Recall

1. Ordene, do primeiro ao último: Equipamento, Grupo de Registradores, Tipo de Equipamento, Material.
2. Qual transação cria o Grupo de Registradores?
3. Qual transação cria o Tipo de Equipamento?
4. Qual transação cria o Equipamento?
5. Qual transação cria o Grupo de Equipamentos?
6. Qual transação faz a instalação total?
7. Qual transação cria o material?
8. Como o SAP chama o objeto que substitui o Grupo de Registradores no caminho do transformador?
9. Um medidor foi criado no `IQ01` e não aparece na instalação. O que faltou?
10. O que o Grupo de Registradores decide?
11. O que separa Tipo de Equipamento de Equipamento?

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#dm-03)  ·  responda tudo antes de abrir.
