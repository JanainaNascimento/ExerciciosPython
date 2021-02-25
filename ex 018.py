'''
sortear a ordem de apresentação de trabalhos dos alunos.
leia nome dos 4 aluno e mostre a ordem sorteada


from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundoa aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem das apresentações são {lista}')'''


