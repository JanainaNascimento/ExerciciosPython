'''
leia varios numeros inteiros pelo teclado, no final
da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valor lido,
o programa deve perguntar ao usuario
se ele quer ou não continuar a digitar valores.
'''
media = soma = qtd = maioe = menor = 0
resp = 'S'

while resp in 'Ss':
    num = int(input('Dgite um número: '))
    qtd += 1
    soma += num

    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
media = soma / qtd
print(f'Você digitou {qtd} números e a média foi {media}')
print(f'O maior valor foi {maior} e menor valor valor foi {menor}')
