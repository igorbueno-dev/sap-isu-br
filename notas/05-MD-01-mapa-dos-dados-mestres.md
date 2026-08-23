# MD-01: As quatro divisões dos dados mestres
> Antes de comparar qualquer coisa, saber o que é cada uma. São quatro
> divisões, não duas, e a quarta não é dado mestre.

**Onde entra:** é o coração dos dados mestres.
**Antes disto:** [GE-01-o-que-e-is-u-ccs](02-GE-01-o-que-e-is-u-ccs.md)
**Depois disto:** [MD-08-os-dois-mundos](06-MD-08-os-dois-mundos.md)
**Origem:** **slide**, com uma exceção declarada na seção 1: a tabela de
tabelas de endereço vem do **pôster de tabelas IS-U**, não da aula, e a leitura que
liga essas tabelas à posição da Estrutura Postal na lista **é minha**.

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
quem a mantém é WM.** Ver [ST-01](11-ST-01-objeto-de-ligacao.md).

### As tabelas, conferidas fora do slide

**Estas não vêm da aula.** Vêm do pôster de tabelas IS-U, conferido em
21/08/2026, e estão reproduzidas na Bancada,
[`_BANCADA.md`](_BANCADA.md).

| Tabela | Conteúdo |
|---|---|
| `ADRCITY` | Cidades |
| `ADRPSTCODE` | Códigos postais |
| `ADRCITYPRT` | Distritos postais |
| `ADRSTREET` | Logradouros |
| `ADRCITYMRU` | **Unidades de leitura por cidade** |
| `ADRSTRTMRU` | **Unidades de leitura por logradouro** |
| `ADRCITYCCS` / `ADRSTRTCCS` | Dados de setor por cidade e por logradouro |
| `ADRCITYKON` / `ADRSTRTKON` | Contratos de concessão por cidade e por logradouro |

**As duas linhas em negrito são a chave.** As tabelas terminadas em `MRU` ligam
o endereço à **unidade de leitura**: é a estrutura postal que diz qual rota
atende cada rua.

**A leitura em cima disso é minha, e as tabelas a sustentam:** sem estrutura
postal não há roteirização, sem roteirização não há leitura, e sem leitura não
há faturamento. **É por isso que ela abre a lista** e não reaparece no resto dos
dados mestres.

> **O que continua em aberto:** as **transações** que mantêm essas tabelas, o
> nome que o projeto dá à estrutura, e a fronteira exata com a "Estrutura
> Regional". **O material coloca as estruturas postais e políticas sob WM**,
> então isso fecha na trilha de Serviço de Campo, não aqui. A pergunta segue na
> lista para o instrutor.

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

## Se sobrar uma coisa

São quatro divisões, e a quarta está na lista para servir de contraste.

---

## No sistema

As tabelas desta nota são as da **Estrutura Postal**, e estão na seção 1. As
duas que importam para o resto do acervo são `ADRCITYMRU` e `ADRSTRTMRU`, que
ligam o endereço à unidade de leitura.

**As transações que mantêm essas tabelas continuam em aberto.** As outras três
divisões têm transação própria, e elas moram nas notas de cada objeto.

---

## Recall

1. Quais são as quatro divisões dos dados mestres, na ordem?
2. Qual é o papel dos Dados Transacionais dentro dessa lista?
3. O que o material da aula diz sobre o conteúdo da Estrutura Postal?
4. A que área pertence a manutenção das estruturas postais?
5. Qual o critério que separa dado mestre de dado transacional?
6. Um imóvel foi construído e ninguém se mudou ainda. Qual divisão já tem dado?
7. Qual par de tabelas liga o endereço à unidade de leitura?
8. Cite o que esse par explica sobre a posição da Estrutura Postal na lista.
9. Uma rua nova foi cadastrada e as instalações dela não entraram em nenhuma ordem de leitura. Cite onde olhar.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#md-01)  ·  responda tudo antes de abrir.
