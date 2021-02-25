'''
crie um programa que leia o nome completo de uma pessoa e mostre
o nome com todas as letras maiusculas

o nome com todas minusculas

quantas letras ao todo (sem considerar espaços)

quantas letras tem o primeiro nome

'''
nome = str(input('Digite seu nome completo: ')).strip()
maiusculas = nome.upper().strip()
minusculas = nome.lower().strip()
total = (len(nome) - nome.count(' '))
#primeiro = nome.find(' ')
primeiro = nome.split()
print(f'Seu nome é: {nome}\nEm letras maiusculas é: {maiusculas}\n')
print(f'E em minusculas: {minusculas}\n')
print(f'Total de letras: {total}\n')
print(f'O primeiro nome é {primeiro[0]} e tem {len(primeiro[0])} letras')
