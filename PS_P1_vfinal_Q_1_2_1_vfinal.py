# 1.2

# 1 - Estruturas de Controle

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
