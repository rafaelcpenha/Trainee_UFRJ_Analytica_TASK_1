# 1.2 Estrturas de controle

#1 Faça um programa que pergunte ao usuário 'qual sua equipe favorita?' e receba o input de uma frase. Seu programa deve responder de acordo com a frase inserida
    # a - Se a frase for ‘UFRJ ANALYTICA’, mostre na tela a frase ‘Minha equipe favorita ´e UFRJ ANALYTICA’.

    # b - Senão, mostre na tela ‘Frase Inesperada’.

def verificar_equipe_favorita():
    frase = input("Qual sua equipe favorita? ")

    if frase == 'UFRJ ANALYTICA':
        print("Minha equipe favorita é UFRJ ANALYTICA")
    else:
        print("Frase Inesperada")

verificar_equipe_favorita()

#--------------------------------------------------------------------------------------------------

#2 Faça um Programa que peça dois números ao usuário e imprima na tela o maior deles ou, caso sejam iguais, imprima ‘Números iguais’.

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