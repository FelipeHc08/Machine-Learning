"""
Crie um código de Menu, onde o usuário vai escolher uma opção de 1 a 4.
O código tem que continuar executando enquanto o usuário não escolher a opção 0.
O que deve conter nas opções de 1 a 4 é de escolha do usuário, o principal é que
o código continue executando enquanto o usuário não escolher a opção 0.
"""


def exibeMenu():
    return print("MENU \n0 - Encerrar\n1 - Identificar tipo de dados\n2 - Substir palavra na frase\n3 - Verificar se "
                 "a palavra está na frase\n4 - Calculadora")


exibeMenu()
menu = int(input("Selecione uma opção: "))

while menu != 0:
    if menu < 0 or menu > 4:
        print("Opção inválida! Tente novamente!")
        menu = int(input("Selecione uma opção: "))
    elif menu == 1:
        print("=============IDENTIFICAR TIPO DE DADO=========================")
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

        exibeMenu()
        menu = int(input("Selecione uma opção: "))
    elif menu == 2:
        print("=============SUBSTITUIR PALAVRA NA FRASE======================")
        frase = input("Digite uma frase: ")
        palavra = input("Digite uma palavra: ")


        def substitui_palavra(frase, palavra):
            frase_sem_palavra = frase.replace(palavra, "****")
            print(frase_sem_palavra)
            return frase_sem_palavra


        substitui_palavra(frase, palavra)

        exibeMenu()
        menu = int(input("Selecione uma opção: "))
    elif menu == 3:
        print("=============VERIFICAR SE A PALAVRA ESTÁ NA FRASE=============")
        frase = input("Digite uma frase: ")
        palavra = input("Digite uma palavra: ")


        def contem_palavra():
            if palavra in frase:
                return True
            else:
                return False


        print("A palavra aparece na frase?", contem_palavra())

        exibeMenu()
        menu = int(input("Selecione uma opção: "))
    elif menu == 4:
        print("=============CALCULADORA======================================")
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
                return print(f"{numero1} / {numero2} = {numero1 / numero2}") if numero2 != 0 else print(
                    "Divisão por zero!")
            elif operador == "//":
                return print(f"{numero1} // {numero2} = {numero1 // numero2}") if numero2 != 0 else print(
                    "Divisão por zero!")
            elif operador == "%":
                return print(f"{numero1} % {numero2} = {numero1 % numero2}") if numero2 != 0 else print(
                    "Divisão por zero!")
            elif operador == "**":
                return print(f"{numero1} ** {numero2} = {numero1 ** numero2}")
            else:
                return print("Operador inválido")


        operacao(numero1, numero2, operador)

        exibeMenu()
        menu = int(input("Selecione uma opção: "))
    else:
        print("Encerrando programa...")