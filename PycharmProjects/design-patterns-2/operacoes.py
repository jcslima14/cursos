class Numero(object):

    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero


class Substracao(object):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return (self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia())

class Soma(object):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return (self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia())


if __name__ == '__main__':

    expressao_esquerda = Soma(Numero(10), Numero(20))
    expressao_direita = Soma(Numero(2), Numero(5))

    print(Soma(expressao_esquerda, expressao_direita).avalia())
    print(Substracao(expressao_esquerda, expressao_direita).avalia())
