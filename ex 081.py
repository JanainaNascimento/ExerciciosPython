'''
crie um programa que vai ler vários numeros e colocar em uma lista
depois disso. mostre:
A) quantos numeros foram digitados.
B) a lista de valores ordenada de forma descrescente
C) Se o valor 5 foi digitado e esta ou não na lista

'''

lista = list()
while True:
    lista.append(int(input('Digite um número: ')))

    r = input('Deseja continuar?[S/N] ').lower()
    if r == 'n':
        break
print('^~' * 30)
#len(lista) mostra a qunatidade de números digitados
#semelhante a fazer qtd += 1
print(f'Você digitou {len(lista)} números')
lista.sort(reverse=True)
print(f'Lista de valores em ordem decrescente {lista}')
if 5 in lista:
    print(f'Valor 5 foi digitado!')
else:
    print(f'O valor 5 NÃO foi digitado!')
print('^~' * 30)
