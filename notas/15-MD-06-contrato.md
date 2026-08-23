# MD-06: Contrato
> A dobradiça do sistema. É o único objeto que toca o mundo comercial e o
> mundo técnico ao mesmo tempo.

**Onde entra:** o ponto de encontro dos dois mundos.
**Antes disto:** [MD-05-conta-contrato](10-MD-05-conta-contrato.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## A analogia

A Conta Contrato é a carteira. A Instalação é a tomada. **O Contrato é o
acordo que diz que aquela carteira paga por aquela tomada.**

Sem ele, você tem um cliente sem consumo e um consumo sem dono.

---

## As oito regras

**Este é o tema mais denso em regra que cai em prova. Decore.**

1. Representa um **acordo** entre o Parceiro de Negócio e a Empresa de Utility
2. **É criado durante o Move In**, e liga os dados mestres comerciais aos técnicos
3. Contém parâmetros para **cálculo de consumo** e para gerenciamento de recebíveis
4. Um PN pode ter várias Contas Contratos, que por sua vez podem ter vários
   Contratos alocados
5. **É o objeto que liga a Conta Contrato à Instalação**
6. **Um Contrato só pode estar ligado a UMA Conta Contrato e UMA Instalação**
7. Refere-se a uma empresa (Company Code) e a um único Setor de Atividade
8. **O Cálculo ocorre no nível do Contrato**

---

## A cardinalidade completa

```
Parceiro de     1 para N     Conta        1 para N
Negócios     ─────────────▶  Contrato  ─────────────▶  CONTRATO
                                                            │
                                                        1 para 1
                                                            ▼
                                                       Instalação
```

**De cima para baixo é um para muitos. Na ponta, é um para um.**

---

## Os três blocos de dados

| Bloco | Conteúdo |
|---|---|
| **Dados Gerais** | Conta de Contratos; indicador de faturamento conjunto; **Bloqueio do faturamento** |
| **Vigência** | Datas de início e fim de vigência; datas de renovação e de cancelamento |
| **Contabilização** | Chave de imposto ICMS; determinador de Classe Contábil |

---

## O erro que todo mundo comete

**Procurar a transação de criar contrato. Ela não existe.**

Olhe a lista de transações do Contrato: há `ES21` modificar, `ES22`
exibir, `ES27` modificar todos, `ES28` exibir todos. **Nenhuma de criar.**

Porque **o Contrato nasce do processo de Move In**, nunca de um cadastro
direto. Quem procura "criar contrato" no menu não vai achar, e vai concluir
errado que falta autorização.

---

## No sistema

| Transação | O quê |
|---|---|
| `ES21` | Modificar Contrato |
| `ES22` | Exibir Contrato |
| `ES27` | Modificar Todos Contratos |
| `ES28` | Exibir Todos os Contratos |

**Criar: só via Move In.** O material diz que *"o Contrato é criado durante o
Move In"* e não dá o código da transação. **O Move-In é processo de
atendimento (CIC), então a transação só aparece na trilha de CS + CRM.**

---

## Se sobrar uma coisa

Não existe transação de criar Contrato porque quem o cria é o Move-In.

---

## Recall

1. Qual transação modifica um Contrato?
2. Qual transação exibe um Contrato?
3. Qual transação modifica todos os contratos?
4. Qual transação exibe todos os contratos?
5. Quando o Contrato é criado?
6. Um contrato pode estar ligado a duas instalações?
7. Em que nível ocorre o cálculo?
8. O que cria o Contrato, já que não existe transação de criar?

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#md-06)  ·  responda tudo antes de abrir.
