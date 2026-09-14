# TP2 — Análise Sintática: Avaliador de Expressões com Listener

Trabalho 02 da disciplina de Compiladores, desenvolvido para implementar um avaliador de expressões aritméticas utilizando o padrão de projeto **Listener** do **ANTLR** com **Python**.

## Sobre o trabalho

O avaliador suporta as seguintes operações, respeitando precedência e associatividade:

| Operação        | Sintaxe          | Exemplo          |
|-----------------|------------------|------------------|
| Parênteses      | `(expr)`         | `(2 + 3) * 4`   |
| Potenciação     | `expr ^ expr`    | `2 ^ 10`         |
| Multiplicação   | `expr * expr`    | `3 * 4`          |
| Divisão         | `expr / expr`    | `10 / 2`         |
| Soma            | `expr + expr`    | `1 + 2`          |
| Subtração       | `expr - expr`    | `5 - 3`          |
| Valor absoluto  | `abs(expr)`      | `abs(-7)`        |
| Fatorial        | `fat(expr)`      | `fat(5)`         |
| Número negativo | `-NUM`           | `-42`            |

A precedência é definida diretamente pela gramática ANTLR, do menor para o maior nível:
`SomaSub` < `MultDiv` < `Pot` < `Func/Number` < `Parent`

## Tecnologias

* Python 3.12
* ANTLR 4.13.2
* Docker

## Como executar

É necessário ter o Docker e o Docker Compose instalados.

Primeiro, construa a imagem:

```bash
docker compose build
```

Depois, execute o programa:

```bash
docker compose run --rm antlr
```

O programa entra em modo interativo. Digite expressões e pressione Enter para avaliá-las. Digite `sair` para encerrar.

```
Expressão: 3 + 2 * 6
Resultado = 15

Expressão: fat(5)
Resultado = 120

Expressão: abs(-3 + 1)
Resultado = 2

Expressão: 2 ^ 10
Resultado = 1024

Expressão: sair
```

Não é necessário executar `docker compose build` novamente ao alterar `EvalListener.py` ou `main.py`. A gramática `Expr.g4` é reprocessada automaticamente a cada execução.

## Estrutura

```text
.
├── Dockerfile
├── docker-compose.yml
├── Expr.g4
├── EvalListener.py
├── main.py
└── README.md
```

Os arquivos `Expr.g4`, `EvalListener.py` e `main.py` correspondem aos arquivos exigidos para a entrega do trabalho.