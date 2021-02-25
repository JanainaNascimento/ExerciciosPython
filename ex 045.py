'''
faça o computador jogar jokenpô com voce.
pedra, papel, tesoura.
'''

from random import choice
from time import sleep
pca = ['pedra','papel','tesoura']
pc = choice(pca)
usuario = str(input('Digite uma dessas opções: Pedra, Papel ou Tesoura?')).strip()
print('\033[31mJO \033[m')
sleep(1)
print('\033[32mKEN \033[m')
sleep(1)
print('\033[33mPÔ! \033[m')
print('\033[34m',7*'-*-*-*-*-','\033[m')
if pc == usuario or usuario == pc:
    print(f'Pc escolheu \033[4:35m{pc}\33[m e Usuário escolheu \033[4:33m{usuario}\33[m \033[7mhouve um Empate!\033[m')
elif pc == 'pedra' and usuario == 'papel':
    print(f'Pc escolheu \033[4:35m{pc}\33[m e Usuário \033[4:33m{usuario}\33[m \033[1:34mPC Venceu!\33[m')
elif pc == 'papel' and usuario == 'tesoura':
    print(f'Pc escolheu \033[4:35m{pc}\33[m e Usuário \033[4:33m{usuario}\33[m \033[1:34mPC Venceu!\33[m')
elif pc == 'tesoura' and usuario == 'pedra':
    print(f'Pc escolheu \033[4:35m{pc}\33[m e Usuário \033[4:33m{usuario}\33[m \033[1:34mPC Venceu!\33[m')
else:
    print(f'Pc escolheu \033[4:35m{pc}\33[m e Usuário \033[4:33m{usuario}\33[m \033[1:31mPC Venceu!\33[m')