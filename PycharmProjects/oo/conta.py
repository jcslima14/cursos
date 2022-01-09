class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto .. {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo do titular {} é de R$ {}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O seu limite para saque é de {}".format(self.__saldo + self.__limite))

    def transfere(self, valor, conta):
        self.saca(valor)
        conta.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return { "BB": "001", "Itau": "341", "Caixa": "104", "Inter": "077", "Bradesco": "237" }