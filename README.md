# SAP IS-U CCS, referência em português

Material de estudo sobre **SAP IS-U CCS** (*Industry Solutions for Utilities /
Customer Care Service*), a solução setorial que roda o ciclo comercial de
concessionárias de energia, água e gás.

Existe muito pouco conteúdo estruturado de IS-U em português. Este repositório
é uma tentativa de mudar isso, em aberto, com correção de quem conhece o
módulo na prática.

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
exigem quais. O mesmo grafo serve para achar buracos no modelo, e a lista de
buracos conhecidos está lá.

## O que este material assume sobre si mesmo

Nenhuma linha aqui pede que você confie nela sem checar. Duas marcas dizem o
grau de confiança:

- No índice, cada nota é **verificado** (conferido contra o sistema ou material
  de produto) ou **a confirmar** (escrito por raciocínio e leitura, ainda não
  conferido na documentação SAP).
- No texto, **(confirmar)** ao lado de um código de transação significa que não
  tenho certeza dele. Prefiro deixar a dúvida explícita a publicar um código
  errado com cara de certeza.

**Todo `(confirmar)` é um convite.** Se você roda IS-U em produção e sabe a
resposta, ela vale mais que uma semana de leitura minha.

## Como contribuir

O jeito mais útil de ajudar é **fechar um `(confirmar)`** ou corrigir algo que
está errado. Não precisa escrever nota nova.

- **[Corrigir conteúdo](../../issues/new?template=correcao-de-conteudo.yml)**,
  quando algo está errado ou incompleto
- **[Confirmar transação](../../issues/new?template=confirmar-transacao.yml)**,
  quando você sabe um código marcado como duvidoso
- Ver [`CONTRIBUTING.md`](CONTRIBUTING.md) para o resto

Pergunta também é contribuição: se algo aqui não fez sentido para você, é
provável que a nota esteja mal escrita, e isso vale uma issue.

## Aviso

Trabalho independente, sem vínculo com a SAP nem com qualquer empregador.
SAP, SAP IS-U e S/4HANA são marcas da SAP SE. Nada aqui reproduz material de
treinamento proprietário, e este repositório não é fonte oficial: para decisão
de projeto, consulte a documentação da SAP.
