# GABARITOS
### As respostas dos recalls, separadas de propósito

> **Este arquivo existe para as respostas não aparecerem junto da pergunta.**
> Blocos colapsáveis de HTML não funcionam de forma confiável: dependem do
> visualizador e do modo (edição x leitura). Arquivo separado funciona em
> qualquer um.
>
> **Como usar:** responda o recall inteiro na cabeça ou no papel, **depois**
> venha aqui. Olhar antes de tentar não é revisão, é leitura.

**Índice:** [GE-03](#ge-03)  ·  [GE-01](#ge-01)  ·  [GE-02](#ge-02)  ·  [GE-04](#ge-04)  ·  [MD-01](#md-01)  ·  [MD-02](#md-02)  ·  [MD-03](#md-03)  ·  [MD-04](#md-04)  ·  [MD-05](#md-05)  ·  [MD-06](#md-06)  ·  [MD-07](#md-07)  ·  [ST-01](#st-01)  ·  [ST-02](#st-02)  ·  [ST-03](#st-03)  ·  [ST-04](#st-04)

---

## GE-03
**GE-03: A concessionária em cinco parágrafos**  ·  [voltar para a nota](GE-03-a-concessionaria.md)

1. **Onde** está ligado, **quanto** consumiu, **por quanto** é cobrado.
2. Porque envolve deslocar uma pessoa, e cortar quem pagou vira processo
   judicial e multa do regulador. Erro de faturamento se corrige com estorno.
3. O consumo vem antes da autorização e antes do pagamento. Não há pedido,
   não há vendedor, e o produto é invisível.

---

## GE-01
**GE-01: O que é o SAP IS-U CCS**  ·  [voltar para a nota](GE-01-o-que-e-is-u-ccs.md)

1. Customer Care Service, e Industry Solutions for Utilities.
2. CS+CRM, WM, DM, BILL, FI-CA.
3. Como faixa transversal, por baixo das cinco. BW enxerga tudo mas não é
   parte do CCS, e por isso não está entre as trilhas disponíveis.

---

## GE-02
**GE-02: A evolução do produto, do R/3 ao SaaS**  ·  [voltar para a nota](GE-02-evolucao-do-produto.md)

1. Fim de 2027. Força a migração de toda a base instalada para S/4HANA, o que
   gera projetos.
2. SAP GUI na clássica, Fiori na moderna, Web/nativo em nuvem no futuro SaaS.
3. Muda a tecnologia (HANA, tempo real) e a interface. **Não muda o modelo de
   dados de negócio** nem os conceitos do CCS.

---

## GE-04
**GE-04: Os três setores, com peso igual**  ·  [voltar para a nota](GE-04-os-tres-setores.md)

1. **Não.** Mede volume em m³, a cobrança é por energia. Há conversão no meio.
2. **Duas**, água e esgoto. A de esgoto normalmente não tem medidor e fatura
   como percentual da água.
3. **Saneamento**, por medidor embaçado, enterrado ou inacessível.
4. **Saneamento**, por ser o mais sensível juridicamente. A régua de cobrança
   costuma ser mais conservadora.

---

## MD-01
**MD-01: O mapa dos dados mestres**  ·  [voltar para a nota](MD-01-mapa-dos-dados-mestres.md)

1. Estrutura Postal, Dados Mestre Técnicos, Dados Mestre Comercial, Dados
   Transacionais.
2. **Duração da validade.** Mestre dura muito e é a única versão válida no
   período. Transacional é dinâmico e vale pouco tempo.
3. O **Objeto de Ligação**.

---

## MD-02
**MD-02: A tradução do prédio**  ·  [voltar para a nota](MD-02-a-traducao-do-predio.md)

1. Objeto de Ligação, Local de Consumo, Local de Instalação de Equipamento,
   Equipamento, Parceiro de Negócios.
2. Porque o lugar onde se **consome** não é o lugar onde o aparelho está
   **instalado**. No prédio, consome-se no apartamento e mede-se na garagem.
3. O **Contrato**.

---

## MD-03
**MD-03: Parceiro de Negócios, categoria e função**  ·  [voltar para a nota](MD-03-parceiro-de-negocios.md)

1. Pessoa, Organização e Grupo. Grupo normalmente não é utilizada.
2. **Parceiro de Contrato.**
3. Que ele não tem a função Parceiro de Contrato, ou tem só função de
   Pessoa de Contato, que não carrega contrato.

---

## MD-04
**MD-04: Parceiro de Negócios, os dados e o customizing**  ·  [voltar para a nota](MD-04-parceiro-de-negocios-dados.md)

1. **No PN.** Mas o direcionamento por função pode ser feito no nível da
   Conta Contrato.
2. `BUCG`, agrupamento de campos por função de PN.
3. No endereço standard do PN, e depois no endereço de correspondência da
   Conta Contrato, que é herdado do PN mas pode ser sobreposto.

---

## MD-05
**MD-05: Conta Contrato**  ·  [voltar para a nota](MD-05-conta-contrato.md)

1. **Mesmos dados de pagamento e cobrança.**
2. Do **PN** (business partner level).
3. Bloqueio de corte/cobrança na **Conta Contrato**. Bloqueio de faturamento
   no **Contrato**.

---

## MD-06
**MD-06: Contrato**  ·  [voltar para a nota](MD-06-contrato.md)

1. Durante o **Move In**, ou em troca de titularidade / nova ligação.
2. **Não.** Um contrato liga a exatamente uma Conta Contrato e uma Instalação.
3. **No nível do Contrato.**
4. Porque ele é resultado do processo de Move In, não de cadastro direto.

---

## MD-07
**MD-07: Move-In e Move-Out**  ·  [voltar para a nota](MD-07-move-in-move-out.md)

1. A **Instalação permanece**, é do imóvel. O **Contrato é encerrado**, é da
   pessoa.
2. Uma **leitura inicial**.
3. **Ligação clandestina.** O sistema monitora imóveis desocupados justamente
   por isso.
4. Porque obriga a desfazer e refazer todo o faturamento posterior à data.

---

## ST-01
**ST-01: Objeto de Ligação**  ·  [voltar para a nota](ST-01-objeto-de-ligacao.md)

1. **Endereço.**
2. **Mais alto.**
3. **Dois.** Cada número predial é um Objeto de Ligação.

---

## ST-02
**ST-02: Local de Consumo**  ·  [voltar para a nota](ST-02-local-de-consumo.md)

1. **Não.** Ele assume o endereço do Objeto de Ligação e guarda só o
   complemento.
2. Tipo do Local de Consumo, e Complemento do endereço.
3. **Um** objeto de ligação, **quarenta** locais de consumo.

---

## ST-03
**ST-03: Instalação**  ·  [voltar para a nota](ST-03-instalacao.md)

1. A **Instalação**, no bloco Faturamento e Medição.
2. Marcação de tarifa social, campo brasileiro, no bloco Informações
   Individuais da **Instalação**.
3. Nos dados mestres da **Instalação**: tarifa, vigência da tarifa, unidade
   de leitura e tipo de validação.

---

## ST-04
**ST-04: Equipamento e Local de Instalação**  ·  [voltar para a nota](ST-04-equipamento.md)

1. Normalmente **um**, com os 40 relógios juntos.
2. **Transformador de Corrente (TC).**
3. Foi feita instalação **técnica** (`EG33`) sem a parte **com efeito no
   cálculo** (`EG34`). Faltou completar a instalação.
