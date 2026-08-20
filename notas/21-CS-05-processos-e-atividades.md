# CS-05: Processos e atividades no atendimento
> O que o atendente realmente faz o dia inteiro. Protocolo, atividade e a
> lista de processos que respondem por quase todo o volume de um call center
> de concessionária.

**Onde entra:** o lado operacional do CRM, depois de entender o encaixe.
**Antes disto:** [CS-04-crm-no-contexto-utilities](20-CS-04-crm-no-contexto-utilities.md)

---

## Protocolo e atividade

São os dois objetos do dia a dia:

| Objeto | O que é |
|---|---|
| **Protocolo** | O número que o cliente recebe. É a prova de que ele ligou, e o fio para acompanhar |
| **Atividade** | O registro do que foi feito dentro daquele contato |

Um protocolo pode ter várias atividades. É por isso que o cliente liga
citando um número e o atendente vê o histórico inteiro.

> Em concessionária o protocolo tem peso regulatório: é ele que prova prazo de
> atendimento perante o regulador. Não é burocracia interna.

---

## Os processos, ou FOPs

A lista costuma aparecer como **Processos/FOPs**:

| Processo | O que o cliente quer |
|---|---|
| **Ligação Nova** | Ligar um imóvel que não tem fornecimento |
| **Alteração de titularidade** | Trocar quem responde pela conta |
| **Segundas Vias** | Reemitir uma conta |
| **Reclamações** | Contestar valor, falta de fornecimento, atendimento |
| **Cadastro** | Corrigir ou completar dados |
| **Modificações Contratuais** | Mudar algo do contrato, como tarifa ou titular de cobrança |

A lista não é exaustiva.

> **`FOP` é uma sigla que eu não consegui expandir com segurança.** Aparece
> colada em "Processos" e muda de projeto para projeto. **Se você sabe o que
> significa, abra uma issue.**

---

## Os dois que você já conhece por outro nome

**Ligação Nova** é o que a `CS‑04` mostra como *new connection* na
responsabilidade da área. É o processo que dispara a criação da estrutura
técnica inteira.

**Alteração de titularidade** aparece na lista de processos do CRM. Do outro
lado do material, o slide do Contrato diz que ele *"é criado quando ocorre uma
nova ligação ou troca de titularidade"*. **Os dois pontos se ligam: o processo
comercial de troca de titular é o que produz um Contrato novo.**

> **Lacuna estrutural.** Se "Alteração de titularidade" é Move-Out seguido de
> Move-In ou um processo próprio é detalhe de processo, e a aula de CRM foi
> panorâmica. **Só fecha na trilha de CS + CRM.**

**Vale reparar no padrão:** o CRM nomeia processos pelo que o cliente pede;
o IS-U nomeia pelo que acontece com o dado. Ligação Nova e Move-In são a
mesma coisa vista da recepção e da cozinha.

---

## O campo que liga cadastro e ciclo de vida

No cadastro do Parceiro de Negócios existe um campo **Status**, com valores
como **Cliente, Prospect, Inativo**.

É pequeno e é importante: é onde o **ciclo de vida da [CS-02](18-CS-02-ciclo-de-vida-do-cliente.md)
vira dado**. "Prospect" não é abstração de marketing, é um valor gravado no
`BUT000`.

---

## Recall

1. Qual a diferença entre protocolo e atividade, e qual contém qual?
2. Por que o protocolo importa fora da empresa?
3. Cite quatro processos da lista de FOPs.
4. Alteração de titularidade corresponde a que processo no lado dos dados
   mestres?
5. Onde o conceito de "prospect" aparece como dado no sistema?

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#cs-05)  ·  responda tudo antes de abrir.
