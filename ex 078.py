''' 
Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
'''
# v = 0
# valores = []
# for v in range(1, 6):
#     valores.append(int(input(f'Digite o {v}º número: ')))

# maior = max(valores)
# menor = min(valores)
# print(f'Você digitou estes valores{valores}')
# print(f'Maior valor digitado foi: {maior} na posição {valores.index(maior)+1}º')
# print(f'Menor valor digitado foi: {menor} na posição {valores.index(menor)+1}º')

vale = []
maior = 0
menor = 0

for c in range(0, 5):
    vale.append(int(input('Digite um valor: ')))

    if c == 0:
        maior = menor = vale[c]
    else:
        if vale[c] > maior:
            maior = vale[c]  
        elif vale[c] < menor:
            menor = vale[c]
print('\n')
print(f'Valores digitados {vale}')

print(f'O maior valor digitado foi {maior} na posição', end=' ')
for i, v in enumerate(vale):
    if v == maior:
        print(f'{i+1}º', end=' ')
print('\n')
print(f'O menor valor digitado foi {menor} na posição', end=' ')
for c, vl in enumerate(vale):
    if vl == menor:
        print(f'{c+1}º', end=' ')
print('\n')
