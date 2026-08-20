# MD-01: As duas divisões dos dados mestres
> Os dados mestres se dividem em **técnicos** e **comerciais**: onde se consome
> e quem paga. Os **transacionais** não são uma terceira divisão, são o
> contraste que define as duas.

**Onde entra:** é o coração dos dados mestres.
**Antes disto:** [GE-01-o-que-e-is-u-ccs](GE-01-o-que-e-is-u-ccs.md)
**Depois disto:** [MD-08-os-dois-mundos](MD-08-os-dois-mundos.md)

> **Correção de 20/08/2026.** Uma versão anterior desta nota abria com quatro
> divisões, sendo "Estrutura Postal" a primeira. **O material não menciona
> Estrutura Postal.** Aquilo era texto meu que assumiu posição estrutural sem
> ter direito a ela. O que restou dele está no fim desta nota, fora da
> taxonomia. **Se você ouviu os episódios 2 e 4, eles ainda carregam o erro.**

---

## A definição

> "Dados Mestre para o CCS são os cadastros necessários para o funcionamento
> do sistema."

O material segrega assim:

- **Dados Mestres**, e dentro deles duas divisões:
  1. Dados Mestre Técnicos
  2. Dados Mestre Comercial
- **Dados Transacionais**, que ficam **fora** dos dados mestres.

Os transacionais aparecem na mesma tela porque é **por oposição a eles** que se
entende o que é um cadastro. Não são uma divisão, são o contraste.

---

# As duas divisões

## 1. Dados Mestres Técnicos

**Onde se consome.** Descrevem o imóvel e a rede: o prédio, o apartamento, o
ponto que mede, o medidor pendurado nele.

Objetos: Objeto de Ligação, Local de Consumo, Instalação, Equipamento, Local de Instalação de Equipamento.

**Não têm dono:** existem mesmo com o imóvel vazio.

## 2. Dados Mestres Comerciais

**Quem paga.** Descrevem a pessoa, a bolsa de dinheiro dela e o vínculo entre
ela e o que consome.

Objetos: Parceiro de Negócio, Conta Contrato e Contrato.

**Não têm lugar.** O Parceiro de Negócio existe sem endereço de fornecimento.

---

# O contraste: Dados Transacionais

**O que aconteceu.** Nascem da execução dos processos: a leitura de agosto, a
conta de agosto, o pagamento de setembro. São o **movimento** que corre por
cima dos dois cadastros anteriores.

---

# Agora sim, as comparações

## Mestre x transacional

| | **Dados Mestres** | **Dados Transacionais** |
|---|---|---|
| O que são | Cadastros usados pelo sistema (cliente, endereços) | Criados na execução dos processos (leitura, faturamento, recebíveis) |
| Duração | **Inalterados por longo período**, e nesse período são a única versão válida | **Dinâmicos**, válidos por curto período |
| Exemplo | O cadastro da Dona Marta | A leitura de agosto e a conta de agosto |

**O critério é duração de validade, não importância.**

## Comercial x técnico

| | **Comerciais** | **Técnicos** |
|---|---|---|
| Pergunta que respondem | **Quem paga** | **Onde se consome** |
| Objetos | Parceiro de Negócio, Conta Contrato, Contrato | Objeto de Ligação, Local de Consumo, Instalação, Equipamento, Local de Instalação |
| Nascem de | Um cliente chegar | Uma obra ficar pronta |
| Mudam quando | A pessoa muda: mudança, titularidade, forma de pagamento | O imóvel ou a rede muda: obra, troca de medidor |
| Acompanham | **A pessoa** | **O imóvel** |
| Quem mexe no dia a dia | Atendimento, `CS + CRM` | Campo e operação, `WM` e `DM` |
| Se sumissem | O imóvel continua ligado e ninguém é cobrado | O cliente existe e não há o que faturar |
| Ponto de encontro | O **Contrato** | A **Instalação** |

**Leia a última linha duas vezes.** Os dois mundos se tocam num ponto só, e é disso que trata a [MD-08](MD-08-os-dois-mundos.md).

---

## Recall

1. Quais são as duas divisões dos dados mestres, e que pergunta cada uma responde?
2. Por que os dados transacionais aparecem junto de uma lista de dados mestres,
   se não são um deles?
3. Qual o critério que separa dado mestre de dado transacional?
4. Um imóvel foi construído e ninguém se mudou ainda. Qual divisão já tem dado,
   e qual não tem?
5. Se os dados mestres comerciais sumissem, o que acontece com o imóvel? E se
   sumissem os técnicos?

> **Gabarito:** [`_GABARITOS.md`](_GABARITOS.md#md-01)  ·  responda tudo antes de abrir.

---

## Fora da taxonomia: de onde vem o endereço

> **Isto não está no material e não é uma divisão dos dados mestres.** Está
> aqui só para não perder o raciocínio, e precisa de confirmação com o
> instrutor antes de virar qualquer coisa.

Em IS-U o endereço do Objeto de Ligação normalmente **aponta para uma estrutura
regional** de país, estado, município, bairro, logradouro e CEP, em vez de ser
texto livre. Se isso vale no projeto e como se chama ali, **perguntar**.

---

## Ligações

[MD-08-os-dois-mundos](MD-08-os-dois-mundos.md) · [MD-02-a-traducao-do-predio](MD-02-a-traducao-do-predio.md) · [MD-03-parceiro-de-negocios](MD-03-parceiro-de-negocios.md) · [ST-01-objeto-de-ligacao](ST-01-objeto-de-ligacao.md)
