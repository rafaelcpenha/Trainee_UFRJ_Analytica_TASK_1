# 1.4 - Estruturas de dados
#Para esta seção, será necessário conhecer as estruturas de dados list e dict.
#https://www.programiz.com/python-programming/list
#https://www.programiz.com/python-programming/dictionary

# 2 - Crie um dicionário do Python com as seguintes informações do formato chave-valor:
	#Joao - Competicao
	#Carlos - Desenvolvimento
	#Patricia - Competicao
	#Caio - Competicao
	#Leticia - Gestao

	# E em seguida peça ao usuário um nome e imprima qual a equipe a pessoa participa. Se o nome não existir na lista, imprima que o nome não existe.

equipes = {
    'João': 'Competição',
    'Carlos': 'Desenvolvimento',
    'Patricia': 'Competição',
    'Caio': 'Competição',
    'Leticia': 'Gestão'
}

nome = input("Digite um nome para verificar a equipe: ")

if nome in equipes:
    print(f"{nome} participa da equipe de {equipes[nome]}.")
else:
    print(f"{nome} não está na lista de participantes. Lembre-se de que letras maiúsculas são diferenciadas de minúsculas.")