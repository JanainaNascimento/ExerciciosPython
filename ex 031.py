'''
pergunte a distancia de uma viagem em km.
calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km.
e R$0,45 para viagens mais longas.

'''

distancia = float(input('Digite a distância da viagem em Km: '))
if distancia <= 200:
    curta = distancia * 0.50
    print(f'a distância curta total a pagar: {curta:.2f}')
else:
    longa = 0.45 * distancia
    print(f'a distância longa total a pagar {longa:.2f}')

