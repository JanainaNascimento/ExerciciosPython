'''
ler um numero inteiro e diga se ele é ou não um numero primo
'''
total = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m', end=' ')
        total += 1
    else:
        print('\033[32m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {n} foi divisível {total} vezes ')
if total == 2:
    print('E portanto ele é um número \033[32mPRIMO!')
else:
    print('E portanto ele \033[31mNÃO É PRIMO!')
