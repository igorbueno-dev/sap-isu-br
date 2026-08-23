# GE-01: O que é o SAP IS-U CCS

> O conjunto de módulos que roda o ciclo comercial de uma concessionária,
> do cadastro do cliente até o dinheiro entrar.

**Onde entra:** é a moldura de tudo. Comece por aqui.
**Depois disto:** [GE-02-evolucao-do-produto](03-GE-02-evolucao-do-produto.md), [MD-01-mapa-dos-dados-mestres](05-MD-01-mapa-dos-dados-mestres.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## As duas siglas


| Sigla    | Expansão            |
| ---------- | ------------------------------------ |
| **CCS**  | *Customer Care Service*            |
| **IS-U** | *Industry Solutions for Utilities* |

São o mesmo produto, dois nomes. CCS é o nome funcional do conjunto; IS-U é
como a solução aparece no sistema.

## Características

- **É a camada que ensina o ERP a ser concessionária.** Um ERP comum sabe
  vender produto e fechar balanço; não sabe o que fazer com um medidor na
  parede de dez milhões de casas, cada um gerando uma conta diferente por mês
- Agrupamento de módulos que suporta o **ciclo comercial** de empresas de
  Utilities (água, energia, gás e outros)
- **É integrado** com os demais módulos do SAP ECC: FI, MM, PM
- É mais direcionado para o mercado de **varejo de energia**
- **Uma implementação de IS-U costuma ser várias vezes maior que um projeto
  de ERP convencional**
- **Não é um sistema à parte.** É solução setorial **dentro** do ERP, e
  reutiliza a contabilidade, os custos, os materiais e a manutenção que já
  estão lá. Quem trata IS-U como sistema separado procura no lugar errado
  quando o problema é de um módulo vizinho

---

## As cinco áreas funcionais

**Decore esta lista. É a espinha do módulo e a base das especializações.**

```
CS + CRM  ──▶  WM  ──▶  DM  ──▶  BILL  ──▶  FI-CA
Atendimento    Serviço  Equipa-  Fatura-   Arrecadação
               de Campo mento e  mento e   e Cobrança
                        Leitura  Impressão
    │           │        │        │          │
    └───────────┴────────┴────────┴──────────┘
                         │
         BW, Business Warehouse: informações gerenciais
         atravessa as cinco, e não é uma delas
```


| Área        | O que faz                                                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **CS + CRM** | Tela de atendimento, interações, nova ligação, religação, mudança de nome                                                   |
| **WM**       | Notas de serviço de campo, solicitações interdepartamentais, cadastro técnico e de endereços                                  |
| **DM**       | Cadastro de equipamentos, validação de medições, instalação, troca, certificação, calendário e roteirização de leituras |
| **BILL**     | Regras tarifárias, preços, descontos, impostos, faturamento e impressão de faturas                                              |
| **FI-CA**    | Pagamentos, vencimentos, multas, juros, contabilização, recebíveis, cobrança, corte, parcelamento                              |

**BW atravessa as cinco, mas não é uma delas.**

---

## O erro que todo mundo comete

**Achar que BW é a sexta área.** Não é. BW aparece como uma faixa
horizontal por baixo das cinco setas, não como uma sexta seta.

É por isso que **BW não é uma trilha do CCS** e não tem vaga: ele não faz
parte do produto, ele lê o produto.

---

## Na prática

Não há transação desta nota. Ela é conceitual.
Ver [`_BANCADA.md`](_BANCADA.md) para as transações.

**A pergunta que vale para o projeto inteiro: isso é padrão ou é nosso?**

Muito do que aparece na tela de um projeto de Utilities é **customização**, e
quatro áreas concentram quase toda ela: **tarifa, layout de fatura, integração
bancária e aplicativo de campo**. Tratar customização como padrão faz procurar
documentação da SAP para um comportamento que só existe naquele cliente, e faz
prometer ao cliente um comportamento que o projeto dele não tem.

---

## Se sobrar uma coisa

O CCS são cinco áreas em cadeia, e o BW não é uma delas.

---

## Recall

1. Escreva a expansão de CCS.
2. Escreva a expansão de IS-U.
3. Ordene as cinco áreas funcionais na ordem da cadeia.
4. Onde o BW aparece no desenho das cinco áreas?
5. O que separa o BW das cinco áreas funcionais?
6. Qual é a relação entre o IS-U e o ERP?
7. Nomeie as quatro áreas que concentram a customização num projeto de Utilities.
8. Um comportamento da tela não bate com a documentação da SAP. Cite a pergunta a fazer antes de abrir chamado.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#ge-01)  ·  responda tudo antes de abrir.
