#PS_P1_vfinal_Q_1_3_v0

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



# 2 - Faça um programa que primeiro pede a quantidade de membros da equipe e, em seguida, para cada membro, pede o seu nome e imprime na tela uma mensagem de boas-vindas 'Olá <nome>, seja bem-vindo!'.

def mensagem_boas_vindas():
    quantidade = int(input("Quantos membros na equipe? "))
    for i in range(quantidade):
        nome = input("Digite o nome do membro: ")
        print(f"Olá {nome}, seja bem-vindo!")

mensagem_boas_vindas()


# 3 - Faça uma calculadora de soma que recebe dois números entre 0 e 9 e mostra sua soma na tela. Verifique se os números de fato estão dentro do intervalo, senão peça para escrever novamente até estar correto.

def calculadora_soma():
    while True:
        num1 = int(input("Digite o primeiro número (entre 0 e 9): "))
        num2 = int(input("Digite o segundo número (entre 0 e 9): "))
        
        if 0 <= num1 <= 9 and 0 <= num2 <= 9:
            break
        else:
            print("Os números devem estar entre 0 e 9. Tente novamente.")

    soma = num1 + num2
    print(f"A soma de {num1} e {num2} é {soma}.")

calculadora_soma()