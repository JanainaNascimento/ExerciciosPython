'''
Crie um programa onde o usuário possa digitar vários
valores numericos e cadastre-os em uma lista. 

Caso o número já exista lá dentro. 
ele não será adicionado.No final, serao exibidos todos os valores únicos
digitados, am ordem crescente.
'''
valores = []

while True:
    n = int(input('Digite uma valor: '))

    if n not in valores:
        valores.append(n)
        print(f'Valor adicionado a lista!')
    else:
        print(f' Valor {n} duplicado. Não foi adicionado!')

    r = input('deseja continuar? ').lower()
    if r == 's':
        pass
    else:
        print(f"fim")
        break

valores.sort()
print(f'Valores adicionados na lista {valores}')
