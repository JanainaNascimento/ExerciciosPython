'''
melhore o desafio 061, perguntando para o usuario
se ele quer mostrar mais alguns termos.
o programa encerra quando ele disser que quer mostrar 0 termos.
'''


print('=='*20)
print('\t\t10 termos de uma PA')
print('=='*20)

primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão da PA:'))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end=' → ')

        cont += 1
        termo += razão

    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com o total de {total} mostrados!')