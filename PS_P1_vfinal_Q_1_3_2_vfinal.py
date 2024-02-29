# 1.3 - Estruturas de repetição
	#Para esta seção, será necessário conhecer as estruturas de repetição for e while.
	#https://www.programiz.com/python-programming/for-loop
	#https://www.programiz.com/python-programming/while-loop


# 2 - Faça um programa que primeiro pede a quantidade de membros da equipe e, em seguida, para cada membro, pede o seu nome e imprime na tela uma mensagem de boas-vindas 'Olá <nome>, seja bem-vindo!'.

def mensagem_boas_vindas():
    quantidade = int(input("Quantos membros na equipe? "))
    for i in range(quantidade):
        nome = input("Digite o nome do membro: ")
        print(f"Olá {nome}, seja bem-vindo!")

mensagem_boas_vindas()