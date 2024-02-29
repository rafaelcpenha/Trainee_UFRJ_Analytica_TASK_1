# 1.3 - Estruturas de repetição
	#Para esta seção, será necessário conhecer as estruturas de repetição for e while.
	#https://www.programiz.com/python-programming/for-loop
	#https://www.programiz.com/python-programming/while-loop


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