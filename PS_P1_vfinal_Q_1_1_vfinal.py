# Solicita os dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calcula a média dos dois números
media = (numero1 + numero2) / 2

# Formata os números e a média com dois decimais e separadores de milhares
numero1_formatado = "{:,.2f}".format(numero1)
numero2_formatado = "{:,.2f}".format(numero2)
media_formatada = "{:,.2f}".format(media)

# Mostra o resultado na tela
print("A média dos números", numero1_formatado, "e", numero2_formatado, "é:", media_formatada)