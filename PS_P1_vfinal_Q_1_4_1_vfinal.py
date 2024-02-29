# 1.4 - Estruturas de dados
#Para esta seção, será necessário conhecer as estruturas de dados list e dict.
#https://www.programiz.com/python-programming/list
#https://www.programiz.com/python-programming/dictionary

#1 - Faça um programa cuja primeira linha consiste na seguinte lista:
	#competidores = ['Joao', 'Carlos', 'Patricia', 'Caio', 'Leticia']
	#E em seguida peça ao usuário um nome e imprima uma mensagem dizendo se este nome está ou não na lista.

competidores = ['João', 'Carlos', 'Patricia', 'Caio', 'Leticia']
nome = input("Digite um nome para verificar se está na lista de competidores: ")

if nome in competidores:
    print(f"{nome} está na lista de competidores.")
else:
    print(f"{nome} não está na lista de competidores. Lembre-se de que letras maiúsculas são diferenciadas de minúsculas.")
