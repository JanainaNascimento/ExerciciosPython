'''
leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

seu programa devera realizar a operação solicitada em cada caso.
'''

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0

while escolha != 5:
    print('---'*20)
    print('''    [1] somar
    [2] multiplicar
    [3] maior número
    [4] novos números
    [5] sair do programa
        ''')

    escolha = int(input('Digite um das opções: '))

    if escolha == 1:
        #somar
        s = n1 + n2
        print(f'A soma de {n1} + {n2} é igual a {s}')

    elif escolha == 2:
        m = n1 * n2
        print(f'A multiplicação de {n1} X {n2} é igual a {m}')

    elif escolha == 3:
        maior = n1
        if n2 > n1:
            maior = n2
            print(f'entre {n2} e {n1} o maior valor é {maior}')
        else:
            print(f'entre {n2} e {n1} não exite valor maior')
    elif escolha == 4:
        print('Informe os números novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida. tente novamente!')

sleep(1)
print('Fim.')










