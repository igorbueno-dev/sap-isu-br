# SAP IS-U CCS, notas de estudo

Notas em português sobre **SAP IS-U CCS** (*Industry Solutions for Utilities /
Customer Care Service*), a solução setorial que roda o ciclo comercial de
concessionárias de energia, água e gás.

Material de estudo pessoal, escrito enquanto aprendo o módulo. Publicado porque
quase não existe conteúdo estruturado de IS-U em português.

## Por onde começar

| Quero | Vou em |
|---|---|
| **Estudar** | [`notas/_INDICE.md`](notas/_INDICE.md), a porta de entrada das 15 notas |
| Entender o todo em 2 minutos | [`00-NUCLEO.md`](00-NUCLEO.md) |
| Saber em que ordem estudar | [`notas/_DEPENDENCIAS.md`](notas/_DEPENDENCIAS.md) |
| Achar uma transação ou tabela | [`02-BANCADA.md`](02-BANCADA.md) |
| Aprofundar FI-CA | [`FI-CA-detalhado.md`](FI-CA-detalhado.md) |

Se for ler só uma coisa, leia [`notas/MD-02`](notas/MD-02-a-traducao-do-predio.md).
É o diagrama que traduz um prédio de verdade nos objetos do sistema, e resolve
metade da confusão inicial com dados mestres.

## Como o material é organizado

**Notas atômicas.** Cada nota em `notas/` cobre um conceito só: 5 a 10 minutos
de leitura, teto de 120 linhas, terminando em raciocínio fechado. Se cresce,
vira duas. A navegação é sempre pelo índice, nunca pela listagem de pasta.

**Cada nota termina em recall.** Perguntas sem resposta à vista. Os gabaritos
ficam separados em [`notas/_GABARITOS.md`](notas/_GABARITOS.md), para você
responder antes de conferir.

**Grafo de dependências.** A ordem de estudo não é opinião: está em
[`notas/_DEPENDENCIAS.md`](notas/_DEPENDENCIAS.md), derivada de quais conceitos
exigem quais. O mesmo grafo serve para achar buracos no modelo.

## Sobre a confiabilidade

O índice marca cada nota com um status:

- **verificado**, conferido contra o sistema ou material de produto
- **a confirmar**, escrito por raciocínio e leitura, ainda não conferido na
  documentação SAP

O material também usa **(confirmar)** ao lado de códigos de transação de que
não tenho certeza. Prefiro deixar a dúvida explícita a publicar um código
errado com cara de certeza.

**Correção é bem-vinda.** Se você trabalha com IS-U e viu um erro, abra uma
issue. É a razão de isto estar público.

## Aviso

Trabalho pessoal, sem vínculo com a SAP nem com qualquer empregador. SAP,
SAP IS-U e S/4HANA são marcas da SAP SE. Nada aqui reproduz material de
treinamento proprietário, e este repositório não é fonte oficial: para decisão
de projeto, consulte a documentação da SAP.
