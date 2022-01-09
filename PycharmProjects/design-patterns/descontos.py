class Desconto_por_volume(object):

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if (orcamento.total_itens > 5):
            return orcamento.valor * 0.1
        else:
            return self.__proximo_desconto.calcula(orcamento)


class Desconto_por_valor(object):

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if (orcamento.valor > 500):
            return orcamento.valor * 0.07
        else:
            return self.__proximo_desconto.calcula(orcamento)


class Sem_desconto(object):

    def calcula(self, orcamento):
        return 0
