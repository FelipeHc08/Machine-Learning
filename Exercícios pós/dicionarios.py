"""
Crie um dicionário que armazene informações sobre um Aluno (nome, idade, curso).

Adicione um novo campo nota.
Altere a idade.
Remova o campo curso.
Some 0.5 na nota.
Imprima o dicionário final.
"""

aluno = {
    "Nome": "João",
    "Idade": 25,
    "Curso": "Engenharia de Software"
}
print(aluno)
aluno["Nota"] = 5.5
print(aluno)
aluno["Idade"] = 26
print(aluno)
del aluno["Curso"]
print(aluno)
aluno["Nota"] += 0.5
print(aluno)
