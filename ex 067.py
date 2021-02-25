'''
mostre a tabuada de varios numeros, um de cada vez,
para cada valor digitado pelo usuario.
o programa sera interrompido quando o numero solicitado for negativo.
'''

num = qtd = 0
i = 1
resp = 'S'

while resp in 'Ss':
    num = int(input('Digite um numero para tabuada: '))
    if num < 1:
        print('Não é aceito números negativos. Programa encerrado!')
        break
    else:
        for i in range(1, 11):
            print(f'{num:^1} X {i:^2} = { num * i}')
        qtd += 1

    resp = str(input('Deseja continuar[S/N]: ')).strip()[0]
print(f'A quantidade de tabuadas lidas foi {qtd}')
print('FIM!')