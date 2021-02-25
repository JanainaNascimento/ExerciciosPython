'''
ler o comprimento de tres retas e diga ao usuario
se eles podem ou não formar um triangulo


é um triângulo se a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois
e maior que o valor absoluto da diferença entre essas medidas.

'''
print('-*-' * 24)
print('PROGRAMA QUE DIZ SE OS TRÊS VALORES DIGITADOS PODEM FORMAR UM TRIÂNGULO!')
print('-*-' * 24)
r1 = float(input('Primeiro comprimento: '))
r2 = float(input('Segundo comprimento: '))
r3 = float(input('Terceiro comprimento: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
        print('\033[7mPode se formar um triângulo! \033[m')
else:
    print('Não se pode formar um triângulo!')


# (abre) \033 e \033[m (fecha) cores no terminal