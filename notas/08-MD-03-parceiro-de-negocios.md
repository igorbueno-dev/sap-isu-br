# MD-03: Parceiro de Negócios, categoria e função
> Quem é a pessoa, e qual papel ela cumpre. São duas perguntas diferentes,
> e o SAP guarda as duas em campos diferentes.

**Onde entra:** primeiro objeto do mundo comercial.
**Antes disto:** [MD-01-mapa-dos-dados-mestres](05-MD-01-mapa-dos-dados-mestres.md)

---

## A analogia

Pense num crachá. **A categoria** é o que está escrito no documento de
identidade: pessoa física ou empresa. **A função** é o que está escrito no
crachá: cliente, funcionário, contato.

A mesma pessoa pode ter vários crachás. Mas o documento é um só.

---

## O que o PN pode ser

- Pode representar um cliente, um funcionário, um fornecedor
- Pode ser uma pessoa, um grupo ou uma organização

## As três CATEGORIAS

| Categoria | Definição |
|---|---|
| **Pessoa** | Todos os indivíduos que tenham alguma relação com a empresa |
| **Organização** | Unidade jurídica: empresa, departamento, sociedade ou associação |
| **Grupo** | Pessoas compartilhando um apartamento, membros de uma empresa. **Normalmente não é utilizada** |

**Para Parceiro de Negócio de Contrato, só duas são usadas: Pessoa e
Organização.**

### O que a categoria decide

**Quais campos aparecem na tela.** Escolhendo "organização" aparece Status
Legal e a formatação do nome muda. Escolhendo "pessoa" você define
nome e sobrenome.

A categoria também limita **quais relacionamentos** estão disponíveis. O tipo
"Tem a pessoa de contato" só existe para categoria organização.

---

## As FUNÇÕES

| Função | O que é |
|---|---|
| **Parceiro de Contrato** | **A função mais usual e a necessária para faturar o cliente.** Clientes residenciais, comerciais e industriais, pagadores alternativos, recebedores alternativos de fatura |
| **Pessoa de Contato** | Representante de uma organização. **Este PN não terá contrato associado** |
| **Empregado** | Da própria empresa de Utility |
| **Cliente Potencial** | Usado em relatórios e iniciativas de Marketing |

---

## Cliente SD

Ao criar um Parceiro de Contrato ou um Cliente Potencial, é possível também
criar um **Cliente Standard em SD** (Sales & Distribution). O cliente standard
pode utilizar serviços, comprar materiais e pagar multas e impostos.

Na criação, um **cliente de referência/modelo** é utilizado.

---

## O erro que todo mundo comete

**Confundir categoria com função.**

- "Ele é Pessoa ou Organização?" → **categoria**
- "Ele é Parceiro de Contrato ou Pessoa de Contato?" → **função**

E a consequência prática que cai na prova: **sem a função Parceiro de
Contrato, não fatura.** Um PN pode existir lindo no sistema e nunca gerar
conta, porque tem só a função de Pessoa de Contato.

---

## No sistema

| Transação | O quê |
|---|---|
| `FPP1` ou `BP` | Criar PN |
| `FPP2` ou `BP` | Modificar PN |
| `FPP3` ou `BP` | Exibir PN |

Ver [MD-04-parceiro-de-negocios-dados](09-MD-04-parceiro-de-negocios-dados.md) para abas, endereços e customizing.

---

## Se sobrar uma coisa

Categoria é o que o parceiro é. Função é o papel que ele cumpre.

---

## Recall

1. Qual transação cria um Parceiro de Negócios?
2. Qual transação modifica um Parceiro de Negócios?
3. Qual transação exibe um Parceiro de Negócios?
4. Nomeie as três categorias de Parceiro de Negócios.
5. Qual das três categorias quase não se usa?
6. Qual função é obrigatória para faturar o cliente?
7. O que separa categoria de função?
8. Você criou um PN e ele não fatura. Cite a primeira hipótese.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#md-03)  ·  responda tudo antes de abrir.
