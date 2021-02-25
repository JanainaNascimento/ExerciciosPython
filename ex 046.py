'''
mostre na tela uma contagem regressiva para o estouro de fogos de artificios,
indo de 10 até 0
com uma pausa de 1 segundo entre elas.
'''
from time import sleep

for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('\033[31mBUM! BUM! POW! \033[m')


'''
#exemplo do for

i = int(input('Inicio:'))
f = int(input('Fim:'))
p = int(input('Passo:'))

for c in range(i, f+1, p):
    print(c)
print('fim!')
'''