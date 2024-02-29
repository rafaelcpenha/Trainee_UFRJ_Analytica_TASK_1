# 1.5 - Funções e modularização/reaproveitamento de código

#Para esta seção, será necessário conhecer funções e seus argumentos.
	#https://www.programiz.com/python-programming/function
	#https://www.programiz.com/python-programming/function-argument

# 1 - Crie uma função que recebe um número n e imprime na mesma linha, com espaços, n vezes o valor.
	#Input: 5
	#Output: 5 5 5 5 5

# 2 - Faça um programa que receba um número n e imprima em cada linha k vezes o número relativo à linha, usando a função criada na questão anterior para fazer a impressão das linhas:
	#Input: 5
	#Output:
	#1
	#2 2
	#3 3 3
	#4 4 4 4
	#5 5 5 5 5


# Função para imprimir um número n vezes na mesma linha
def imprimir_n_vezes(n):
    print(*[n] * n, sep=" ")

# Programa para imprimir números de 1 a n repetidos k vezes em cada linha
def imprimir_linhas_repetidas(n):
    for i in range(1, n + 1):
        imprimir_n_vezes(i)

# Testando as funções com os inputs fornecidos
if __name__ == "__main__":
    n = int(input("Digite um número: "))

    print("Output 1:")
    imprimir_n_vezes(n)

    print("\nOutput 2:")
    imprimir_linhas_repetidas(n)