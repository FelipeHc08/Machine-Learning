"""
🧠 Desafio Prático: Análise de Dados de Livros 📚
Você é um analista de dados em uma livraria online.

Etapas do desafio:
Leitura do Dataset

Leia o arquivo CSV ou Excel contendo os dados dos livros.

Exploração Inicial

Mostre as 5 primeiras linhas do DataFrame.

Mostre os nomes das colunas disponíveis.

Mostre o número de linhas e colunas do dataset.

Filtro de Livros com Preço Acima da Média

Calcule a média de preço (coluna price) e filtre os livros com preço acima da média.

Mostre apenas as colunas: title, price, author.

Filtrar por Idioma e Avaliação

Selecione os livros em espanhol(language == 'Spanish') que têm avaliação média (avg_reviews) acima de 4.5 (Faça isso em uma linha).

Exiba as colunas: title, avg_reviews, language.

Questão Desafio - Não Obrigatório

Criação de Coluna Nova – Valor Total

Crie uma nova coluna chamada valor_estimado, que é o produto de price × n_reviews (convertendo n_reviews para número inteiro antes).

Exiba os livros com maior valor_estimado em ordem decrescente (mostre os 5 primeiros).
"""

import pandas as pd
import numpy as np

# Lendo arquivo base
dados_livros = pd.read_csv('book_dataset.csv')

# Exibir as primeiras 5 linhas (método head())
print("Exibindo as 5 primeiras linhas (head):")
print(dados_livros.head())
print('=' * 50)

# Exibir nome das colunas (.columns)
print("Exibindo nome das colunas:")
print(dados_livros.columns)
print('=' * 50)

# Exibir quantidade de linhas e de colunas (.shape)
print("Exibindo número de linhas e colunas do dataset:")
print(dados_livros.shape)
print('=' * 50)


print("Filtro de Livros com Preço Acima da Média\n")

# Calcular a média (.mean)
media = np.mean(dados_livros['price'])

# Exibir média formatada (0.00)
print(f"Média de preço: {media:.2f}")

# Filtrando apenas os valores maiores que a média
filtro_media = dados_livros[dados_livros['price'] > media][['title', 'price', 'author']]
print(f"Livros com valor acima da média: {filtro_media}")
print('=' * 50)


print("Filtrar por Idioma e Avaliação")
filtro_linguagem_avaliacao = dados_livros[
    (dados_livros['avg_reviews'] > 4.5) & (dados_livros['language'] == 'Spanish')
][['title', 'avg_reviews', 'language']]
print(filtro_linguagem_avaliacao)
print('=' * 50)
print("Criação de Coluna Nova – Valor Total")
dados_livros['n_reviews'] = pd.to_numeric(dados_livros['n_reviews'], errors='coerce')
dados_livros['valor_estimado'] = dados_livros['price'] * dados_livros['n_reviews']
dados_livros.sort_values(by='valor_estimado', ascending=False, inplace=True)
print(dados_livros['valor_estimado'].head())
print('=' * 50)

