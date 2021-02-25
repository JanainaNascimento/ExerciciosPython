'''
crie um programa que leia nome e peso de varias pessoas.
guardando tudo em uma lista. No final, mostre:

A) quantas pessoas foram cadastradas.

B)uma lsitagem com as pessoas mais pesadas.

C) uma listagem com as pessoas mais leves.

'''
temp = []
princ = []

men = mai = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()

    r = input('Continuar?[S/N]')
    if r in 'Nn':
        break

print(f'Quantidade de pessoas cadastradas são {len(princ)} ')
print(f'O peso das pessoas mais pesadas é {mai} Kg Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O peso das pessoas mais leves é {men} Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
