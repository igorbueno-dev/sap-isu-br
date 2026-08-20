# PADRÃO DA NOTA
### O esqueleto, e as regras que impedem ele de derreter

> **Por que este arquivo existe.** As 31 primeiras notas foram escritas sem
> esqueleto, uma de cada vez. O resultado: **127 títulos de seção distintos, e
> 119 deles aparecem numa nota só.** Não havia forma comum, então não dava
> para folhear o acervo, só para ler nota por nota.
>
> O padrão abaixo foi extraído da [`GE-01`](notas/02-GE-01-o-que-e-is-u-ccs.md), que é
> a nota que funciona.

---

## O princípio

**O título faz a pergunta. O resumo responde. Todo o resto acrescenta.**

Se uma seção reformula o que o resumo já disse, ela sai. Repetição não é
reforço: é o leitor gastando atenção para descobrir que não ganhou nada.

---

## As zonas obrigatórias

Sempre presentes, sempre nesta ordem.

| # | Zona | Papel |
|---|---|---|
| 1 | **Título** | A pergunta. `XX-NN: <o assunto>` |
| 2 | **Resumo** | A resposta, em **uma frase**. Objetiva, não provocativa |
| 3 | **Estrutura** | O elemento central: a figura, a hierarquia, a tabela que organiza |
| 4 | **Onde quebra** | O erro que se comete. Único lugar da nota com cor |
| 5 | **No sistema** | Transações e tabelas |
| 6 | **Pistas** | As perguntas de recuperação |
| 7 | **Se sobrar** | A tese que precisa sobreviver ao esquecimento |

### A regra da seção vazia

**Seção obrigatória sem conteúdo se declara vazia. Não some.**

A `GE-01` faz isso certo: *"Não há transação desta nota. Ela é conceitual."*

O leitor precisa saber que a ausência foi **verificada**, não esquecida. Seção
que some em silêncio é conceito suprimido, e conceito suprimido é o que
quebra a contextualização de quem está aprendendo sozinho.

---

## As zonas condicionais

Entram **só quando ganham o espaço**. Nunca por simetria.

| Zona | Entra quando | Exemplo |
|---|---|---|
| **Vocabulário** | Há nomes ou siglas a fixar | `GE-01`, as duas siglas |
| **Características** | O objeto tem atributos que valem lista | `MD-03` Parceiro de Negócios, `MD-06` Contrato |
| **Analogia** | Passa no teste abaixo | `MD-06`, a carteira e a tomada |

### O teste da analogia

**A analogia só sobrevive se o resumo não a contiver.**

Ela precisa entregar pelo menos uma destas três coisas:

- **um teste**: "se existe um poste alimentando aquilo, existe um Objeto de Ligação"
- **um contraste**: o que a coisa **não** é
- **uma corrente**: liga este objeto a outro já conhecido

Analogia que só traduz o resumo em metáfora é a segunda cópia da mesma frase.
`ST-02` dizia *"É o apartamento"* logo abaixo de um resumo que já dizia *"o
apartamento dentro do prédio"*.

---

## As pistas

**Uma pergunta, uma resposta.** Se dá para responder pela metade, são duas
perguntas. Nada de `e` juntando dois pedidos.

Toda pista tem que ser uma destas cinco formas:

| Forma | Exemplo |
|---|---|
| **Nomeia** | "Como o SAP chama o prédio?" |
| **Transação** | "Qual transação cria uma Instalação?" |
| **Ordena** | "Ordene do que contém para o contido: Instalação, Local de Consumo, Objeto de Ligação" |
| **Diagnostica** | "A instalação não faturou. Cite três causas possíveis." |
| **Distingue** | "O que separa Billing de Invoicing?" |

**Fora da lista, não entra.** Isso mata por construção três defeitos que o
acervo tinha: pergunta binária com 50% de chute, pergunta começando com "por
que" que só pede a reprodução de um parágrafo, e pergunta sobre a própria
nota em vez de sobre o SAP.

### A regra de cobertura

**Todo código de transação citado no corpo vira pista da forma _Transação_.**

O acervo tinha 50 códigos citados e **duas** pistas que os cobravam. Para vaga
de analista funcional, transação é o conteúdo mais provável de ser cobrado, o
mais objetivo de corrigir e o mais impossível de blefar.

---

## As figuras

**A figura codifica a relação, não ilustra o assunto.** Cada tipo de relação
já tem uma forma que funciona em texto puro:

| A relação é | A forma |
|---|---|
| Sequência | Uma linha: `A → B → C` |
| Cardinalidade | Na seta: `A ──1:N──▶ B` |
| Contém, hierarquia | Lista indentada, porque a indentação **é** a contenção |
| Ciclo | Sequência indentada, com `↺` no retorno e `■` no fim |
| Dois mundos com ponte | Duas colunas alinhadas, ponte na linha do encontro |
| Linha do tempo | Tabela, uma linha por marco |

**Quando a figura usa notação, uma legenda curta vem antes dela.** Ninguém
deve precisar adivinhar o que `1:N` quer dizer.

Diagrama renderizado só se ganhar do texto. Uma cadeia de quatro caixas perde:
a linha de texto é mais rápida de bater o olho e não depende de renderizador.

---

## Formatação

**Negrito marca o termo sendo definido, ou a única afirmação que precisa
sobreviver. Nada mais.** O acervo chegou a uma marcação a cada 4 linhas, com
notas em que 38% das linhas tinham negrito. Quando quase tudo está destacado,
nada está.

**Cor marca uma coisa só: a armadilha.** Se aparecer cor, significa "aqui você
erra". Cor em cinco lugares diferentes não orienta ninguém.

**Sem pauta de caderno, sem caixa decorativa, sem ícone de seção.** Todo
elemento visual que não codifica informação compete com o conteúdo.

---

## O que este padrão não faz

**Não impõe teto de linhas.** Houve uma regra de 120 linhas e ela virou alvo:
a mediana ficou em 103 e onze notas encostaram no teto. Pior, ela levou a
cortar conceito para caber.

A nota tem o tamanho que o assunto pedir. **Quem controla o esforço do leitor
é a leitura em camadas**, não o corte: resumo em dez segundos, pistas em dois
minutos, corpo inteiro quando precisar.
