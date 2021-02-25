'''
desenvolva um progrma que leia quatro valores pelo teclado e guarde-os
em uma tupla. no final mostre:
a) quantos vezes aparece o valor 9.
b) em que posição foi digitado o primeiro valor 3.
c) quais foram os numeros pares

'''
tupla = (int(input(f'Digite o 1º valor: ')),
        int(input(f'Digite o 2º valor: ')),
        int(input(f'Digite o 3º valor: ')),
        int(input(f'Digite o 4º valor: ')))


print(f'O valor 9 foi digitado {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 foi digitado na posição {tupla.index(3)+1}')
else:
    print(f'o valor 3 não foi digitado em nenhuma posição!')

print(f'O total de valores pares são ', end='')
for n in tupla:
    if n %2 == 0:
        print(n, end=' ')
