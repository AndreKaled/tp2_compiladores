from ExprListener import ExprListener
from ExprParser import ExprParser


class EvalListener(ExprListener):
    """
    Listener que avalia expressões aritmeticas com suporte a:
    - Parenteses
    - Potenciacao (^)
    - Multiplicacao e divisao (* /)
    - Soma e subtracao (+ -)
    - Valor absoluto: abs(expr)
    - Fatorial: fat(expr)
    """

    def __init__(self):
        # dicionario que associa cada no da arvore ao seu valor calculado
        self.valores = {}

    def exitParent(self, ctx: ExprParser.ParentContext):
        """'(' expr ')' repassa o valor da sub-expressao"""
        self.valores[ctx] = self.valores[ctx.expr()]

    def exitPot(self, ctx: ExprParser.PotContext):
        """expr '^' expr potenciacao"""
        base = self.valores[ctx.expr(0)]
        exp  = self.valores[ctx.expr(1)]
        self.valores[ctx] = base ** exp

    def exitMultDiv(self, ctx: ExprParser.MultDivContext):
        """expr ('*'|'/') expr  multiplicação ou divisão"""
        esq = self.valores[ctx.expr(0)]
        dir = self.valores[ctx.expr(1)]
        op  = ctx.getChild(1).getText()

        if op == '*':
            self.valores[ctx] = esq * dir
        else:
            if dir == 0:
                raise ZeroDivisionError("Erro semântico: divisão por zero.")
            self.valores[ctx] = esq / dir

    def exitSomaSub(self, ctx: ExprParser.SomaSubContext):
        """expr ('+'|'-') expr  soma ou subtração"""
        esq = self.valores[ctx.expr(0)]
        dir = self.valores[ctx.expr(1)]
        op  = ctx.getChild(1).getText()

        if op == '+':
            self.valores[ctx] = esq + dir
        else:
            self.valores[ctx] = esq - dir

    def exitFunc(self, ctx: ExprParser.FuncContext):
        """(abs_ | fact) repassa o valor calculado pela função"""
        filho = ctx.getChild(0)
        self.valores[ctx] = self.valores[filho]

    def exitNumber(self, ctx: ExprParser.NumberContext):
        """('-')? NUM número literal, possivelmente negativo"""
        texto = ctx.getText()
        self.valores[ctx] = float(texto) if '.' in texto else int(texto)

    # funcoes auxiliares aqui embaixo
    
    def exitAbs_(self, ctx: ExprParser.Abs_Context):
        """abs(expr) — valor absoluto."""
        self.valores[ctx] = abs(self.valores[ctx.expr()])

    def exitFact(self, ctx: ExprParser.FactContext):
        """fatorial (somente inteiros positivos)"""
        valor = self.valores[ctx.expr()]

        if valor != int(valor) or valor < 0:
            raise ValueError(
                f"Erro semântico: fatorial indefinido para {valor}."
            )

        self.valores[ctx] = _fatorial(int(valor))

    def exitRoot(self, ctx: ExprParser.RootContext):
        self.resultado_final = self.valores[ctx.expr()]


def _fatorial(n: int) -> int:
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado