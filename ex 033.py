'''
ler tres números e
mostre qual é o maior e qual é o menor número.

'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

#verifica qual é o menor número
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#verifica qual é o maior número
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3


#verificar os dois numeros maiores digitados
maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3



print(f'O maior número digitado é: {maior} ')
print(f'O menor número digitado é: {menor}')



