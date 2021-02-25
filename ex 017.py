'''
um prof quer sortear um dos seus quatro alunos para apagar o quadro.
lendo nome deles e escrevendo o nome do escolhido


import random
print('* Sorteia um dos quatro alunos para apagar a lousa*\n')
n1 = input('Primeiro nome: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
sorteio = random.choice(lista)
print(f' O escolhido foi, {sorteio}')


# exemplo deixando somente uma biblioteca
from random import choice # Retorna um elemento aleatório da sequência não vazia
print('* Sorteia um dos quatro alunos para apagar a lousa*\n')
n1 = input('Primeiro nome: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
sorteio = choice(lista)
print(f'O aluno escolhido foi, {sorteio}')


from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundoa aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista) #shuffle embaralha a lista
print(f'A ordem das apresentações são {lista}')


from random import randint
numeros = randint(1,10)#pega um numero inteiro aleatório
print(numeros)

import random
num = random.random() #retorna um numero aletório de ponto flutuante entre esse intervalo 0.0, 1.0
print(num)

'''


'''
Retorna um número de ponto flutuante aleatório 
N de forma que a <= N <= b para a <= b e b <= N <= a para b < a.
O valor do ponto final b pode ou não ser incluído no intervalo,
dependendo do arredondamento do ponto flutuante na equação a + (b-a) * random().


import random
a = 2
b = 10
num = random.uniform(a, b)
print(num)
'''

import random
a = 2
b = 10
num = random.uniform(a, b)
print(num)
