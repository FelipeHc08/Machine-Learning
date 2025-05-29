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

def recuperacao(nome, notas):
    notas.sort()
    nova_nota = float(input(f"\n{nome.upper()} está em recuperação.\nInforme a nova nota para substituir a menor ({notas[0]}): "))
    if nova_nota > notas[0]:
        notas[0] = nova_nota
        print(f"Notas atualizadas de {nome.upper()}: {notas}")
    else:
        print("Nota não foi suficiente para substituir a menor.")

for nome, dados in alunos.items():
    notas = dados["Notas"]
    media = sum(notas) / 3
    dados["Média"] = media

    if media >= 7:
        dados["Situação"] = "Aprovado"
    elif media >= 5:
        recuperacao(nome, notas)
        nova_media = sum(notas) / 3
        dados["Média"] = nova_media
        dados["Situação"] = "Aprovado" if nova_media >= 7 else "Recuperação"
    else:
        dados["Situação"] = "Reprovado"

# Exibição formatada
print("\n========== RESULTADO FINAL ==========")
for nome, dados in alunos.items():
    print(f"\nAluno: {nome.upper()}")
    print(f"Notas: {dados['Notas']}")
    print(f"Média: {dados['Média']:.2f}")
    print(f"Situação: {dados['Situação']}")
