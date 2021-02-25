'''
leia uma frase qualquer e diga se ela é um palidromo.
desconsiderando os espaços.

ex:
apos a sopa
a sacada da casa
a torre da derrota
'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = '' # sem usar o for → 'inverso = junto[::-1]' fatiamento
for letras in range(len(junto)-1,-1,-1):#usando o for
    inverso += junto[letras]#com for
print('O inverso de \033[32m',junto,'\033[m','é','\033[32m', inverso, '\033[m')
if inverso == junto:
    print('É um \033[33mpalíndromo!')
else:
    print('A frase não é um \033[31mpalíndromo!')


