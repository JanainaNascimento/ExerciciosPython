'''
jogue par ou impar com o computador.
o jogo so sera interrompido quando o jogador Perder,
mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
'''

from random import randint

vitoria = 0
ops = ''

while True:
    print('~' * 21)
    print('JOGO DO PAR OU IMPAR')
    print('~' * 21)
    num = int(input('Digite um numero: '))  # usuario entra com um valor
    pc = randint(0, 10)
    soma = num + pc
    escolha = ' '
    while escolha not in 'PI':#enquanto acertou for verdadeiro
        escolha = str(input('Par ou impar?[P/I]')).upper().strip()[0]#usuario diz se vai ser par ou impar

    if soma % 2 == 0:
        print('-' * 60)
        print(f'Usuário digitou {num} e PC {pc} e a soma é {soma} portanto é PAR!')
        print('-' * 60)
    else:
        print('-' * 60)
        print(f'Usuário digitou {num} e PC {pc} e a soma é {soma} portanto é IMPAR!')
        print('-' * 60)
    if escolha == 'P':
        if soma % 2 == 0:
            ops = 'Par'
            print('\033[32mVocê VENCEU!\033[m')
            vitoria += 1
        else:
            print('\033[31mVocê PERDEU!\033[m')
            ops = 'Impar'
            break

    elif escolha == 'I':
        if soma % 2 == 1:
            ops = 'Impar'
            print('\033[32mVocê VENCEU!\033[m')
            vitoria += 1
        else:
            print('\033[31mVocê PERDEU!\033[m')
            ops = 'Par'
            break



    print('\033[35mVamos jogar novamente...\033[m')
print(f'Sua quantidade de vitória foi {vitoria} vezes!')
