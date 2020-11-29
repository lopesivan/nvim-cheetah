class Calc:
    def __init__(self, formula, **vars):
        self.formula = formula
        self.vars    = vars

        self.__recalc()

    def __recalc(self):
        self.__res = eval(self.formula, self.vars)

    def __repr__(self):
        self.__recalc()
        return str(self.__res)

