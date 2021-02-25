'''
ler um número inteiro e
mostrar na tela se ele é PAR ou Impar.

'''

num = int(input('Digite um número: '))

if (num / 2) % 1:
    print('IMPAR')
else:
    print('PAR')

'''
OUTRO EXEMPLO DE COMO FAZER:

num = int(input('Digite um número: '))
resultado = num % 2
if resultado == 0:
    print('par')
else:
    print('impar')
    
'''