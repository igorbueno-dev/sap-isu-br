# PE-01: Gestão de Perdas, fraude e defeito
> A mesma consequência, dois mundos jurídicos diferentes. Classificar errado
> aqui é o erro que vira processo.

**Onde entra:** o Bloco 3 do SVC. A menos documentada das três.
**Antes disto:** [SV-01-servico-de-campo](29-SV-01-servico-de-campo.md)
**Depois disto:** [PE-02-faturado-da-epoca](38-PE-02-faturado-da-epoca.md)

---

## O que a área faz

Em uma linha: **identificação, tratamento e recuperação de receitas.**

Em uma frase: **Perdas descobre que o medidor não estava contando a verdade,
calcula quanto deveria ter sido cobrado, e cobra a diferença.**

É a única área do IS-U cujo produto direto é **dinheiro que volta**.

---

## Como um caso começa

Seis gatilhos, e eles se dividem em dois grupos:

| Gatilho | Origem |
|---|---|
| **Fiscalizações em campo** | Alguém foi lá olhar |
| **Denúncias** | Terceiro avisou |
| **Suspeita de fraude** | Alguém desconfiou |
| **Consumo atípico** | **O sistema achou** |
| **Análises estatísticas** | **O sistema achou** |
| **Monitoramento de indicadores** | **O sistema achou** |

**Os três de baixo são o que escala.** Fiscalizar três milhões de imóveis a pé
é impossível; achar por padrão de consumo e mandar o técnico só onde vale a
pena é o que torna a área viável.

A fiscalização em campo é uma **nota de serviço** do tipo Fiscalização, e a
leitura tirada lá tem **motivo** Fiscalização. É por aí que WM e DM entregam o
caso para Perdas. Ver [WM-01](30-WM-01-nota-de-servico.md) e
[DM-02](33-DM-02-leituras-e-registradores.md).

---

## As duas classificações

Esta é a divisão que organiza a área inteira:

| | **FRAUDE** | **DEFEITO** |
|---|---|---|
| Definição | **Ação intencional** | **Falha técnica** |
| Quem causou | O cliente, ou alguém a mando dele | Ninguém. O aparelho falhou |
| Exemplos | Violação de lacre · Desvio de energia · By-pass · Inversão de ligação | Medidor travado · Registrador com defeito · Equipamento queimado · Falha de medição |
| Consequência de medição | Consumo menor que o real | Consumo menor que o real |
| Consequência jurídica | **Ilícito.** Pode ter multa, custo de perícia, ação penal | Cobrança da diferença, sem punição |

**Leia a penúltima linha duas vezes.** As duas ocorrências fazem a mesma coisa
com o número. **O que muda é a intenção**, e a intenção é o que decide se o
cliente vai ser apenas cobrado ou também punido.

---

## Os quatro tipos de fraude, em português

| Termo | O que é fisicamente |
|---|---|
| **Violação de lacre** | O selo que impede abrir o medidor foi rompido |
| **Desvio de energia** | Um fio puxa energia **antes** do medidor. O famoso "gato" |
| **By-pass** | Uma ponte contorna o medidor, total ou parcialmente |
| **Inversão de ligação** | Os cabos foram trocados de posição para o medidor contar errado |

Os quatro têm o mesmo efeito e graus diferentes de sofisticação. **Inversão de
ligação é a mais difícil de achar**, porque nada parece violado por fora.

---

## Por que a classificação é a decisão mais delicada da área

Um medidor travado e um medidor com by-pass **produzem a mesma leitura baixa**.
A diferença está na evidência física que o técnico encontrou e registrou.

**Classificar defeito como fraude** acusa um cliente inocente de crime.
**Classificar fraude como defeito** entrega dinheiro e não aplica sanção.

Por isso o processo é pesado de propósito: perícia, laudo, foto, laudo de
laboratório do medidor. **A memória de cálculo é o que sustenta a cobrança se
o cliente for à justiça.** Ver [PE-02](38-PE-02-faturado-da-epoca.md).

> **O gancho para quem vem de FI-CA:** este é o único lugar do IS-U onde a
> qualidade da documentação decide se a receita entra ou é devolvida.

---

## Se sobrar uma coisa

Fraude e defeito produzem a mesma leitura baixa. O que separa é a evidência.

---

## Recall

1. Em uma frase, o que a Gestão de Perdas faz?
2. Quais dos seis gatilhos escalam para muitos casos de uma vez?
3. Cite o que torna esses gatilhos indispensáveis.
4. O que separa fraude de defeito?
5. O que não muda entre fraude e defeito?
6. O que é um by-pass?
7. O que é uma inversão de ligação?
8. Classificar defeito como fraude produz qual dano?
9. Classificar fraude como defeito produz qual dano?
10. Como um caso de Perdas nasce dentro de WM e de DM?

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#pe-01)  ·  responda tudo antes de abrir.
