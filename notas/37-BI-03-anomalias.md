# BI-03: Anomalias, dois fluxos que parecem iguais e não são
> Anomalia é a trava que impede conta errada de sair. No cálculo ela só marca o
> documento; no faturamento ela **cria um documento novo**.

**Onde entra:** o que acontece quando o cálculo ou o faturamento desconfia.
**Antes disto:** [BI-01](35-BI-01-calculo-e-faturamento.md)

---

## O conceito, na frase do material

> *"O processo de detecção de anomalias permite que sejam realizadas
> consistências nos documentos de Cálculo e Faturamento a fim de impedir a
> emissão de contas erradas."*

**Não é erro, é retenção.** O documento foi produzido e ficou preso esperando
alguém olhar.

---

## Os dois fluxos, lado a lado

```
ANOMALIA DE CÁLCULO
execução ─▶ anomalia? ─sim─▶ liberar? ─sim─▶ desmarca ─▶ MANTÉM o mesmo
                                                         documento de cálculo

ANOMALIA DE FATURAMENTO
execução ─▶ anomalia? ─sim─▶ CRIA doc. ─▶ liberar? ─sim─▶ CRIA documento
                             de anomalia                  de faturamento
```

| | Cálculo | Faturamento |
|---|---|---|
| Enquanto retido | o próprio documento fica marcado | **nasce um documento de anomalia à parte** |
| Ao liberar | **desmarca**, e o documento é o mesmo | **cria um documento novo** |
| Depois de liberar | | *"não há nova verificação de anomalia"* |

**Essa assimetria aparece até nas tabelas:** `ERCHO` guarda a anomalia do
cálculo e `ERDO` a da fatura. São duas tabelas porque são dois objetos.

---

## A frase que vira pergunta de prova

> *"O tratamento de anomalias de cálculo e faturamento deve ser realizado de
> forma individual através da transação `EA05`. **Não existe ferramenta de
> liberação em massa** de documentos em anomalia."*

Duas consequências práticas:

1. **Anomalia é trabalho de gente, um a um.** Não há botão de liberar tudo, e
   isso é decisão de produto, não limitação
2. **Backlog de anomalia não se resolve com job.** Se acumularam mil, alguém
   vai abrir mil

No momento da análise, o usuário tem duas saídas: **cancelar** o documento
retido ou **liberá-lo**.

---

## O erro que todo mundo comete

**Liberar sem olhar, porque o cliente está reclamando.**

A anomalia existe justamente porque o número está fora do esperado. Liberar
sem investigar transforma uma retenção correta em conta errada emitida, e aí o
caminho de volta passa por estorno, refaturamento e, se for o caso, pelo
processo da [PE-02](34-PE-02-faturado-da-epoca.md).

**A anomalia de faturamento agrava isso**, porque depois de liberada *não há
nova verificação*. É liberação sem rede.

---

## Na prática

`EA05` é a transação que você mais vai abrir se cair em Billing. Ela é o balcão
onde chegam os documentos que o sistema não teve coragem de emitir sozinho.

**Antes de liberar, olhe a leitura.** Boa parte das anomalias de cálculo vem de
leitura implausível que passou pela validação. Ver
[DM-05](32-DM-05-ciclo-da-leitura.md).

---

## No sistema

| Transação ou tabela | O que é |
|---|---|
| `EA05` | A única transação de tratamento de anomalia, individual |
| `ERCHO` | Anomalia do documento de cálculo |
| `ERDO` | Anomalia da fatura |

---

## Se sobrar uma coisa

Liberar anomalia de faturamento é liberação sem rede: não há nova verificação.

---

## Recall

1. Qual transação trata anomalia?
2. Qual tabela guarda a anomalia do cálculo?
3. Qual tabela guarda a anomalia da fatura?
4. Como o SAP chama a retenção de um documento que não passou na consistência?
5. O que a anomalia impede?
6. O que separa a liberação de anomalia de cálculo da de faturamento?
7. Que duas saídas o usuário tem diante de um documento retido?
8. Mil documentos entraram em anomalia. Cite o que impede resolver isso com um job.
9. Uma anomalia de faturamento foi liberada por engano. O que o sistema verifica depois?

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#bi-03)  ·  responda tudo antes de abrir.
