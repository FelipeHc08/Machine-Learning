"""
🧠 Desafio POO

Implemente as seguintes classes:

Etapas do desafio:
Classe `Veiculo` com atributos `marca`, `modelo`, e `ano`. Método `descricao`.

 Subclasse `Carro` que herda de `Veiculo`, adiciona `porta_malas` e sobrescreve `descricao`.

Crie uma função que receba uma lista de veículos (de tipos diferentes) e imprima suas descrições.
Teste seu código criando objetos reais e executando a função com eles.

"""


class Veiculo:
    def __init__(self):
        self.marca = None
        self.modelo = None
        self.ano = None

    def descricao(self):
        print(f"Descrição do veículo: {self.marca}, {self.modelo}, {self.ano}")


class Carro(Veiculo):
    def __init__(self):
        super().__init__()
        self.porta_malas = None

    def descricao(self):
        print(f"Descrição do veículo: {self.marca}, {self.modelo}, {self.ano}, {self.porta_malas}")


veiculo1 = Veiculo()
veiculo1.marca = "Toyota"
veiculo1.modelo = "Corolla"
veiculo1.ano = 2020

carro1 = Carro()
carro1.marca = "Volkswagen"
carro1.modelo = "Golf"
carro1.ano = 2022
carro1.porta_malas = "420 litros"

veiculos = [veiculo1, carro1]


def exibir_descricoes(lista_de_veiculos):
    for v in lista_de_veiculos:
        v.descricao()


exibir_descricoes(veiculos)
