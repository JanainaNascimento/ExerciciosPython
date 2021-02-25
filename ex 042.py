'''
refaça o ex 35 dos triangulos. acresecentando
que tipo de triangulo sera formado

equilatero - todos os lados iguais

isoceles - dois lados iguais

escaleno - todos os lados diferentes

'''

print('-*-' * 24)
print('PROGRAMA QUE DIZ SE OS TRÊS VALORES DIGITADOS PODEM FORMAR UM TRIÂNGULO!')
print('-*-' * 24)
r1 = float(input('Primeiro comprimento: '))
r2 = float(input('Segundo comprimento: '))
r3 = float(input('Terceiro comprimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[7mPode se formar um triângulo! \033[m')
    if r1 == r2 and r2 == r3 and r3 == r1:#if r1 == r2 == r3: *também pode ser feito assim que funciona
            print('Equilátero!')
    elif r1!= r2 and r2!= r3 and r3!= r1:#r1 != r2 != r3 != r1: *também pode ser feito assim que funciona
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Estes comprimentos não podem formar um triângulo!')

