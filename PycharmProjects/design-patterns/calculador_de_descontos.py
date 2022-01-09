from descontos import Desconto_por_valor, Desconto_por_volume, Sem_desconto


class Calculador_de_descontos(object):

    def calcula(self, orcamento):
        desconto = Desconto_por_volume(
            Desconto_por_valor(
                Sem_desconto()
            )
        ).calcula(orcamento)
        return desconto


if __name__ == "__main__":
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item("Item 1", 100.0))
    orcamento.adiciona_item(Item("Item 3", 50.0))
    orcamento.adiciona_item(Item("Item 4", 100.0))
    orcamento.adiciona_item(Item("Item 4", 100.0))
    orcamento.adiciona_item(Item("Item 4", 100.0))
    orcamento.adiciona_item(Item("Item 4", 100.0))

    print(orcamento.valor)

    calculador = Calculador_de_descontos()
    print(calculador.calcula(orcamento))