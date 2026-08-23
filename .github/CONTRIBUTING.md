# Como contribuir

Este material existe porque falta conteúdo de SAP IS-U em português. Toda
correção melhora ele para a próxima pessoa que chegar perdida no mesmo ponto.

**Você não precisa escrever nada grande.** As contribuições mais valiosas são
as menores.

---

## As três coisas mais úteis que você pode fazer

### 1. Fechar um `(confirmar)`

O material marca com **(confirmar)** todo código de transação de que eu não
tenho certeza. Se você roda IS-U e sabe a resposta, isso é ouro.

Use o template **Confirmar transação**. O que importa é dizer **como você sabe**:
viu no sistema, está na documentação, usa no dia a dia.

### 2. Corrigir o que está errado

Conceito trocado, relação invertida, tabela com nome errado. Use o template
**Correção de conteúdo** e diga onde está e o que deveria ser.

Se você tem fonte, ótimo. Se é experiência de projeto, também vale: diga que é
experiência, e eu marco como tal.

### 3. Dizer que uma nota não fez sentido

Se você leu e não entendeu, **a nota está mal escrita**. Não é falha sua e não
é reclamação: é o defeito mais difícil de enxergar sozinho, porque quem
escreveu já sabe o assunto.

Abra uma issue dizendo onde travou.

---

## A regra que sustenta o material

**Toda afirmação carrega seu grau de confiança.**

| Marca | Significa |
|---|---|
| `verificado` no README | Conferido contra o sistema ou material de produto |
| `a confirmar` no README | Escrito por raciocínio e leitura, não conferido |
| `(confirmar)` no texto | Código ou detalhe específico de que não tenho certeza |

Quando você contribui, **não remova a marca sem dizer no que se apoiou.** Um
código confirmado por "eu uso essa transação toda semana" é uma coisa; por "vi
num fórum" é outra. Ambos valem, mas o leitor precisa saber qual é qual.

Prefiro uma dúvida explícita a uma certeza falsa.

---

## O padrão da nota

Antes de propor mudança de conteúdo, vale ler o
[**padrão da nota**](../_projeto/PADRAO.md). Ele define o esqueleto de zonas, o
teste que decide se uma analogia fica, as cinco formas que uma pergunta de
recall pode ter, e as regras de figura e de formatação.

Ele foi extraído da nota que funcionava e escrito para impedir a deriva que,
**medida em 22/08/2026, tinha produzido 127 títulos de seção distintos em 31
notas**, 119 deles aparecendo uma vez só. Esse número é o diagnóstico de
origem, não o estado atual do acervo.

---

## Pull request

PR é bem-vindo, e para correção pequena costuma ser mais rápido que issue.

Se for mexer em nota:

- **Uma nota é um conceito.** 5 a 10 minutos de leitura, teto de 120 linhas,
  terminando em raciocínio fechado. Se sua adição estoura isso, provavelmente
  são duas notas.
- **Cada nota termina em recall**, com o gabarito em `notas/_PISTAS.md`,
  no fim do arquivo, nunca na própria nota.
- **Links são markdown relativo** (`[MD-06](notas/15-MD-06-contrato.md)`), não wikilink.
  Assim funcionam no GitHub e num vault de Obsidian.
- **O nome do arquivo começa com a ordem de estudo**, dois dígitos, seguida do
  código da nota: `15-MD-06-contrato.md`. **O número é a posição na sequência,
  o código é a identidade.** Quem abre a pasta lê de cima para baixo sem
  precisar do README. Nota nova no meio da sequência renumera as seguintes.
- **Nota nova entra na tabela do [README](../README.md) e no grafo** de
  `_projeto/EM-ABERTO.md`, ligada ao pré-requisito dela. Nota fora do
  README não existe.
- **Depois de mexer numa nota, rode** `python ferramentas/gera.py`, que
  regenera a tabela do README e `notas/_PISTAS.md`. **Nunca edite os dois a
  mão:** a nota e a fonte, o resto e derivado.

---

## O que não entra aqui

- **Material de treinamento de qualquer empresa.** Slide, apostila, PDF de
  curso, transcrição de aula. Nada disso, mesmo que você tenha acesso legítimo.
  Escreva com suas palavras.
- **Dado de cliente.** Nome de concessionária num exemplo real, print com dado
  de projeto, nome de sistema interno.
- **Print de tela de sistema produtivo.**

Exemplo se escreve inventado. O prédio da `MD‑02` não existe, e é por isso que
ele pode estar aqui.

---

## Idioma

Português. O objetivo é justamente ser o material que não existe em português.

Termo técnico fica em inglês quando é assim que aparece no sistema
(*Move-In*, *Billing*, *Invoicing*), com a tradução do menu em português na
primeira menção quando existir.
