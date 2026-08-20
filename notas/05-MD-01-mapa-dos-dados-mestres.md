# MD-01: As quatro divisões dos dados mestres
> Antes de comparar qualquer coisa, saber o que é cada uma. São quatro
> divisões, não duas, e a quarta não é dado mestre.

**Onde entra:** é o coração dos dados mestres.
**Antes disto:** [GE-01-o-que-e-is-u-ccs](02-GE-01-o-que-e-is-u-ccs.md)
**Depois disto:** [MD-08-os-dois-mundos](06-MD-08-os-dois-mundos.md)

---

## A definição

> "Dados Mestre para o CCS são os cadastros necessários para o funcionamento
> do sistema."

**Como estão divididos os dados?** São **quatro**, nesta ordem:

1. Estrutura Postal
2. Dados Mestre Técnicos
3. Dados Mestre Comercial
4. Dados Transacionais

A quarta **não** é dado mestre, e mesmo assim está na lista. É proposital:
ela está ali para servir de contraste.

**O objetivo declarado do bloco:** entender como esses dados estão
representados no sistema, e como eles se relacionam.

---

# As quatro, uma a uma

## 1. Estrutura Postal

**O material nomeia a divisão e nunca abre uma seção para ela.** O que se sabe
vem de duas menções em outros pontos:

- O **Objeto de Ligação** *"relaciona-se ao Local de Consumo e ao Local de
  Instalação do Equipamento e também às **Estruturas Regionais, Postais e
  Políticas**"*, e seu campo relevante é o **Endereço**
- Entre as responsabilidades de **WM** está *"manter estruturas políticas e
  postais (de endereço)"*

Junte as duas: **é onde o endereço mora, o Objeto de Ligação se liga a ela, e
quem a mantém é WM.** É por isso que ela abre a lista e não reaparece no
resto dos dados mestres. Ver [ST-01](11-ST-01-objeto-de-ligacao.md).

> **Lacuna estrutural, não pendência.** O conteúdo da estrutura, as transações
> e a relação com "Estrutura Regional" são aprofundamento, e a semana 1 é
> panorâmica por desenho. **O material coloca as estruturas postais e políticas
> sob WM**, então isso só fecha na trilha de Serviço de Campo. **Não preencha
> por dedução.**

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
cima dos cadastros anteriores.

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

**Leia a última linha duas vezes.** Os dois mundos se tocam num ponto só, e é disso que trata a [MD-08](06-MD-08-os-dois-mundos.md).

---

## Recall

1. Quais são as quatro divisões, na ordem?
2. Por que os dados transacionais aparecem numa lista de dados mestres?
3. O que o material diz sobre a Estrutura Postal, e a que área ela pertence?
4. Qual o critério que separa dado mestre de dado transacional?
5. Um imóvel foi construído e ninguém se mudou ainda. Quais divisões já têm
   dado, e quais não?

> **Gabarito:** [`_GABARITOS.md`](_GABARITOS.md#md-01)  ·  responda tudo antes de abrir.
