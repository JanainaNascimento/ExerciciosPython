'''
refaça o desafio 051, lendo o primeiro termo e a razão
de uma PA, mostrando os 10 primeiros termos da progressão usando
a estrutura while.

'''

print('=='*20)
print('\t\t10 termos de uma PA')
print('=='*20)

primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão da PA:'))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo}',end=' → ')
    cont += 1
    termo += razão
print('Fim!')