"""
5. Métodos Especiais – Desafio: Carrinho de Compras
Contexto: Um e-commerce deseja manipular objetos de carrinho com mais naturalidade.

Desafio:

Crie a classe Carrinho com uma lista de itens e método adicionar_item(nome).

Implemente __len__ para retornar a quantidade de itens.

Implemente __str__ para retornar os itens separados por vírgula.

Teste imprimindo o carrinho e aplicando len(carrinho).
"""


class Carrinho:
    def __init__(self):
        self.produto = []

    def adicionar_item(self, nome):
        self.produto.append(nome)

    def quantidade_itens(self):
        print(self.produto.__len__())

    def mostrar_itens(self):
        print(self.produto.__str__())


carrinho = Carrinho()

while True:
    produto = input("Informe o produto: ")
    if produto == '0':
        carrinho.quantidade_itens()
        carrinho.mostrar_itens()
        break
    else:
        carrinho.adicionar_item(produto)
