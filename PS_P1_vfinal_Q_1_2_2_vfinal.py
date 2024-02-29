# 1.2

#Comparação de Números

# 2 - Faça um Programa que peça dois números ao usuário e imprima na tela o maior deles ou, caso sejam iguais, imprima ‘Números iguais’.

def comparar_numeros():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    # Formatar os números com dois decimais e separadores de milhares
    numero1_formatado = "{:,.2f}".format(numero1)
    numero2_formatado = "{:,.2f}".format(numero2)

    if numero1 > numero2:
        print("O maior número é:", numero1_formatado)
    elif numero2 > numero1:
        print("O maior número é:", numero2_formatado)
    else:
        print("Números iguais")

comparar_numeros()