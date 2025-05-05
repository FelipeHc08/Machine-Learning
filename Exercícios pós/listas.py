"""
Você é responsável por desenvolver uma ferramenta de análise de despesas mensais. Crie uma lista contendo os valores
gastos em cada dia do mês (assuma 30 dias), onde cada valor representa os gastos diários em reais.

Implemente uma função que:

Calcule a média de gastos do mês.

Retorne uma nova lista contendo apenas os dias em que os gastos foram acima da média.

Retorne também a quantidade de dias acima da média.

Ao final, apresente um relatório formatado (printado) contendo:

Total gasto no mês.

Média de gastos.

Lista dos dias com gastos acima da média, ordenados do maior para o menor.

Percentual de dias acima da média.

O maior e o menor gasto do mês.

Os 3 maiores e os 3 menores gastos do mês.

Use métodos como: sum(), len(), sorted(), max(), min(), enumerate(), list comprehensions, format() e outros que achar
necessário.


"""

import random

gastos = [round(random.uniform(20, 300), 2) for _ in range(30)]
print(f"Gastos mensais: {gastos}")


def media_mensal(gastos):
    media = sum(gastos) / len(gastos)
    return media


def analisar_media(gastos, media):
    return [valor for valor in gastos if valor > media]


def porcentagem(dias_totais, dias_acima_media):
    return (100 * dias_acima_media) / dias_totais


media = media_mensal(gastos)
acima_media = analisar_media(gastos, media)
acima_media.sort(key=None, reverse=True)
dias_acima_media = len(acima_media)
porcentagem = porcentagem(30, dias_acima_media)
gastos.sort()

print(f"Total gasto no mês: R$ {sum(gastos)}")
print(f"Média de gastos: R$ {media:.2f}")
print(f"Quantidade de dias em que os gastos foram acima da média: {dias_acima_media}")
print(f"Percentual de dias acima da média: {porcentagem:.2f}%")
print(f"Maior gasto do mês: {max(gastos)}")
print(f"Menor gasto do mês: {min(gastos)}")
print(f"Três maiores gastos do mês: {acima_media[0:3]}")
print(f"Três menores gastos do mês: {sorted(acima_media[-3:])}")
