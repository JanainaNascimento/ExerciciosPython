'''
programa mega-sena crie palpites. perguntar 
quantos jogos serão gerados e vai sortear 6 numeros
entre 1 e 60 para cada jogo, cadatrando tudo em uma lista composta(lista dentro de outra lista)
'''

from random import randint
from time import sleep
#criando primeira lista
lista = list()
#criando lista onde os jogos vão ser armazenados
jogos = list()
total = 1

print('-' * 30)
print ('      Jogo da Mega Sena      ')
print('-' * 30)
#pergunta a quantidade de jogos que vão ser sorteados
quantos = int(input('Quantos jogos você quer sortear? '))

#se quantos for menor ou igual a total 
while total <= quantos:
    #inicia variavel cont com 0
    cont = 0

    while True:
        # enquanto for verdadeiro sortear de 1 a 60 numeros
        num = randint(1, 60)
        if num not in lista:
            # se mumero sorteado não estiver na lista adicionar na lista
            lista.append(num)
            #adicionar ao contador caso o numero não esteja na lista
            cont += 1
        #se cont for maior ou igual a 6, no caso se cont tiver adicionado os 6 numeros sorteados a lista
        if cont >= 6:
            #então pare de adicionar numerosporque já chegou ao total de 6 valores aleatrorios sorteados
            break
    #organiza os numeros em ordem crescente
    lista.sort()
    #limpa a lista (lista) e joga os valores para a lista jogos 
    jogos.append(lista[:])
    #limpa a lista
    lista.clear()
    #adiciona ao total
    total += 1
#mostra os numeros que foram sorteados, e a quantidade
print('-=' * 3, f'Sorteando {quantos} jogos ', '-=' * 3)


for i, l in enumerate(jogos):
    # 'i' é igual ao indice em relação a quantidade de jogos
    # 'l' é para mostra a lista de numeros de jogos sorteados
    print(f'Jogo: {i+1} {l}')
    sleep(0.5)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
