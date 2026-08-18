# SAP IS-U CCS, referência em português

Notas sobre **SAP IS-U CCS** (*Industry Solutions for Utilities / Customer Care
Service*), a solução setorial que roda o ciclo comercial de concessionárias de
energia, água e gás.

Quase não existe material estruturado de IS-U em português. Este repositório é
uma tentativa de mudar isso, em aberto, com correção de quem conhece o módulo
na prática.

**Se for ler só uma coisa, leia [`MD-02`](notas/MD-02-a-traducao-do-predio.md).**
É o diagrama que traduz um prédio de verdade nos objetos do sistema, e resolve
metade da confusão inicial com dados mestres.

---

# As 15 notas

Cada nota é um conceito só: 5 a 10 minutos, terminando em raciocínio fechado.

### Geral

| Nota | Tema | Status | O gancho | Tempo |
|---|---|---|---|---|
| [`GE-03`](notas/GE-03-a-concessionaria.md) | **A concessionária em 5 parágrafos** | a confirmar | O problema de negócio. **Leia primeiro de tudo** | 5 min |
| [`GE-01`](notas/GE-01-o-que-e-is-u-ccs.md) | O que é o SAP IS-U CCS | verificado | As duas siglas, as cinco áreas, e por que BW não é uma delas | 6 min |
| [`GE-02`](notas/GE-02-evolucao-do-produto.md) | A evolução do produto | verificado | Do R/3 ao SaaS, e a data de 2027 que gera projeto | 4 min |
| [`GE-04`](notas/GE-04-os-tres-setores.md) | Os três setores | a confirmar | Energia, gás e água. Muda a resposta do exercício | 5 min |

### Dados mestres comerciais

| Nota | Tema | Status | O gancho | Tempo |
|---|---|---|---|---|
| [`MD-01`](notas/MD-01-mapa-dos-dados-mestres.md) | O mapa dos dados mestres | verificado | Quatro divisões, dois mundos, e validade no tempo | 7 min |
| [`MD-02`](notas/MD-02-a-traducao-do-predio.md) | **A tradução do prédio** | verificado | O diagrama que converte o mundo real em SAP | 6 min |
| [`MD-03`](notas/MD-03-parceiro-de-negocios.md) | Parceiro de Negócios | verificado | Categoria é o que ele é, função é o papel. Sem Parceiro de Contrato, não fatura | 7 min |
| [`MD-04`](notas/MD-04-parceiro-de-negocios-dados.md) | PN, dados e customizing | verificado | Os seis blocos, os endereços, e as 17 transações de configuração | 8 min |
| [`MD-05`](notas/MD-05-conta-contrato.md) | Conta Contrato | verificado | A bolsa financeira. E onde mora o bloqueio de corte | 7 min |
| [`MD-06`](notas/MD-06-contrato.md) | **Contrato** | verificado | A dobradiça, as oito regras, e por que não existe "criar contrato" | 6 min |
| [`MD-07`](notas/MD-07-move-in-move-out.md) | **Move-In e Move-Out** | a confirmar | O processo que cria o Contrato. Fecha a maior lacuna do modelo | 6 min |

### Dados mestres técnicos

| Nota | Tema | Status | O gancho | Tempo |
|---|---|---|---|---|
| [`ST-01`](notas/ST-01-objeto-de-ligacao.md) | Objeto de Ligação | verificado | O prédio. Nível mais alto, e onde mora o endereço | 5 min |
| [`ST-02`](notas/ST-02-local-de-consumo.md) | Local de Consumo | verificado | O apartamento. Onde mora o complemento, não o endereço | 5 min |
| [`ST-03`](notas/ST-03-instalacao.md) | **Instalação** | verificado | O objeto que fatura. Tarifa, unidade de leitura, validação | 6 min |
| [`ST-04`](notas/ST-04-equipamento.md) | Equipamento e Registrador | misto | O medidor, o TC, as três formas de instalar | 8 min |

**Tudo: cerca de 91 minutos. Só os recalls: cerca de 15.**

---

## Em que ordem ler

`GE-03` → `GE-01` → `MD-01` → `MD-02` → então os dois ramos em paralelo:

| Comercial | Técnico |
|---|---|
| `MD-03` → `MD-04` → `MD-05` | `ST-01` → `ST-02` → `ST-03` → `ST-04` |

E os dois convergem em **`MD-06`**, seguido de **`MD-07`**.

`GE-02` e `GE-04` são folhas soltas: leia quando quiser. O porquê dessa ordem
está em [`notas/_DEPENDENCIAS.md`](notas/_DEPENDENCIAS.md), que também lista o
que ainda falta no material.

## As quatro que mais valem

1. **[`GE-03`](notas/GE-03-a-concessionaria.md)**, a concessionária. Sem o
   problema de negócio, o resto vira decoreba.
2. **[`MD-02`](notas/MD-02-a-traducao-do-predio.md)**, a tradução do prédio.
3. **[`MD-06`](notas/MD-06-contrato.md)**, o Contrato. O mais denso em regra.
4. **[`ST-03`](notas/ST-03-instalacao.md)**, a Instalação. O objeto que fatura.

---

# Material de apoio

| Arquivo | Para quê |
|---|---|
| [`referencia/02-BANCADA.md`](referencia/02-BANCADA.md) | Transações, tabelas e caminhos de menu. É consulta, use `Ctrl+F` |
| [`referencia/00-NUCLEO.md`](referencia/00-NUCLEO.md) | O mapa geral e um cartão de revisão de 2 minutos |
| [`referencia/FI-CA-detalhado.md`](referencia/FI-CA-detalhado.md) | Aprofundamento de FI-CA |
| [`notas/_GABARITOS.md`](notas/_GABARITOS.md) | Respostas dos recalls, separadas de propósito |

---

# Como isto funciona

**Nota atômica.** Um conceito por arquivo, teto de 120 linhas. Se cresce, vira
duas. Cada nota termina em **recall**, com perguntas sem resposta à vista.

**Nada aqui pede confiança cega.** Duas marcas dizem o grau:

| Marca | Significa |
|---|---|
| **verificado** | Conferido contra o sistema ou material de produto |
| **a confirmar** | Escrito por raciocínio e leitura, não conferido na documentação SAP |
| **(confirmar)** no texto | Código de transação específico de que não tenho certeza |

Prefiro a dúvida explícita a um código errado que alguém vai digitar na frente
de um cliente.

# Como contribuir

**Todo `(confirmar)` é um convite.** Se você roda IS-U em produção, sua
resposta vale mais que uma semana de leitura minha.

- **[Corrigir conteúdo](../../issues/new?template=correcao-de-conteudo.yml)**,
  quando algo está errado, incompleto ou confuso
- **[Confirmar transação](../../issues/new?template=confirmar-transacao.yml)**,
  quando você sabe um código marcado como duvidoso
- **[Ver o que está aberto](../../issues)**, se quiser pegar algo pronto
- [`CONTRIBUTING.md`](CONTRIBUTING.md) para o resto

Se você leu uma nota e não entendeu, **a nota está mal escrita**. Isso também
vale issue, e é o defeito que eu não consigo enxergar sozinho.

---

Trabalho independente, sem vínculo com a SAP nem com qualquer empregador.
SAP, SAP IS-U e S/4HANA são marcas da SAP SE. Nada aqui reproduz material de
treinamento proprietário, e este repositório não é fonte oficial: para decisão
de projeto, consulte a documentação da SAP.
