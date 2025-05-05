"""
1. Crie uma função que analise o tipo de dado do argumento. Caso a entrada seja Int, quero que retorne float, e caso a
entrada seja float, quero que retorne Int.
Se entrar outro tipo, printar "Tipo não suportado".
"""


def converte_tipo():
    valor = input("Digite um número : ")

    try:
        convertido = int(valor)
        return float(convertido)
    except ValueError:
        try:
            convertido = float(valor)
            return int(convertido)
        except ValueError:
            print("Tipo inválido")

tipo_dado = converte_tipo()
print("Tipo de dado:", type(tipo_dado))
