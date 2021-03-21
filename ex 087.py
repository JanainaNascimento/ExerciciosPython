'''
aprimorar o desafio anterior, mostrando
no final:

A) a soma de todos os valores pares digitados

B) a soma dos valores da terceira coluna.

C) o maior valor da segunda linha.
'''


#gerar estrutura da matriz
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
somapares = maiorvalor = somadacoluna = 0
#criando a matriz, preenche matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a matriz [{l}, {c}]: '))

#espaço
print()
print('*' * 30)
#mostrar a matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        #se matriz elementos digitados forem pares 
        if matriz[l][c] % 2 == 0:
            #soma recebe valor da matriz soma cada valor par adicionado
            somapares += matriz[l][c]
    print()#espaço
print('*' * 30)
print(f'A soma dos valores pares é {somapares}')

#valor da coluna varia
#linha fixa
for l in range(0, 3):
    #valor da coluna é fixo 
    #soma todos os valores da terceira coluna
    somadacoluna += matriz[l][2]

print(f'A soma dos valores da terceira coluna é {somadacoluna}')

#maior valor da segunda coluna
#coluna fixa
for c in range(0, 3):
#se a coluna 1 for igual a zero ou maior que o calor da matriz
    if c == 0 or matriz[1][c] > maiorvalor:
#então maiorvalor recebe o valor da matriz que for maior
        maiorvalor = matriz[1][c]

print(f'O maior valor da segunda linha é {maiorvalor}')