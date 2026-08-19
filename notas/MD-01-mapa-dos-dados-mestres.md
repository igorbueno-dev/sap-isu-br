# MD-01: As quatro divisões dos dados mestres
> Antes de comparar qualquer coisa, saber o que é cada uma. São quatro
> divisões, não duas, e a que quase ninguém explica é a primeira.

**Onde entra:** é o coração dos dados mestres.
**Antes disto:** [GE-01-o-que-e-is-u-ccs](GE-01-o-que-e-is-u-ccs.md)
**Depois disto:** [MD-08-os-dois-mundos](MD-08-os-dois-mundos.md)

---

## A definição

> "Dados Mestre para o CCS são os cadastros necessários para o funcionamento
> do sistema."

São **quatro** divisões, não duas:

1. Estrutura Postal
2. Dados Mestre Técnicos
3. Dados Mestre Comercial
4. Dados Transacionais

Repare que a quarta **não** é dado mestre, e mesmo assim está na lista. É
proposital: ela está ali para servir de contraste.

---

# As quatro, uma a uma

## 1. Estrutura Postal

**Onde os endereços moram, antes de qualquer cliente existir.**

É o cadastro de país, estado, município, bairro, logradouro e CEP, montado uma
vez e reaproveitado pelos outros objetos. Quando o Objeto de Ligação recebe um
endereço, ele não digita texto livre: **aponta para uma entrada desta
estrutura.** Por isso vem primeiro. É a fundação embaixo da fundação.

> **Status: escrito por mim, a confirmar.** Esta divisão é quase sempre
> listada e quase nunca explicada. O que está acima é o funcionamento padrão
> de estrutura regional em IS-U, montado por leitura, não conferido.
>
> **Em aberto:** se "Estrutura Postal" e "Estrutura Regional" são a mesma
> coisa ou duas metades, postal e política, e quais as transações.

**Na prática:** endereço errado é erro de estrutura, não de digitação. E como ela
alimenta rota de leitura, bairro mal cadastrado vira leiturista rodando errado.

## 2. Dados Mestres Técnicos

**Onde se consome.** Descrevem o imóvel e a rede: o prédio, o apartamento, o
ponto que mede, o medidor pendurado nele.

Objetos: Objeto de Ligação, Local de Consumo, Instalação, Equipamento, Local de Instalação de Equipamento.

**Não têm dono:** existem mesmo com o imóvel vazio.

## 3. Dados Mestres Comerciais

**Quem paga.** Descrevem a pessoa, a bolsa de dinheiro dela e o vínculo entre
ela e o que consome.

Objetos: Parceiro de Negócio, Conta Contrato e Contrato.

**Não têm lugar.** O Parceiro de Negócio existe sem endereço de fornecimento.

## 4. Dados Transacionais

**O que aconteceu.** Nascem da execução dos processos: a leitura de agosto, a
conta de agosto, o pagamento de setembro. São o **movimento** que corre por
cima dos três cadastros anteriores.

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

1. Quais são as quatro divisões, na ordem?
2. Por que os dados transacionais aparecem numa lista de dados mestres?
3. O que é a Estrutura Postal, e por que ela vem antes das outras?
4. Qual o critério que separa dado mestre de dado transacional?
5. Um imóvel foi construído e ninguém se mudou ainda. Quais divisões já têm
   dado, e quais não?

> **Gabarito:** [`_GABARITOS.md`](_GABARITOS.md#md-01)  ·  responda tudo antes de abrir.

---

## Ligações

[MD-08-os-dois-mundos](MD-08-os-dois-mundos.md) · [MD-02-a-traducao-do-predio](MD-02-a-traducao-do-predio.md) · [MD-03-parceiro-de-negocios](MD-03-parceiro-de-negocios.md) · [ST-01-objeto-de-ligacao](ST-01-objeto-de-ligacao.md)
