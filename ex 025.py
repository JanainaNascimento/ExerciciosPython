'''
crie um programa que leia o nome completo de uma pessoa e
diga se ela tem ou não o "SILVA" no nome
'''

nome = str(input('Digite o seu nome completo: ')).upper().strip()
print('Seu nome tem Silva?','SILVA' in nome)