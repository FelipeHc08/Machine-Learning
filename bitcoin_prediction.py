# Importa bibliotecas necessárias
import yfinance as yf  # Para obter dados financeiros do Yahoo Finance
import pandas as pd  # Para manipulação e análise de dados tabulares
import matplotlib.pyplot as plt  # Para criação de gráficos
from sklearn.ensemble import RandomForestClassifier  # Algoritmo de classificação baseado em floresta aleatória
from sklearn.metrics import precision_score, classification_report  # Métricas para avaliar desempenho do modelo
from sklearn.preprocessing import StandardScaler  # Normalização dos dados

# 1. Carrega os dados históricos do Bitcoin (em dólares)
acao = yf.Ticker("BTC-USD").history(period="max")  # Pega todo o histórico disponível
acao = acao.loc["2014-01-01":].copy()  # Filtra apenas os dados a partir de 2014
acao.drop(["Dividends", "Stock Splits"], axis=1, inplace=True)  # Remove colunas irrelevantes para criptomoedas

# 2. Cria coluna com o preço de fechamento do dia seguinte e uma coluna alvo (Target)
acao["Tomorrow"] = acao["Close"].shift(-1)  # Move o preço de fechamento um dia para cima (preço do dia seguinte)
acao["Target"] = (acao["Tomorrow"] > acao["Close"]).astype(int)  # Se o preço vai subir, target = 1, senão = 0

# 3. Adiciona indicadores técnicos como preditores
horizons = [2, 5, 60, 250, 1000]  # Janelas temporais para cálculos de médias e tendências
new_predictors = []  # Lista que armazenará os nomes das colunas criadas

# Calcula indicadores com base nos horizontes definidos
for horizon in horizons:
    acao[f"Close_Ratio_{horizon}"] = acao["Close"] / acao["Close"].rolling(horizon).mean()  # Relação entre o preço atual e a média móvel
    acao[f"Trend_{horizon}"] = acao["Target"].shift(1).rolling(horizon).sum()  # Número de dias de alta nos últimos 'horizon' dias
    new_predictors += [f"Close_Ratio_{horizon}", f"Trend_{horizon}"]  # Adiciona os nomes dos indicadores à lista de preditores

# Adiciona outros indicadores técnicos úteis
acao["Volatility_5"] = acao["Close"].pct_change().rolling(5).std()  # Volatilidade curta (5 dias)
acao["Volatility_20"] = acao["Close"].pct_change().rolling(20).std()  # Volatilidade média (20 dias)
acao["EMA_10"] = acao["Close"].ewm(span=10).mean()  # Média móvel exponencial de 10 dias

# RSI de 14 períodos (Índice de Força Relativa) — mede sobrecompra ou sobrevenda
acao["RSI_14"] = 100 - (100 / (1 + acao["Close"].pct_change().rolling(14).apply(
    lambda x: (x[x > 0].mean() / -x[x < 0].mean()) if x[x < 0].mean() != 0 else 0, raw=False)))

# Adiciona os nomes desses indicadores à lista de preditores
new_predictors += ["Volatility_5", "Volatility_20", "EMA_10", "RSI_14"]

# 4. Remove linhas com valores nulos gerados pelos cálculos anteriores
acao.dropna(inplace=True)

# 5. Normaliza os dados dos preditores para média 0 e desvio padrão 1
scaler = StandardScaler()
acao[new_predictors] = scaler.fit_transform(acao[new_predictors])  # Substitui os dados originais pelos normalizados

# 6. Função para treinar o modelo e gerar previsões
def predict(train, test, predictors, model, threshold=0.6):
    model.fit(train[predictors], train["Target"])  # Treina o modelo com os dados de treino
    probs = model.predict_proba(test[predictors])[:, 1]  # Obtém as probabilidades da classe "1" (alta)
    preds = (probs >= threshold).astype(int)  # Converte as probabilidades em classes com base no limiar
    return pd.concat([test["Target"], pd.Series(preds, index=test.index, name="Predictions")], axis=1)  # Retorna DataFrame com reais x previstos

# Função para simular o backtest em blocos de tempo crescentes
def backtest(data, model, predictors, start=1000, step=150):
    all_predictions = []
    for i in range(start, data.shape[0], step):
        train = data.iloc[0:i].copy()  # Usa os dados anteriores como treino
        test = data.iloc[i:(i + step)].copy()  # Usa os próximos "step" dias como teste
        predictions = predict(train, test, predictors, model)  # Executa predição
        all_predictions.append(predictions)  # Armazena as previsões
    return pd.concat(all_predictions)  # Junta tudo num único DataFrame

# 7. Define o modelo Random Forest com parâmetros mais robustos e balanceamento de classes
model = RandomForestClassifier(
    n_estimators=500,  # Número de árvores
    min_samples_split=10,  # Quantidade mínima de amostras para dividir um nó
    max_depth=10,  # Profundidade máxima da árvore
    max_features='sqrt',  # Quantidade de variáveis usadas por nó (raiz quadrada)
    class_weight='balanced',  # Balanceia pesos das classes automaticamente
    random_state=1  # Fixa a aleatoriedade para reprodutibilidade
)

# 8. Executa o backtest com os preditores criados
predictions = backtest(acao, model, new_predictors)

# 9. Realiza previsão com os dados mais recentes
latest_data = acao.iloc[-1:][new_predictors]  # Pega a última linha do DataFrame com preditores
proba = model.predict_proba(latest_data)[:, 1][0]  # Obtém a probabilidade de alta

# Gera uma recomendação com base na probabilidade
if proba >= 0.6:
    recomendacao = "📈 Comprar"
elif proba <= 0.4:
    recomendacao = "📉 Vender"
else:
    recomendacao = "🤝 Segurar"

# Mostra o resultado
print(f"\nProbabilidade de alta para o próximo dia: {proba:.2%}")
print(f"Ação recomendada: {recomendacao}")

# 10. Avaliação de desempenho do modelo com os dados do backtest
print("\nContagem de previsões:")
print(predictions["Predictions"].value_counts())  # Quantas vezes o modelo recomendou compra ou venda

print("\nPrecisão do modelo:")
print(precision_score(predictions["Target"], predictions["Predictions"]))  # Precisão: quantas previsões de alta foram corretas

print("\nRelatório completo:")
print(classification_report(predictions["Target"], predictions["Predictions"], digits=3))  # Métricas completas (precisão, recall, F1)

# 11. Gráfico com o histórico de preços do Bitcoin
acao["Close"].plot(title="Histórico de Fechamento Bitcoin (USD)", figsize=(12, 6))
plt.xlabel("Data")
plt.ylabel("Preço de Fechamento (BRL)")
plt.grid(True)
plt.tight_layout()
plt.show()  # Exibe o gráfico
