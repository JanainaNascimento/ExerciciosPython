'''
leia idade e sexo de varias pessoas a cada pessoa cadastrada,
o programa devera perguntar se o usuario quer ou nao continuar. no final mostre:
-quantas pessoas tem mais de 18 anos ambos sexos
-quantos homens foram cadastrados
-quantas mulheres tem menos de 20 anos
'''
ida = sexhm = sexmu = 0
while True:
    print(':' * 20)
    print('Cadastro de pessoas')
    print(':' * 20)
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]

    if sexo in 'M':
        sexhm += 1

    if sexo in 'F' and idade < 20:
        sexmu += 1

    if idade > 18:
        ida += 1

    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break

print(f'A quantidade de pessoas com mais de 18 anos é {ida}')
print(f'E {sexhm} homens foram cadastrados')
print(f'E {sexmu} mulheres tem menos de 20 anos')
