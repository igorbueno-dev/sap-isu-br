# FC-04: Documento real, documento estatístico, e a chave que leva ao FI
> Nem tudo que o FI-CA registra vira contabilidade. E o que vira não vai
> documento a documento: vai somado, por uma chave que abre, fecha e
> transfere.

**Onde entra:** a fronteira entre o FI-CA e a contabilidade da empresa.
**Antes disto:** [FC-02](45-FC-02-operacao-e-suboperacao.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## Real e estatístico

| Tipo | Texto do material |
|---|---|
| **Documento real** | *"Registra um fato financeiro efetivo: a fatura emitida, o pagamento recebido, o estorno, os juros lançados. Gera partidas em aberto e movimenta o saldo do cliente."* |
| **Documento estatístico** | *"Registra uma informação de controle, sem efeito financeiro: valores previstos, encargos simulados, itens de cobrança acompanhados apenas para gestão."* |

**A diferença tem quatro consequências:**

| | Real | Estatístico |
|---|---|---|
| Contabiliza | **Sim**, vai para o FI | **Não**, fica só no FI-CA |
| Compõe o saldo devedor | **Sim** | **Não** |
| É exigível e compensável | **Sim** | **Não** |
| Entra no fechamento do período | **Sim** | **Não** |

*"Exemplos típicos: juros previstos e parcelas futuras nascem estatísticos; ao
vencer ou ao serem faturados, viram documentos reais e só então contabilizam."*

**A conversão é o ponto:** quando o valor previsto se confirma, o sistema gera
o documento real e o estatístico deixa de ser necessário.

---

## A chave de reconciliação

> *"É o agrupador que reúne todos os documentos contabilizáveis do FI-CA em um
> mesmo período de apuração. Cada lançamento, fatura, pagamento, compensação,
> estorno, nasce vinculado a uma chave aberta. É ela que garante a
> rastreabilidade entre o razão auxiliar de contas a receber e a contabilidade
> geral."*

**Por que ela existe**, na razão declarada: *"O FI-CA processa um volume muito
alto de itens; transferir documento a documento para o FI seria inviável."*

```
1 CHAVE ABERTA ──▶ 2 FECHAMENTO ──▶ 3 TRANSFERÊNCIA ──▶ 4 CONFERÊNCIA
  documentos do     encerrado o       gera os documentos    compara o total
  dia entram nela,  período, não      contábeis             transferido com
  ainda sem         aceita mais       consolidados na       os saldos do
  lançamento no FI  nada, e totaliza  contabilidade geral   FI-CA
                    por conta
```

*"Enquanto a chave não é fechada e transferida, o resultado da arrecadação não
aparece na contabilidade, por isso o fechamento faz parte da rotina diária da
operação."*

---

## Enfim: FI-CA não é FI

**Esta é a pergunta clássica de prova, e a resposta está na chave.**

| | **FI-CA** | **FI** |
|---|---|---|
| O que é | **Razão auxiliar** de contas a receber | **Contabilidade geral** |
| Granularidade | Item a item, por cliente | **Totais consolidados por conta** |
| Volume | Milhões de partidas | Documentos somados |
| Quem vê | Operação, atendimento, cobrança | Contabilidade e auditoria |
| Como se ligam | **A chave de reconciliação** | |

Eles existem separados por **volume**. Uma concessionária lança milhões de
partidas por mês, e nenhum razão contábil geral aguenta isso item a item.

---

## O erro que todo mundo comete

**Procurar no FI um lançamento que ainda está numa chave aberta.**

O documento existe, o pagamento entrou, o cliente está quitado, e a
contabilidade não vê nada. Não é erro: é a chave que ainda não fechou.

O inverso também engana: **um valor previsto que aparece na tela e não está em
lugar nenhum da contabilidade** é documento estatístico, e ele nunca vai
contabilizar enquanto não virar real.

---

## No sistema

**Não há transação desta nota.** A Aula 05 apresentou o FI-CA inteiro em 24
slides e **não mostrou um único código**, nem de transação nem de tabela.

Isso não é lacuna de captura, é característica da aula. **As transações de
FI-CA são pergunta para o instrutor**, e a [`_BANCADA.md`](_BANCADA.md) tem a
seção de FI-CA montada a partir do pôster de tabelas.

---

## Se sobrar uma coisa

O FI-CA é razão auxiliar e o FI é a contabilidade geral. A chave de
reconciliação é a ponte, e ela transfere somas, não documentos.

---

## Recall

1. O que separa um documento real de um documento estatístico?
2. Cite as quatro consequências dessa diferença.
3. Cite o que impede um documento estatístico de ser cobrado do cliente.
4. Nomeie dois exemplos típicos de documento que nasce estatístico.
5. O que é a chave de reconciliação?
6. Descreva as quatro etapas da chave, da abertura à conferência.
7. Cite a razão pela qual a chave existe, em vez de transferir documento a documento.
8. O que separa o FI-CA do FI?
9. Cite o motivo de os dois existirem separados.
10. Um pagamento foi compensado e a contabilidade não mostra nada. Cite a primeira hipótese.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#fc-04)  ·  responda tudo antes de abrir.
