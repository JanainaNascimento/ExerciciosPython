'''
ler dois números int e compara-os . mostrando na tela uma mensagem.

o primeiro valor é maior

o segundo valor é maior

não existe valor maior. os dois são iguais.

'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print(f'o primeiro número {n1} é maior que o segundo {n2}!')
elif n2 > n1:
    print(f'O segundo número {n2} é maior que o primeiro {n1}!')
else:
    print('Não existe valor maior os dois são iguais!')
