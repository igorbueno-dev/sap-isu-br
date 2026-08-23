# MD-04: Parceiro de Negócios, os dados e o customizing
> O que cabe dentro da ficha do cliente, e onde se desenha a ficha.

**Onde entra:** detalhe operacional do PN.
**Antes disto:** [MD-03-parceiro-de-negocios](08-MD-03-parceiro-de-negocios.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## Os seis blocos de dados

| Bloco | Conteúdo |
|---|---|
| **Dados Gerais** | Nome/Sobrenome; Número do Sistema; Categoria; Função (Papel); Status (Cliente, Prospect, Inativo) |
| **Identificação e Controle** | Sexo, Estado Civil, Nacionalidade; CPF, CNPJ; Tipo (Regular, Corporativo) |
| **Endereços e Comunicações** | End. Correspondência; **End. Local de Consumo**; telefone, celular, e-mail |
| **Dados de Pagamento** | Bancos, contas bancárias; **Solvência** (qualidade de pagador) |
| **Relações** | Entre Pessoas, Grupos e Organizações |
| **Características (Atributos)** | Classificação de VIPs; dados demográficos |

**Abas na tela:** `Endereço` · `Síntese de endereços` · `Identificação` ·
`Controle` · `Pagamentos` · `Status` · `Circular 380` · `Lista de utilizações`

---

## Endereços, a regra fina

- Endereços são armazenados **no Parceiro de Negócio**
- Um mesmo PN pode ter **mais de um endereço**
- Um deles deve ser marcado como **standard**, que é o de correspondência
  padrão quando não há um específico indicado
- O PN usa o **Cadastro Central de Endereços**
- **Endereços para diferentes funções podem ser associados no nível da
  Conta Contrato**

---

## Identificação fiscal brasileira

Bloco `Nºs identificação fiscal`, com flag `pessoa física` e tipo `BR2`
para `Brasil: nº CPF`.

---

## No sistema

**Duas transações de atalho:** `BUPT` para o parceiro de negócios,
`BUMR` para relacionamentos.
**E o `SPRO`**, que é o IMG inteiro.

Caminhos no IMG:
`Cross application components > SAP Business Partner`
`SAP Utilities > Master Data > Business Partner`

### As transações de configuração

| O que configura | Transação |
|---|---|
| Faixas de numeração | `BUCF` |
| Agrupamentos e atribuição de faixas | `BUC2` |
| Tipos de parceiro de negócios | `BUCD` |
| **Agrupamento de campos por função de PN** | `BUCG` |
| Tipo de endereço padrão por função | `BUC4` |
| Formas de tratamento | `BUC0` |
| Tipos de legitimação (documentos de identidade) | `BUCM` |
| Regras de formatação de nome | `SA13` |
| Estado civil | `BUCK` |
| Profissões | `BUCL` |
| Ramos de atividade | `BUCA` |
| Formas jurídicas | `BUC8` |
| Entidade legal | `BUC9` |
| Categoria de PN | `BUSO` |
| Categorias de relacionamento | `BUBA` |
| Layout de tela | `BUS5` |
| Faixas de numeração de relacionamento | `BUB9` |

---

## O erro que todo mundo comete

**Confundir configurar o campo com preencher o campo.**

`BUCK` não cadastra o estado civil da Dona Marta. Ele define **quais estados
civis existem** para escolher. Você desenha o formulário, o atendente
preenche.

Quando alguém disser "não consigo escolher a opção X", a resposta quase nunca
é no cadastro do cliente. É no customizing.

---

## Se sobrar uma coisa

O endereço mora no Parceiro de Negócios, e a tela dele é desenhada no customizing.

---

## Recall

1. Qual transação define agrupamentos e atribuição de faixas de numeração?
2. Qual transação define o tipo de endereço padrão por função?
3. Qual transação define as formas de tratamento?
4. Qual transação define as regras de formatação de nome?
5. Qual transação define as formas jurídicas?
6. Qual transação define a entidade legal?
7. Qual transação define o layout de tela?
8. Qual transação define as faixas de numeração de relacionamento?
9. Onde mora o endereço, no PN ou na Conta Contrato?
10. A conta do cliente está indo para o endereço errado. Cite onde olhar primeiro.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#md-04)  ·  responda tudo antes de abrir.
