# WM-01: A nota de serviço e o ciclo do campo
> Tudo que o campo faz começa numa nota de serviço. Ela carrega tipo, motivo,
> prioridade e prazo, e é o prazo que dá multa.

**Onde entra:** o objeto central do Bloco 1, WM / SVC.
**Antes disto:** [SV-01-servico-de-campo](29-SV-01-servico-de-campo.md)
**Depois disto:** [WM-02-workflow-e-integracoes](31-WM-02-workflow-e-integracoes.md)
**Origem:** **misto.** As listas e os nomes são do material.
**O raciocínio em volta é meu.**

---

## O que o bloco WM cobre

Em uma linha: **a gestão dos serviços executados em campo, e do relacionamento
com o cliente em torno deles.** Seis frentes:

| Frente | O que é |
|---|---|
| **Notas de serviço** | O objeto. O pedido de trabalho |
| **Atualização de endereço** | Corrigir onde o imóvel fica, inclusive coordenadas |
| **Transgressões** | Controle de prazo. **A frente que vira multa** |
| **Taxas e cobranças** | O serviço que o cliente paga |
| **Workflow e automação** | Como o pedido anda sozinho. Ver [WM-02](31-WM-02-workflow-e-integracoes.md) |
| **Integração com CRM e Dunning** | De onde os pedidos chegam. Ver [WM-02](31-WM-02-workflow-e-integracoes.md) |

---

## Os sete tipos de nota de serviço

Vale decorar esta lista: ela cobre quase todo o dia a dia do campo.

| Tipo | O que manda alguém fazer |
|---|---|
| **Corte** | Desligar o fornecimento |
| **Religação** | Religar |
| **Fiscalização** | Ir olhar se tem irregularidade. **A porta de entrada de Perdas** |
| **Modificação** | Alterar algo já instalado |
| **Inspeção** | Vistoriar |
| **Ligação nova** | Ligar um imóvel que nunca teve fornecimento |
| **Substituição de medidor** | Trocar o equipamento |

**Corte, religação e ligação nova estão na mesma lista.** Para o sistema todos
são a mesma coisa: um pedido de trabalho com prazo. O que separa é tipo, motivo e prioridade.

---

## O que a nota carrega

A nota nasce com **tipo de processo, motivo, prioridade e prazo**. Quatro
campos, e cada um decide uma coisa diferente:

| Campo | Decide |
|---|---|
| **Tipo de processo** | Que trabalho é |
| **Motivo** | Por que foi pedido. É o que separa corte por inadimplência de corte a pedido |
| **Prioridade** | Ordem na fila |
| **Prazo** | **O relógio regulatório.** Ver abaixo |

---

## Transgressões: onde mora a multa

Quadrante inteiro, quatro itens: **controle de prazos**, **início, conclusão e
suspensões**, **eventos de paralisação** e **transgressões regulatórias**.

**Transgressão é o prazo estourado.** O regulador define quanto tempo a
concessionária tem para religar, para ligar um imóvel novo, para atender uma
emergência. Estourar não é atraso administrativo: **é infração com valor.**

Os outros três itens existem para defender a empresa desse relógio:

- **Início e conclusão** marcam quando a contagem começa e termina
- **Suspensão** para o relógio quando a culpa não é da concessionária. Cliente
  ausente, imóvel trancado, documentação faltando
- **Evento de paralisação** registra o motivo da suspensão

> **Consequência prática:** boa parte do trabalho de quem cuida de WM não é
> executar a nota, é **provar que o relógio esteve parado**. Suspensão mal
> registrada vira transgressão que não existiu.

---

## Taxas e cobranças: o campo gera receita

Cinco itens, e o ponto é que **serviço de campo não é só custo**: religação
**normal ou de urgência**, com preço diferente, ligação nova, alteração de
carga, vistoria e outros serviços, e **integração com faturamento**.

O último fecha o raciocínio: a taxa não fica no campo, ela desce para a conta
do cliente. **Nota de serviço executada pode virar linha de fatura.**

---

## Atualização de endereço, que não é o que parece

Alteração de endereço, correção de localização, **coordenadas geográficas** e
atualização cadastral.

Não é digitação de escritório: é o técnico que foi lá e descobriu que o poste
está na outra esquina. **Isso alimenta a rota de leitura e o despacho de
equipe.** É coerente com WM manter as **estruturas políticas e postais**, a
divisão 1 dos dados mestres. Ver [MD-01](05-MD-01-mapa-dos-dados-mestres.md).

---

## Se sobrar uma coisa

A nota nasce com prazo, e prazo estourado é multa, não atraso.

---

## Recall

1. Nomeie os quatro campos que a nota de serviço carrega ao nascer.
2. O que o campo tipo de processo decide?
3. O que o campo prazo decide?
4. Cite quatro dos sete tipos de nota de serviço.
5. O que é uma transgressão?
6. Para que serve a suspensão de prazo?
7. Qual tipo de nota é a porta de entrada da Gestão de Perdas?
8. Um técnico chega e o imóvel está trancado. Cite o que registrar.
9. Cite o que acontece se essa paralisação não for registrada.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#wm-01)  ·  responda tudo antes de abrir.
