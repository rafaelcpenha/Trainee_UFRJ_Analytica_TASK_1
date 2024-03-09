import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar DataFrame a partir do arquivo CSV
df = pd.read_csv("Dataset_Processo_Seletivo_UFRJ_Analytica.csv")

def plotar_histograma(ano, coluna, max_height):
    """
    Função para plotar o histograma de uma coluna do DataFrame para um ano específico.

    Argumentos:
      ano: Ano a ser analisado.
      coluna: Nome da coluna a ser plotada.
      max_height: Altura máxima da distribuição de frequência entre todos os anos.
    """

    # Filtrar os dados para o ano especificado
    df_ano = df.loc[df['ano'] == ano]

    # Criar o histograma com bins automáticos
    plt.hist(df_ano[coluna], bins='auto')
    plt.xlabel(coluna.upper(), fontsize=18)  # Convertendo a label do eixo x para maiúsculas
    plt.ylabel("Quantidade de Estados", fontsize=18)
    
    # Título do gráfico com o nome da coluna em maiúsculas
    plt.title(f"Histograma - {coluna.upper()} - {ano}", fontsize=18)

    # Definir limite do eixo x com base nos valores mínimos e máximos da coluna para todos os anos, com uma margem de 5%
    x_min = df[coluna].min() * 0.95
    x_max = df[coluna].max() * 1.05
    plt.xlim(x_min, x_max)

    # Definir limite do eixo y com base na altura máxima da distribuição de frequência entre todos os anos, com uma margem de 5%
    plt.ylim(0, max_height * 1.05)

    # Ajustar o tamanho da fonte para o eixo x e y
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    plt.show()

# Calcular a altura máxima da distribuição de frequência entre todos os anos
max_height = 0
for ano in df['ano'].unique():
    counts, _ = np.histogram(df[df['ano'] == ano]['idhm'], bins='auto')
    max_height = max(max_height, max(counts))

# Lista de anos únicos
anos = df['ano'].unique()

# Iterar sobre os anos e plotar o histograma para cada ano
for ano in anos:
    plotar_histograma(ano, 'idhm', max_height)
