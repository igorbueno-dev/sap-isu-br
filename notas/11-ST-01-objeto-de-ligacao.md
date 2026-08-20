# ST-01: Objeto de Ligação
> A edificação conectada à rede. O nível mais alto dos dados mestres técnicos,
> e onde mora o endereço.

**Em inglês:** `Connection Object`. Use o nome em inglês quando a tradução em
português divergir entre materiais.
**Onde entra:** o topo do mundo técnico.
**Antes disto:** [MD-01-mapa-dos-dados-mestres](05-MD-01-mapa-dos-dados-mestres.md)

---

## O teste de campo

**Se existe um poste alimentando aquilo, existe um Objeto de Ligação.**
É o ponto onde a rua encosta no imóvel.

---

## O que é

- Representa uma **edificação ou propriedade conectada à rede elétrica**
- Na maioria dos casos, **estabelece o ponto de entrada do fornecimento**
- É criado quando surge uma nova edificação ou propriedade à qual será
  fornecida energia elétrica
- **É onde se registra o endereço da unidade consumidora**
- **É o nível mais alto dos Dados Mestres Técnicos.** Relaciona-se ao Local de
  Consumo, ao Local de Instalação do Equipamento e também às **Estruturas
  Regionais, Postais e Políticas**
- **Campo relevante: Endereço**

---

## Exemplos

Residência · Edifício · Fornecimento temporário · Torres de Telefonia ·
Outdoors · Bancas de Jornal

**Repare que não é só prédio.** É qualquer coisa que encosta na rede. Um
outdoor tem Objeto de Ligação. Uma banca de jornal tem.

A regra visual é simples: **cada número predial é um
Objeto de Ligação separado**, mesmo em edificações coladas na mesma quadra.

---

## O erro que todo mundo comete

**Confundir onde fica o endereço e onde fica o complemento.**

- **Objeto de Ligação** guarda o **endereço**: rua, número, CEP
- **Local de Consumo** guarda o **complemento**: andar, número do apartamento

É pergunta clássica de prova, e é a diferença entre achar e não achar um
cliente na busca.

---

## Na prática

| Transação | O quê |
|---|---|
| `ES55` | Criar Objeto de Ligação |
| `ES56` | Modificar Objeto de Ligação |
| `ES57` | Exibir Objeto de Ligação |

Caminho: `Serviços públicos > Dados mestre técnicos > Objeto de ligação`

**Exercício:** criar um novo objeto de ligação e modificar a classe
do objeto criado.

---

## Recall

1. Qual campo é o relevante do Objeto de Ligação?
2. Ele é o nível mais alto ou mais baixo dos dados mestres técnicos?
3. Dois sobrados colados, com números prediais diferentes. Um ou dois objetos
   de ligação?

> **Gabarito:** [`_GABARITOS.md`](_GABARITOS.md#st-01)  ·  responda tudo antes de abrir.
