'''
leia um número qualquer e mostre o seu fatorial.

ex: 5! = 5x4x3x2x1=120
'''

num = int(input('Digite um valor para calcular o fatorial: '))
cont = num #cont recebe num
f = 1 #inicia a variavel
print(f'Calculando fatorial de {num}! = ', end='')
while cont > 0:#enquanto contador for maior que 0 realiza o laço
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')#if simplificado
    # if cont > 1:
    #     print(' x ', end='')
    # else:
    #     print('  ', end='')
    f *= cont #multiplica fatorial pelo contador até 1
    cont -= 1 # vai diminuindo de um em um ate chegar a 0
print(f'{f}')#resultado


# com módulo
# from math import factorial
# num = int(input('Digite um valor para calcular o fatorial: '))
# f = factorial(num)
# print(f'O fatorial de {num} é {f}')
