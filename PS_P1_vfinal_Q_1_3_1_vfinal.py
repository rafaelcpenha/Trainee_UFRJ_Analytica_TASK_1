# 1.3 - Estruturas de repetição
	#Para esta seção, será necessário conhecer as estruturas de repetição for e while.
	#https://www.programiz.com/python-programming/for-loop
	#https://www.programiz.com/python-programming/while-loop

# 1 - Faça um programa que recebe um número e imprime cada número de 1 até esse número recebido.

def imprimir_numeros_ate(numero):
    for i in range(1, numero + 1):
        print(i)

numero = int(input("Digite um número: "))
imprimir_numeros_ate(numero)
