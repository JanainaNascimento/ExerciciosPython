'''
Crie uma matriz de 3x3 e preencha com valores lidos do teclado.

mostre ne tela com o formato correto no final:

3x3

[0][1][2]
[3][4][5]
[6][7][8]

'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        
print() 

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()