'''
leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
caso esteja errado, peça a digitação novamente
até ter um valor correto o desejado 'M' ou 'F'.
'''

# while True:
#     sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
#     if sexo == 'M' or sexo == 'F':
#         print(f'Dado guardado! {sexo}')
#         break
#     else:
#         print('Dado inválido digite novamente!')
# print('Fim')

#outro exemplo
sexo = str(input('digite seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos.digite seu sexo [F/M]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
