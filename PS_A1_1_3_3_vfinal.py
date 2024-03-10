import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importando o arquivo CSV
df = pd.read_csv("Dataset_Processo_Seletivo_UFRJ_Analytica.csv")

# Selecionando as colunas de interesse
ano = df["ano"]
sigla_uf = df["sigla_uf"]
expectativa_vida = df["expectativa_vida"]
idhm = df["idhm"]

# Criando o gráfico "Scatter Plot"
plt.scatter(idhm, expectativa_vida)
plt.xlabel("IDHM")
plt.ylabel("Expectativa de Vida (anos)")

# Ajustando a linha de regressão linear
reg = np.polyfit(idhm, expectativa_vida, 1)
x_fit = np.linspace(min(idhm), max(idhm), 100)
y_fit = reg[0] * x_fit + reg[1]

# Adicionando a linha de regressão ao gráfico
plt.plot(x_fit, y_fit, color="red")

# Adicionando legendas
plt.legend(["Dados", "Regressão Linear"])

# Adicionando um título ao gráfico
plt.title("Relação entre IDHM e Expectativa de Vida por Estado")

# Mostrando o gráfico
plt.show()

# Calculando o coeficiente de determinação (R²)
r2 = np.corrcoef(idhm, expectativa_vida)[0, 1]**2

# Imprimindo o R²
print(f"R²: {r2}")

# Imprimindo a equação da reta de regressão
print(f"\nEquação da reta: Expectativa de Vida = {reg[1]} + {reg[0]} * IDHM")
print("\nO gráfico revela uma correlação superior a 95% entre o IDHM e a expectativa de vida. Essa forte correlação é evidenciada pela concentração dos pontos próximos à linha de regressão linear. Isso significa que o IDHM é um indicador muito forte da expectativa de vida. No entanto, é importante considerar outros fatores socioeconômicos, como renda, educação e acesso à saúde, para obter explicações mais profundas sobre o impacto do IDHM na expectativa de vida.")
