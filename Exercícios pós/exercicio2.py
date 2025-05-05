"""
Crie uma função que receba uma frase, e também que receba uma palavra.
retorne a frase substituindo a palavra por "****" e print a frase.
"""

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

def substitui_palavra(frase, palavra):
    frase_sem_palavra = frase.replace(palavra, "****")
    print(frase_sem_palavra)
    return frase_sem_palavra

substitui_palavra(frase, palavra)