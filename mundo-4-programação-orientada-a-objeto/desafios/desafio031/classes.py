class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._base = None
        self._altura = None
        self._area = None
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if base > 0:
            self._base = base
        else:
            raise ValueError(f"Base digitada inválida")

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if altura > 0:
            self._altura = altura
        else:
            raise ValueError(f"altura digitada inválida")
         
    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area 

    @property
    def medidas(self):
        return f'Base = {self._base} \nAltura = {self._altura} \nÁrea = {self._area}'

    @medidas.setter
    def medidas(self, tupla):
        if not isinstance(tupla, tuple):
            raise TypeError(f"As medidas devem ser informadas em uma Tupla")
        if len(tupla) != 2:
            raise SyntaxError("Informe uma tupla com apenas dois valores")
        if isinstance(tupla[0], float) or isinstance(tupla[0], int):
            self.base = tupla[0]
        else:
            raise TypeError("A base deve ser um número.")
        if isinstance(tupla[1], float) or isinstance(tupla[1], int):
            self.altura = tupla[1]
        else:
            raise TypeError("A altura deve ser um número.")
        

    