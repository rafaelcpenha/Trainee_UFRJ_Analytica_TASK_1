import pandas as pd
import matplotlib.pyplot as plt

# Carregando o arquivo CSV em um DataFrame do pandas
df = pd.read_csv("Dataset_Processo_Seletivo_UFRJ_Analytica.csv")

# Filtrando os dados para os anos desejados
df_filtrado = df[df['ano'].isin([1991, 2010])].copy()

# Ordenando o DataFrame pelo ano e pela sigla da UF
df_filtrado.sort_values(by=['ano', 'sigla_uf'], inplace=True)

# Criando uma nova coluna para armazenar a diferença na expectativa de vida em relação ao ano anterior
df_filtrado['diff_expectativa_vida'] = df_filtrado.groupby('sigla_uf')['expectativa_vida'].diff()

# Filtrando estados com diferença na expectativa de vida maior que 10
df_diferenca_maior_10 = df_filtrado[abs(df_filtrado['diff_expectativa_vida']) > 10].copy()

# Ordenando o DataFrame pelo valor da diferença na expectativa de vida em ordem decrescente
df_diferenca_maior_10.sort_values(by='diff_expectativa_vida', ascending=False, inplace=True)

# Plotando o gráfico de barras
plt.figure(figsize=(10, 6))
bars = plt.bar(df_diferenca_maior_10['sigla_uf'], df_diferenca_maior_10['diff_expectativa_vida'])
plt.xlabel('Estados')
plt.ylabel('Diferença na Expectativa de Vida')
plt.title('Estados com Aumento na Expectativa de Vida ≥ 10 anos (1991-2010)')
plt.xticks(rotation=45)


# Adicionando os valores no topo de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 1), va='bottom', ha='center')

plt.show()
