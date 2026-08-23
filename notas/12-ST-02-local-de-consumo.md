# ST-02: Local de Consumo
> A unidade que recebe energia e é medida separadamente. O apartamento dentro
> do prédio.

**Em inglês:** `Premise`. Use o nome em inglês quando a tradução em
português divergir entre materiais.
**Onde entra:** o nível do meio do mundo técnico.
**Antes disto:** [ST-01-objeto-de-ligacao](11-ST-01-objeto-de-ligacao.md)
**Origem:** **slide.** O material da academia sustenta esta nota inteira.

---

## O que é

- Representa uma **unidade provida de energia elétrica e medida
  separadamente**
- **Assume o endereço do Objeto de Ligação**
- **É onde informamos o complemento do endereço**
- É criado quando surge uma **nova Unidade Consumidora**
- Campos relevantes:
  - **Tipo do Local de Consumo**
  - **Complemento do endereço**

---

## Exemplos

Andar · Apartamento · Lojas · Pilotis · Caixas · Pontos de ônibus ·
Torres de Telefonia · Outdoors · Bancas de Jornal · **IP e Semaforização**

`IP` é Iluminação Pública.

---

## A divisão do endereço

```
OBJETO DE LIGAÇÃO ──┬──▶ LOCAL DE CONSUMO 1
Rua das Acácias, 214│    Apto 101
o ENDEREÇO          │    o COMPLEMENTO
                    │
                    └──▶ LOCAL DE CONSUMO 2
                         Apto 102
                         o COMPLEMENTO
```

**Uma pergunta, duas respostas, dois objetos.** Endereço em cima,
complemento embaixo.

---

## O erro que todo mundo comete

**Achar que "medida separadamente" quer dizer "tem medidor".**

Não. Quer dizer que aquela unidade **é uma unidade de medição autônoma no
cadastro**. O medidor físico está em outro objeto, o Local de Instalação de
Equipamento, geralmente na garagem.

Local de Consumo é onde se **consome**. O relógio fica noutro lugar.

---

## No sistema

| Transação | O quê |
|---|---|
| `ES60` | Criar Local de Consumo |
| `ES61` | Modificar Local de Consumo |
| `ES62` | Exibir Local de Consumo |

Caminho: `Serviços públicos > Dados mestre técnicos > Local de consumo`

> **Atenção ao código de criação.** `ES61` modifica e `ES62` exibe. **Para
> criar, o correto é `ES60`.** Códigos parecidos como `ES53` não pertencem a
> este objeto.

**Exercício:** criar um local de consumo para o objeto de ligação
criado, e modificar o número/apto dele.

---

## Se sobrar uma coisa

O Local de Consumo herda o endereço do prédio e guarda só o complemento.

---

## Recall

1. Qual transação cria um Local de Consumo?
2. Qual transação modifica um Local de Consumo?
3. Qual transação exibe um Local de Consumo?
4. De onde vem o endereço do Local de Consumo?
5. Nomeie os dois campos relevantes do Local de Consumo.
6. Um prédio de 40 apartamentos tem quantos Objetos de Ligação?
7. O mesmo prédio tem quantos Locais de Consumo?
8. Um colega diz que `ES61` cria o Local de Consumo. Cite o que corrigir.

> **Gabarito:** [`_PISTAS.md`](_PISTAS.md#st-02)  ·  responda tudo antes de abrir.
