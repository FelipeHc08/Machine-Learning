"""
🧠 Desafio Final: Cadastro de 3 Alunos com Análise de Notas
💼 Contexto
Você precisa desenvolver um programa simples para uma escola fictícia, que receberá dados de 3 alunos, suas notas, e
imprimirá a situação de cada um com base na média. caso ele fique de recuperação, quero que ele tenha a opção de fazer
a prova de recuperação, e troque a pior nota dele, e recalcule a media.

📋 Requisitos
Cadastrar 3 alunos:

Nome do aluno

Nota 1, Nota 2 e Nota 3

Calcular a média

Exibir resultado formatado com:

Nome em letras maiúsculas

Média

Situação:

Aprovado (média ≥ 7)

Recuperação (5 ≤ média < 7)

Reprovado (média < 5)

OBS: Recriar utilizando apenas 1 dicionário
** Dica: Não precisa utilizar o input(). ** Dica: Uma lista pode receber dicionários e um dicionário pode receber listas
"""

alunos = {
    "Felipe": {
        "Notas": [7.5, 8, 9.5],
        "Situação": "Indefinido"
    },
    "Arthur": {
        "Notas": [5.5, 6, 8],
        "Situação": "Indefinido"
    },
    "Beatriz": {
        "Notas": [5.5, 5, 3],
        "Situação": "Indefinido"
    }
}

print(alunos)


def recuperacao(nome, notas):
    notas.sort()
    nova_nota = float(input(f"Informe a nota obtida na recuperação, {nome}: "))
    if nova_nota > notas[0]:
        notas[0] = nova_nota
    print(f"Notas finais de {nome}: {notas}")

for nome, dados in alunos.items():
    print(f"Notas de {nome}: {dados['Notas']}")
    media = sum(dados['Notas']) / 3
    dados['Média'] = media
    if media >= 7:
        dados["Situação"] = "Aprovado"
    elif media < 7 and 5 < media:
        dados["Situação"] = "Recuperação"
        recuperacao(nome, dados['Notas'])
    elif media < 5:
        dados["Situação"] = "Reprovado"


print(alunos)
