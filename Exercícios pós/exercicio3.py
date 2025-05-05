"""
Crie uma função que receba uma frase, e tambem que receba uma palavra.
Caso essa palavra esteja na frase, retorne True, caso não esteja, retorne False.
"""

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")


def contem_palavra():
    if palavra in frase:
        return True
    else:
        return False


print("A palavra aparece na frase?", contem_palavra())
