# CS-06: A esteira do chamado, do protocolo ao fechamento
> Todo processo do CRM termina em outra área. O atendimento abre o protocolo e
> quem fecha é campo, medição, faturamento ou cobrança.

**Onde entra:** é a nota que liga CRM ao resto do acervo.
**Antes disto:** [CS-05](21-CS-05-processos-e-atividades.md), [CS-04](20-CS-04-crm-no-contexto-utilities.md)
**Origem:** **misto.** Os processos e a cadeia das cinco áreas são do material.
**O encadeamento objeto a objeto é meu**, montado cruzando as notas do acervo.
Cada elo aponta para a nota que o sustenta.

---

## Por que esta nota existe

O CRM é a **primeira** área da cadeia, e nenhuma das outras quatro começa
sozinha. Isso tem uma consequência que muda o trabalho: **quem atende decide o
que as outras áreas vão fazer**, classificando o pedido na entrada.

Classificar errado não é erro de digitação. É mandar o chamado para a esteira
errada, e a esteira errada custa deslocamento de técnico, refaturamento ou
processo no regulador.

**Por isso um analista de CRM precisa das outras trilhas.** Não para executar,
mas para saber para onde está mandando.

---

## Cada processo e a esteira que ele dispara

| Processo do CRM | Passa por | Termina em |
|---|---|---|
| **Ligação Nova** | `WM` nota de serviço → `DM` instalação do medidor → dados mestres técnicos | O **Contrato**, criado no Move-In |
| **Alteração de titularidade** | dados mestres comerciais | **Contrato novo**, o antigo encerrado |
| **Segundas Vias** | `BILL` | Documento de impressão reemitido |
| **Reclamação de valor** | `DM` leitura → `BILL` cálculo → `PE` se houver irregularidade | Estorno, refaturamento ou nada |
| **Cadastro** | dados mestres comerciais, e `WM` se for endereço | Parceiro de Negócios corrigido |
| **Modificações Contratuais** | dados mestres comerciais e técnicos | Contrato ou Instalação alterados |
| **Religação** | `FI-CA` confirma o pagamento → `WM` executa | Fornecimento restabelecido |

---

## A esteira mais longa, passo a passo

**Ligação Nova** é a que atravessa mais áreas, e serve de modelo para as
outras:

```
CS + CRM   protocolo aberto, pedido classificado        CS-05
   ↓
WM         nota de serviço com tipo, motivo,            WM-01
           prioridade e prazo
   ↓
campo      técnico executa e devolve a ordem            WM-02
   ↓
técnicos   Objeto de Ligação → Local de Consumo →       ST-01 a ST-03
           Instalação
   ↓
DM         material → tipo → equipamento →              DM-03
           instalação total
   ↓
DM         Conjunto de Contratos e Unidade de           DM-04
           Leitura atribuídos
   ↓
comercial  Move-In cria o CONTRATO                      MD-07
   ↓
BILL       primeira leitura, primeiro cálculo           DM-05, BI-01
```

**Repare onde o Contrato aparece.** Ele é penúltimo, e não primeiro. O
atendimento abre o pedido de um cliente que ainda não tem contrato, e o
contrato só existe quando a estrutura física já está pronta. Ver
[MD-06](15-MD-06-contrato.md).

---

## O erro que todo mundo comete

**Prometer prazo pelo protocolo, e não pela esteira.**

O protocolo abre em segundos. A esteira de Ligação Nova envolve deslocar
equipe, instalar aparelho e esperar o primeiro ciclo de leitura. **Quem promete
o prazo do protocolo cria um segundo chamado**, agora de reclamação de prazo, e
esse tem peso com o regulador. Ver [WM-01](30-WM-01-nota-de-servico.md), onde o
prazo nasce junto com a nota.

---

## Na prática

**A pergunta que resolve metade dos chamados é "onde está isto agora?"**

Com a esteira na cabeça, ela vira objetiva: existe nota de serviço? a ordem foi
confirmada? o equipamento foi instalado com efeito no cálculo? existe contrato?
saiu documento de cálculo?

Cada uma dessas perguntas tem uma nota que a responde, e é para isso que as
outras trilhas continuam no acervo.

---

## Se sobrar uma coisa

O CRM não fecha chamado: ele decide quem vai fechar.

---

## Recall

1. Qual objeto encerra a esteira de Ligação Nova?
2. Em que ponto da esteira de Ligação Nova o Contrato é criado?
3. Por qual área passa um pedido de Segunda Via?
4. Quais três áreas uma reclamação de valor pode atravessar?
5. Quem decide o corte, e quem o executa?
6. Ordene a esteira de Ligação Nova: Contrato, instalação do equipamento, nota de serviço, protocolo.
7. Um atendente promete ao cliente o prazo do protocolo para uma ligação nova. Cite a consequência.
8. Um cliente pede religação depois de pagar. Cite a área que confirma o pagamento.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#cs-06)  ·  responda tudo antes de abrir.
