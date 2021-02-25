'''
faça um programa que leia uma frase pelo teclado e mostre:

quantas vezes aparece a letra "A"

em que posição ela aparece a primeira vez

em que posição ela aparece a última vez
'''

frase = str(input('Digite uma frase: ')).strip().upper()
A = frase.count('A')
pos = (frase.find('A')+1)
ult = (frase.rfind('A')+1)
print(f'A letra A aparece {A} vezes ')
print(f'Ela aparece a primeira vez na posição {pos}').rstrip()
print(f'Ela aparece a ultima vez na posição {ult}')