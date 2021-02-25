'''
Melhore o jogo do Desafio 028 onde o computador vai "Pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar ate acertar
mostrando no final quantos palpites foram necessários para vencer.
'''

# from random import randint
#
# tentativas = 0
# pc = randint(0, 10)
#
# print('O computador pensou um número entre 0 e 10 tente adivinhar')
#
# while True:
#     adivinha = int(input('Digite um número para tentar adivinhar: \n'))
#     tentativas += 1
#     if pc == adivinha:
#         print(f'Usuário adivinhou o número é \033[33m{pc}\033[m, parabéns!')
#         break
#     elif pc != adivinha:
#         print('\033[31mEstá errado, tente outro palpite!\033[m')
# print(f'O usuário fez \033[33m{tentativas}\033[m tentativas até acertar o número que o PC pensou.')


from random import randint
computador = randint(0, 10)
print('Tente adivinha o numero entre 0 e 10 que o pc pensou.')
acertou = False

palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais...')
        else:
            print('menos...')
print(f'acertou com {palpites} tentativas. Parabéns!')



