'''
crie um programa onde o usuario possa digitar sete valores numéricos e
cadastre-os em uma lista unica que mantenha separados os valores pares e impares.
no final, mostre os valores pares e impares em ordem crescente

'''
#lista composta
num = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i}º valor: '))

    #verfica se o valor 0 na lista composta é par ou impar
    if valor  % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print()
print(f'Valores PARES adcionados a lista {num[0]}') 
print(f'Valores IMPARES adicionados a lista {num[1]}')
   