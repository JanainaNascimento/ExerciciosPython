'''
uma tupla unica com nomes de produtos e seus respectivos preços na sequencia.
no final, mostre uma listagem de preços, organizado os dados em forma tabular.

mostrar
ex:
bala.............R$ 5.50
'''

produtos = ('bala',0.10,
            'bombom',1.00,
            'chocolate',7.00,
            'pirulito',0.30,
            'chiclete',0.50)

print('-' * 40)            
print(f'{"Listagem de preços":^40}')
print('-' * 40)   

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end = '')
    else:
        print(f'R${produtos[pos]:>5.2f}')
print('-' * 40)   