# BI-02: Os dados mestres de cálculo, como o sistema escolhe a tarifa
> A instalação não guarda a tarifa. Ela guarda uma **categoria**, e a tarifa é
> **determinada** pelo cruzamento dessa categoria com o tipo que cada
> registrador carrega.

**Onde entra:** o mecanismo por trás do cálculo da `BI-01`.
**Antes disto:** [BI-01](39-BI-01-calculo-e-faturamento.md), [ST-03](13-ST-03-instalacao.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## Os objetos

| Objeto | O que é |
|---|---|
| **Tipo de Tarifa** | A classificação que um registrador ou operando carrega |
| **Tarifa** | A regra de preço em si |
| **Categoria de Tarifa** | *"Dita as regras de cálculo a serem utilizadas para um grupo de clientes"* |
| **Esquema** | O encadeamento que combina as tarifas |
| **Operando** | A variável que o cálculo usa |

---

## A determinação, que é o coração da coisa

A instalação carrega, **na faixa de tempo**, uma categoria de tarifa. Cada
registrador e cada operando carrega um tipo de tarifa. **O cruzamento dos dois
determina quais tarifas entram.**

```
INSTALAÇÃO A
  faixa de tempo ──▶ CT3          a categoria
  registrador    ──▶ TT4          um tipo
  operando       ──▶ TT1          outro tipo

DETERMINAÇÃO
  CT3 + TT4  =  T2, T9, T22
  CT3 + TT1  =  T19, T22

  CT3 ──▶ E2                      a categoria também aponta o esquema
```

**Duas leituras nesse desenho:**

1. **A mesma categoria produz conjuntos diferentes de tarifa**, conforme o tipo
   do registrador. É assim que uma indústria com seis registradores é cobrada
   por seis regras diferentes com um cadastro só
2. **`T22` aparece nas duas linhas.** Tarifas se repetem entre determinações, o
   que é esperado: a taxa de iluminação pública vale para todo mundo

---

## Por que a categoria mora na faixa de tempo

Porque tarifa muda, e **o passado tem que continuar calculável**.

A categoria fica na faixa de tempo da instalação, não na instalação. Quando o
regulador reajusta, entra uma faixa nova; a antiga permanece, e um recálculo de
janeiro continua achando a regra de janeiro. É a mesma família de mecanismo da
[MD-08](06-MD-08-os-dois-mundos.md).

---

## Operando, enfim definido

O termo aparecia desde a Aula 03, numa etapa de workflow de campo chamada
*Atualização de Operandos*, e ninguém dizia o que era.

**Operando é dado mestre de cálculo.** Tem nó próprio de customizing (*definir
operandos*), carrega um tipo de tarifa como o registrador carrega, e a
**categoria de tarifa armazena os valores de operando válidos para o grupo de
clientes**.

Isso fecha a estranheza da [WM-02](31-WM-02-workflow-e-integracoes.md): um
workflow de **campo** atualiza operando porque o que o técnico encontra na rua
muda a variável que o **faturamento** usa. Os dois se tocam nesse ponto.

---

## O erro que todo mundo comete

**Procurar a tarifa na instalação.**

Ela não está lá. A instalação tem a **categoria**, e a tarifa é resultado de
uma determinação. Quem abre a instalação esperando ver "tarifa residencial
convencional" não encontra, conclui que o cadastro está incompleto, e abre
chamado por um comportamento correto.

---

## No sistema

Os nós ficam em `Cálculo da fatura → Dados mestre`:

| Nó | Item |
|---|---|
| Definir tipos de tarifas | `EA56` |
| Definir operandos | `S_KK4_74000866` |
| Definir preços | `S_KK4_74000893` |
| Definir tarifas | `S_KK4_74000887` |
| Definir esquemas | `S_KK4_74000889` |
| Definir categorias de tarifa | `S_KK4_74000825` |
| Definir determinação de tarifa | `S_KK4_74000824` |
| Definir descontos e acréscimos | `S_KK4_74000826` |

**Quase tudo aqui é customizing, não transação.** É configuração de projeto, e
por isso os códigos têm a forma `S_KK4_*` em vez de quatro letras.

Tabelas: `ETRF` tarifas · `ETTA` categoria · `ETTAF` fatos da categoria ·
`TE069` tipos · `ERTFND` **determinação** · `ESCH` e `ESCHS` esquema ·
`EPREI` preços · **`TE221` operandos**.

---

## Se sobrar uma coisa

A instalação não guarda a tarifa, guarda a categoria. A tarifa é determinada.

---

## Recall

1. Qual transação define tipos de tarifa?
2. Qual tabela guarda as tarifas?
3. Qual tabela guarda a categoria de tarifa?
4. Qual tabela guarda a determinação de tarifa?
5. Qual tabela guarda os operandos?
6. Qual tabela guarda os tipos de tarifa?
7. Quais duas tabelas guardam o esquema de cálculo?
8. O que a instalação guarda, na faixa de tempo, a respeito de tarifa?
9. Quais são as duas entradas da determinação de tarifa?
10. O que a determinação de tarifa produz?
11. Como o SAP chama a variável que o cálculo usa e que o customizing define à parte?
12. Onde ficam armazenados os valores de operando válidos?
13. Um analista abre a instalação e não encontra a tarifa. Isso é erro?
14. Uma tarifa foi reajustada em março. Cite o que impede o recálculo de janeiro de usar o valor novo.
15. O que separa Tipo de Tarifa de Categoria de Tarifa?

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#bi-02)  ·  responda tudo antes de abrir.
