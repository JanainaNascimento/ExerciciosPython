'''
refaça ex 12, mostrando a tabuada de um numero que o usuario escolher
so que agora utilizando um laço for.
'''

n = int(input('Digite um número:'))#solicita um numero ao usuario
for i in range(1,11):# faz do 1 ao 10, não conta o 11
    print(f'{n}x{i}={n*i}')#calculo da tabuada com iteração de 1