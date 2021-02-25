'''faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um trian retangulo,
calc e mostre o comp da hipotenusa

print('*Calcula a Hipotenusa de um triângulo retangulo*')
catOpo = float(input('Digite o cateto oposto: '))
catAdj = float(input('Digite o cateto adjacente: '))
hi = (catAdj ** 2 + catOpo ** 2) ** (1/2)
print(f'O comprimento da Hipotenusa é {hi:.3f}')


from math import pow
catOpo = float(input('Digite o cateto oposto: '))
catAdj = float(input('Digite o cateto adjacente: '))
hi = pow(pow(catAdj, 2) + (pow(catOpo, 2)), 1/2)
print(f'O comprimento da Hipotenusa é {hi:.3f}')


#calcular hipotenusa com biblioteca math
import math
catOpo = float(input('Digite o cateto oposto: '))
catAdj = float(input('Digite o cateto adjacente: '))
hi = math.hypot(catAdj, catOpo)
print(f'O comprimento da Hipotenusa é {hi:.3f}')

from math import hypot
catOpo = float(input('Digite o cateto oposto: '))
catAdj = float(input('Digite o cateto adjacente: '))
hi = hypot(catAdj, catOpo)
print(f'O comprimento da Hipotenusa é {hi:.3f}')
'''