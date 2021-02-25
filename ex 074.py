'''
crie um programa que vai gerar cinco numeros aletorios e colocar em uma tupla
depois disso mostre a listagem de numeros
gerados e tambem indique o menor e o maior valor que estao na tupla
'''
from random import randint
pc = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))
print('os valores sortedaos foram: ',end='')
for n in pc:
    print(f'{n}', end=' ')
print('\n')
print(f'o maior valor sorteado foi: {max(pc)}')
print(f'o menor valor sorteado foi: {min(pc)}')
    


