'''
crie um progrma que vai ler varios numeros e colocar em uma lista

depois disso, crie duas listas extras
que vão conter apenas os valores pares
e os valores impares digitados
respectivamente.

ao final, mostre o conetudo das tres lista geradas

'''

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um valor: ')))



    r = input('deseja continuar?[S/N] ').lower()
    if r == 'n':
        break
print('-=' * 30)
print(f'Valores adicionados á lista {lista}')
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Números pares dessa lista {pares}')
print(f'Números ímpares dessa lista {impares}')
print('-=' * 30)
