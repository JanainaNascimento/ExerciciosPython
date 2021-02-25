'''ler duas notas de um aluno e calcular média
mostrando uma mensagem no final, de acordo com a média atingida:

- media abaixo de 5.0:
reprovado

- media entre 5.0 e 6.9:
recuperação

- media 7.0 ou superior:
aprovado
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A média do aluno é {media}')

if media < 5:
    print('Reprovado!')
elif media >=5 and media <7:
    print('Recuperação!')
elif media >=7:
    print('Aprovado!')
