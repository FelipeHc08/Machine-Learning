# Criando uma matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprimindo a matriz
for linha in matriz:
    print(linha)

i = int(input("Informe i: "))
i -= 1
j = int(input("Informe j: "))
j -= 1
matriz[i][j] = 'X'

for linha in matriz:
    print(linha)


