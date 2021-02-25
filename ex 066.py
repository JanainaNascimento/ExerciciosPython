'''
leia varios numeros inteiros pelo teclado. o programa so para quando
o usuario digitar o valor 999, que é a condição de parada.
no final mostre quantos numeros foram digitados e qual foi a soma entre eles
(desconsidere o flag)
'''

qtd = soma = 0
while True:
    num = int(input('Digite um valor (p/ parar \033[4m999\033[m): '))
    if num != 999:
        qtd += 1
        soma += num
    else:
        break
print(f'A soma dos {qtd} valores digitados foi {soma}!')
