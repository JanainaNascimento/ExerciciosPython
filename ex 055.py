'''
leia o peso de cinco pessoas, no final mostre
qual foi a maior e o menor peso lidos.
'''

maior = 0
menor = 0

for i in range(1,6):
    peso = float(input(f'Digite o peso da {i} pessoa:'))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'A quantidade de pessoas com maior peso foi de {maior}Kg')
print(f'E a quantidade de pesssoas com menor peso foi de {menor}Kg')
