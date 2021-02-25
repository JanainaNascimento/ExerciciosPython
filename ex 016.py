'''
#faça um programa que leia um angulo qualquer
e mostre na tela o valor do seno, consseno e tangente desse angulo


import math
angulo = float(input('Digite um angulo: '))

print(f'O angulo de {angulo} tem')

#calcula o valor do angulo e converte de radianos o seno, consseno e tangente
seno = math.sin(math.radians(angulo))
print(f'O seno de : {seno:.2f}')

consseno = math.cos(math.radians(angulo))
print(f'O consseno de : {consseno:.2f}')

tangente = math.tan(math.radians(angulo))
print(f'A tangente de : {tangente:.2f}')


#OUTRO EXEMPLO DE COMO FAZER E ECONOMIZAR MEMÓRIA

from math import radians, sin, tan, cos
angulo = float(input('Digite um angulo: '))

print(f'O angulo de {angulo} tem')

#calcula o valor do angulo e converte de radianos o seno, consseno e tangente
seno = sin(radians(angulo))
print(f'O seno de : {seno:.2f}')

consseno = cos(radians(angulo))
print(f'O consseno de : {consseno:.2f}')

tangente = tan(radians(angulo))
print(f'A tangente de : {tangente:.2f}')

'''