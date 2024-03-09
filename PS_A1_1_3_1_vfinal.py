import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
df_csv = pd.read_csv("Dataset_Processo_Seletivo_UFRJ_Analytica.csv")

# Filtrar os dados para o ano de 1991
df = df_csv[df_csv['ano'] == 1991].copy()  # Certificar-se de fazer uma cópia para evitar o aviso

# Calcular a população urbana total do Brasil
populacao_total_brasil = df['populacao_urbana'].sum()

# Calcular a proporção da população urbana de cada estado em relação à população urbana total do Brasil
df.loc[:, 'proporcao'] = df['populacao_urbana'] / populacao_total_brasil * 100  # Usar .loc para fazer atribuição diretamente no DataFrame original

# Ordenar os dados pela proporção em ordem decrescente
df_resultado_sorted = df.sort_values(by='proporcao', ascending=True)

# Criar o gráfico
fig, ax = plt.subplots(figsize=(9, 10))  # Definir o tamanho da figura e obter os objetos dos eixos
bars = ax.barh(df_resultado_sorted['sigla_uf'], df_resultado_sorted['proporcao'], color='#4CAF50')

# Personalizar o gráfico
ax.set_xlabel('Proporção da População Urbana (%)', fontsize=22, labelpad=20)
ax.set_ylabel('Estados', fontsize=22, rotation=0, labelpad=70)
ax.set_title('Proporção da População Urbana entre os Estados Brasileiros (1991)', fontsize=22)

# Definir limites e marcas do eixo x
ax.set_xlim(0, 31)
ax.set_xticks(range(0, 31, 10))

# Função para inserir os rótulos de dados (porcentagem) ao lado de cada barra
def insert_data_labels(bars):
    for bar in bars:
        bar_width = bar.get_width()
        ax.annotate('{:.1f}%'.format(bar_width),
                    xy=(bar.get_x() + bar_width, bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0),  # deslocamento horizontal
                    textcoords='offset points',
                    ha='left', va='center')

# Inserir porcentagens ao lado de cada barra
insert_data_labels(bars)

plt.show()
