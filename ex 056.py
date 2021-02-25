'''
leia o nome, idade e sexo de 4 pessoas,
no final do programa mostre:
ex:
-a média de idade do grupo
-o nome do homem mais velho
-quantas mulheres tem menos de 20 anos
'''
somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
totmulher = 0
for i in range(1, 2):
    print(f'---------- {i}º PESSOA ----------')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [F/M]: ')).strip()
    print()

    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totmulher += 1

mediaidade = somaidade / 4

print(f'A média de idade do grupo é de \033[4:35m{mediaidade:.0f} anos\033[m')
print(f'O homem mais velho tem \033[4:33m{maioridadeh} anos\033[m e chama-se \033[4:33m{nomevelho}\033[m')
print(f'Ao todo temos \033[4:32m{totmulher}\033[m mulheres com menos de 20 anos')
