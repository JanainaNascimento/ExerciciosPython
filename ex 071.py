'''
simule o funcionamento de um caixa eletronico. no inicio,
pergunte ao usuario qual sera o valor a ser sacado(num int)
e o programa vai informar quantas cédulas de cada valor serão entregues.
obs: considere que o caixa possiu cedulas de R$50, R$20, R$10 e R$1
'''
print('^' * 20)
print('CAIXA ELETRÔNICO')
print('^' * 20)
valor = int(input('Qual valor a ser sacado?'))
total = valor
céd = 50
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('fim')



