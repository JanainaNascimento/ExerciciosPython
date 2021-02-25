'''
a confederação brasileira de natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua
categoria de acordo com a idade:

ate 9 anos - mirim
ate 14 anos - infantil
ate 19 anos - junior
ate 25 anos - senior
acima- master
'''

from datetime import date
print(95*'-')
print('Programa da Confederação Brasileira de Natação classificação do nadador de acordo com a idade.')
print(95*'-')
nascimento = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento

print(f'O atleta tem {idade} anos!')

if idade <= 9:
    print('Classificação: Mirim.')
elif idade <= 14:
    print('Classificação: Infantil.')
elif idade <= 19:
    print('Classificação: Júnior.')
elif idade <= 25:
    print('Classificação: Sênior.')
else:
    print('Classificação: Master.')