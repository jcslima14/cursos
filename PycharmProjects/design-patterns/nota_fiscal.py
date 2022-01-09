from datetime import date


class Item(object):

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class Nota_fiscal(object):

    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes="", observadores=[]):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception("Detalhes da NF não pode ter mais de 20 caracteres")
        self.__detalhes = detalhes
        self.__itens = itens

        for observador in observadores:
            observador(self)

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def detalhes(self):
        return self.__detalhes

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    def __repr__(self):
        return f"CNPJ: {self.__cnpj} - Razão Social: {self.__razao_social} - Data Emissão: {self.__data_de_emissao} - Detalhes: {self.__detalhes}"


if __name__ == "__main__":
    from criador_de_nota_fiscal import Criador_de_nota_fiscal
    from observadores import imprime, envia_por_email, salva_no_banco

    itens = [Item("Item A", 100), Item("Item B", 200)]
    nota_fiscal = (Criador_de_nota_fiscal()
                   .com_cnpj(123)
                   .com_razao_social("askdflksdfj")
                   .com_itens(itens)
                   .com_detalhes("sjdfhd")
                   .constroi())

    nota_fiscal2 = Nota_fiscal(
        cnpj=123,
        razao_social="JCSL Enterprises",
        itens=itens,
        # data_de_emissao=date.today(),
        detalhes="",
        observadores=[imprime, envia_por_email, salva_no_banco])

    imprime(nota_fiscal)
    print(nota_fiscal2)
