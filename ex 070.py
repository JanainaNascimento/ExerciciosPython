'''
leia o nome e o preço de varios produtos.
o programa devera perguntar se o usuario vai continuar.
no final mostre:
-qual é o total gasto na compra
-quantos produtos custam mais de R$1000
-qual é o nome do produto mais barato
'''

custa = total = soma = qtdmil = menor = cont = 0
barato = ''


while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    cont += 1
    total += preço

    if preço > 1000:
        qtdmil += 1

    if cont == 1 or preço < menor:
        menor = preço
        barato = produto


    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar [S/N]?').strip().upper()[0]
    if resp == 'N':
        break

#total gasto na compra
print(f'Total gasto na compra R$ {total:.2f}')
print(f'A quantidade de produtos que custa mais de R$ 1000 é {qtdmil}')
print(f'O produto mais barato é {barato} e o menor preço {menor}')
