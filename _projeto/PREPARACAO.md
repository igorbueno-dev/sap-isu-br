# PREPARAÇÃO PARA PROVA E PARA O PROJETO
### O que se cobra, o que se treina, e o que se escala

> **Isto não ensina IS-U.** É expectativa sobre a avaliação e sobre a rotina de
> trabalho, e por isso mora em `_projeto/` e não na Bancada. Estava misturado
> com a referência de transações, onde um palpite sobre a prova aparecia com o
> mesmo peso de um código conferido.
>
> **Nada aqui é fonte.** São expectativas do autor, e a única forma de fechar
> a primeira delas é perguntar ao instrutor.

---

## O que costuma ser cobrado

O peso está em **entender fluxo e relação entre objetos**, não em decorar código.

1. A hierarquia de dados mestres e a diferença entre cada objeto. **Quase certeza que cai.**
2. O fluxo ponta a ponta e a ordem correta das etapas.
3. **Billing versus Invoicing.** Clássico absoluto.
4. O que precisa existir para uma instalação faturar (a checklist da seção 5).
5. FI-CA versus FI, e por que existem separados.
6. Move-In e Move-Out, e o que acontece com leitura, contrato e faturamento.
7. Análise de causa: dado um sintoma, qual etapa falhou.
8. MRU versus Portion.
9. Instalação técnica versus instalação para faturamento.
10. A ideia de que erro de valor quase nunca é bug, é dado mestre.

---

## Tipos de exercício prático

- **Criar um cliente do zero.** O roteiro da seção 7. É o mais comum.
- **Ciclo completo:** informar leitura, faturar, emitir, conferir a dívida.
- **Simular pagamento e compensar**, depois simular inadimplência e ver a régua.
- **Estudo de caso escrito:** "o cliente X reclama de conta alta, investigue e explique". A resposta esperada percorre leitura → consumo → tarifa → período.
- **Diagnóstico de fatura travada.** O fluxograma da seção 6.
- **Desenhar o fluxo numa lousa e explicar em voz alta.** Treine isto, é o que mais impressiona.

---

## Os cinco testes que dizem se você está pronto

1. **Teste dos 5 minutos.** Desenhar o fluxo ponta a ponta numa folha em branco, nomeando o módulo de cada etapa.
2. **Teste da tradução.** Explicar Billing versus Invoicing para alguém que não é da área, em 60 segundos, sem usar a palavra "documento".
3. **Teste da checklist.** Recitar os oito pré-requisitos de faturamento, de memória.
4. **Teste da Dona Marta.** Contar a história dela do Move-In à religação, nomeando o módulo de cada etapa.
5. **Teste do gabarito.** Acertar 80% dos recalls das notas sem consultar.

---

---

## O que você resolve sozinho e o que você escala


| Resolve sozinho                                                                   | Escala                                                       |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Erro de dado mestre em caso individual                                            | Qualquer coisa que afete muitos clientes pelo mesmo motivo   |
| Leitura implausível para correção                                              | Suspeita de erro em desenvolvimento próprio                 |
| Rastrear a causa e documentar a evidência                                        | Estorno de documento já contabilizado                       |
| Extração de dados para o negócio                                               | Qualquer coisa com risco fiscal ou regulatório              |
| Verificar se o job rodou e o que ele registrou                                    | Mudança que exige aprovação do cliente                    |
| **Parametrizar conforme requisito funcional**, com validação de quem é sênior | Parametrização em ambiente produtivo sem alguém revisando |

> **Correção importante:** parametrizar **é a sua função**, e não algo a escalar. A descrição da vaga diz isso no primeiro item: *"realizar parametrizações nos módulos SAP for Utilities conforme requisitos funcionais"*. O que se escala não é o ato de parametrizar, é a decisão de mudar algo que afeta muita gente, o ambiente produtivo, ou o processo do cliente.

**Escalar cedo com a causa isolada não é fraqueza. É exatamente o que se espera de um júnior bom.**

---
