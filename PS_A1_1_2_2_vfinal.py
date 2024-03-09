# Importando bibliotecas necessárias
import pandas as pd

# Carregando o conjunto de dados socioeconômicos brasileiros
df = pd.read_csv("Dataset_Processo_Seletivo_UFRJ_Analytica.csv")

# Filtrando os dados do ano de 1991
df_1991 = df[df['ano'] == 1991]

# Calculando a média do Índice de Desenvolvimento Humano Municipal (IDHM)
idh_media = df_1991['idhm'].mean()
print("Média do IDHM em 1991:", idh_media)

# Selecionando os registros com IDHM acima da média calculada
acima_da_media = df_1991[df_1991['idhm'] > idh_media]
print("\nRegistros com IDHM acima da média:")
print(acima_da_media[['ano', 'sigla_uf', 'expectativa_vida', 'populacao_urbana', 'populacao_rural', 'idhm']])

# Ordenando os dados com IDHM acima da média em ordem crescente de IDHM
df_ordenado = acima_da_media.sort_values(by='idhm')

# Exibindo os primeiros 5 registros do DataFrame ordenado
print("\nTop 5 municípios com IDHM acima da média, ordenados:")
print(df_ordenado[['ano', 'sigla_uf', 'expectativa_vida', 'populacao_urbana', 'populacao_rural', 'idhm']].head())

# Encontrando o valor mínimo do IDHM entre os municípios com IDHM acima da média
min_idhm = df_ordenado['idhm'].min()
print("\nValor mínimo do IDHM entre os municípios acima da média:", min_idhm)

# Encontrando o valor máximo do IDHM entre os municípios com IDHM acima da média
max_idhm = df_ordenado['idhm'].max()
print("Valor máximo do IDHM entre os municípios acima da média:", max_idhm)

# Encontrando o índice do município com o menor IDHM entre os municípios com IDHM acima da média
idxmin_idhm = df_ordenado['idhm'].idxmin()
print("Índice do município com menor IDHM entre os municípios acima da média:", idxmin_idhm)

# Encontrando o índice do município com o maior IDHM entre os municípios com IDHM acima da média
idxmax_idhm = df_ordenado['idhm'].idxmax()
print("Índice do município com maior IDHM entre os municípios acima da média:", idxmax_idhm)
