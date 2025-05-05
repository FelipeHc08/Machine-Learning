"""
Crie uma função que recebe um número representando a idade e recebe outro parametro que vai ser um booleano
(True ou False). Se ele tiver mais de 18 anos e o booleano for True, retorne "Maior de idade e pode dirigir".
caso ele tenha mais de 18 anos e o booleano for False, retorne "Maior de idade e não pode dirigir".
caso ele tenha menos de 18 anos e o booleano for True, retorne "Menor de idade e a carteira é falsa".
caso ele tenha menos de 18 anos e o booleano for False, retorne "Menor de idade e não pode dirigir".
"""

idade = int(input("Informe sua idade: "))

carteira = input("Possui carteira (Sim/Não)? ")
carteira = carteira.capitalize()
tem_carteira = False

while carteira != "Sim" and carteira != "Não":
    print("Resposta inválida")
    carteira = input("Possui carteira (Sim/Não)? ")
    carteira = carteira.capitalize()

if carteira == "Sim":
    tem_carteira = True


def pode_dirigir(idade, tem_carteira):
    if idade >= 18 and tem_carteira == True:
        return print("Maior de idade e pode dirigir")
    elif idade >= 18 and tem_carteira == False:
        return print("Maior de idade e não pode dirigir")
    elif idade < 18 and tem_carteira == True:
        return print("Menor de idade e a carteira é falsa")
    elif idade < 18 and tem_carteira == False:
        return print("Menor de idade e não pode dirigir")


pode_dirigir(idade, tem_carteira)
