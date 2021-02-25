'''
leia o ano de nascimento de 7 pessoas,
no final mostre quantas pessoas ainda não atigiram a maioridade
e quantas ja são maiores

ex: 21 anos
'''
from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0

for i in range(1,8):
    nasc = int(input(f'Em que ano a {i}º pessoa nasceu: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade.')
print(f'E também tivemos {totmenor} pessoas menores de idade.')