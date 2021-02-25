'''
faça o computador 'pensar' em um número inteiro de 0 a 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

o programa devera escrever na tela se o usuário venceu ou perdeu.

'''

from random import randint
from time import sleep
pc = randint(0,5)

adivinha = int(input('Adivinhe que número o computador escolheu de 0 á 5: '))
print('Processando...')
sleep(2)
if pc == adivinha:
    print(f'Você acertou o número é {adivinha}')
else:
    print(f'Você errou o número era {pc} e não {adivinha}!')