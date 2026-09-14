from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalListener import EvalListener


def avaliar(expressao: str):
    """Analisa e avalia uma expressão aritmetica, retornando o resultado dela"""
    input_stream  = InputStream(expressao)
    lexer         = ExprLexer(input_stream)
    token_stream  = CommonTokenStream(lexer)
    parser        = ExprParser(token_stream)
    tree          = parser.root()

    listener = EvalListener()
    walker   = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.resultado_final


if __name__ == '__main__':
    print("Avaliador de Expressões — Compiladores")
    print("Operações: + - * / ^ abs(...) fat(...)")
    print("Digite 'sair' para encerrar.\n")

    while True:
        try:
            entrada = input("Expressão: ").strip()
        except EOFError:
            break

        if entrada.lower() == 'sair':
            break

        if not entrada:
            continue

        try:
            resultado = avaliar(entrada)
            # mostra inteiro quando o resultado não tem parte fracionaria
            if isinstance(resultado, float) and resultado.is_integer():
                print(f"Resultado = {int(resultado)}\n")
            else:
                print(f"Resultado = {resultado}\n")
        except ZeroDivisionError as e:
            print(f"Erro: {e}\n")
        except ValueError as e:
            print(f"Erro: {e}\n")
        except Exception as e:
            print(f"Erro inesperado: {e}\n")