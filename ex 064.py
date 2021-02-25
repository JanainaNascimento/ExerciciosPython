'''
leia varios numeros inteiros, o programa so para quando o usuario digitar o valor 999
que é a condição de parada, no final, mostre quantos numeros forma digitados
e qual foi a soma entre eles (desconsiderando o flag :999)
'''
qtd = soma = cont = 0
num = int(input('Digite numeros: '))
while num != 999:
    soma += num
    qtd += 1
    num = int(input('Digite numeros: '))

print(f'A quantidade de numeros inserido foi {qtd}')
print(f'A soma entre os valores digitados é {soma}')
