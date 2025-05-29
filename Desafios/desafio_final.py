"""
Crie um programa que:

Solicite ao usuário nomes de frutas até digitar "sair".
Armazene essas frutas em uma lista.
Crie um dicionário que contenha como chave a fruta e como valor o número de letras.
Gere uma lista de compreensão com apenas as frutas que possuem mais de 5 letras.
Ordene e imprima a lista final.
"""

"""  for fruta in frutas:
      dicionario_frutas['fruta'] = len(fruta)
      tamanho_nome_fruta = len(fruta)
      if tamanho_nome_fruta > 5:
          frutas_cinco_letras.append(fruta)
      break
  print(f'frutas[] = {frutas} \nfrutas_cinco_letras = {frutas_cinco_letras} \ndicionario_frutas = {dicionario_frutas}')"""
import sys

opcao = input("Digite 'Sim' para iniciar ou 'Sair' para encerrar: ")
opcao = opcao.capitalize()
frutas = list()
frutas_cinco_letras = list()
dicionario_frutas = dict()

while opcao != "Sim" and opcao != "Sair":
    print("Opção inválida")
    opcao = input("Digite 'Sim' para iniciar ou 'Sair' para encerrar: ")
    opcao = opcao.capitalize()

if opcao == "Sair":
    print("Saindo...")
    sys.exit()

elif opcao == "Sim":
    while opcao != "Sair":
        opcao = input("Digite o nome de uma fruta ou digite 'sair': ")
        opcao = opcao.capitalize()
        if opcao == "Sair":
            frutas.sort()
            frutas_cinco_letras.sort()
            print("============================FINAL=====================================")
            print(f"Frutas com mais de 5 letras: {frutas_cinco_letras}")
            print(f"Frutas informadas: {frutas}")
            print(f"Dicionário [fruta: qtd letras]: {dicionario_frutas}")
            print("======================================================================")
            print("Saindo...")
            break
        dicionario_frutas[opcao] = len(opcao)
        if len(opcao) > 5:
            frutas_cinco_letras.append(opcao)
        frutas.append(opcao)

