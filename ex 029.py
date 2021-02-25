'''
ler a velocidade de um carro. se ele ultrapassar 80km/h,
mostre uma mensagem dizendo que ele foi multado.

a multa vai custar R$7,00 por cada Km acima do limite.

'''

velocidade = float(input('Digite a velocidade que o carro estava: '))
k = velocidade * 1000
max = 80 * 1000
if k > max:
    print('Ultrapassou o limite de velocidade permitido de 80Km!')
    multa = (velocidade - 80) * 7
    print(f'Você foi multado! total a pagar: R${multa:.2f}')
else:
    print('Você não foi multado!')