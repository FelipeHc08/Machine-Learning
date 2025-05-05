"""
Crie uma função de calculadora, aonde ela vai receber 2 números, e um operador.
retorne o resultado da operação. Caso seja um operador inválido, retorne "Operador inválido".
"""

numero1 = int(input("Informe um número: "))
numero2 = int(input("Informe outro número: "))
operador = input("Informe o operador (+, -, *, /, //, %, **): ")


def operacao(numero1, numero2, operador):
    if operador == "+":
        return print(f"{numero1} + {numero2} = {numero1 + numero2}")
    elif operador == "-":
        return print(f"{numero1} - {numero2} = {numero1 - numero2}")
    elif operador == "*":
        return print(f"{numero1} * {numero2} = {numero1 * numero2}")
    elif operador == "/":
        return print(f"{numero1} / {numero2} = {numero1 / numero2}") if numero2 != 0 else print("Divisão por zero!")
    elif operador == "//":
        return print(f"{numero1} // {numero2} = {numero1 // numero2}") if numero2 != 0 else print("Divisão por zero!")
    elif operador == "%":
        return print(f"{numero1} % {numero2} = {numero1 % numero2}") if numero2 != 0 else print("Divisão por zero!")
    elif operador == "**":
        return print(f"{numero1} ** {numero2} = {numero1 ** numero2}")
    else:
        return print("Operador inválido")


operacao(numero1, numero2, operador)
