from abc import ABCMeta, abstractmethod
from functools import total_ordering


@total_ordering
class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        self._saldo -= valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __eq__(self, other):
        return other._codigo == self._codigo

    def __lt__(self, other):
        return self._saldo < other._saldo

    def __str__(self):
        return f"Código: {self._codigo} - Saldo: {self._saldo}"


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


class ContaInvestimento(Conta):
    def passa_o_mes(self):
        pass
