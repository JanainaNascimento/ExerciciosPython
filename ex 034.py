'''
pergunte o salario de um funcionario e calcule o valor do seu aumento.
salarios maiores a 1250 calcule 10% de aumento

para salarios menores ou iguais o aumento é de 15%

'''

salario = float(input('Digite o valor do seu sálario R$: '))
if salario > 1250:
    novosal = salario + (salario * 10/100)
    print(f'O seu sálario de R${salario:.2f} com 10% de aumento fica R${novosal:.2f}!')
if salario <= 1250:
    novosala = salario + (salario * 15/100)
    print(f'O seu sálario de R${salario:.2f} com 15% de aumento fica R${novosala:.2f}!')


#OUTRO EXEMPLO DE COMO FAZER
'''
salario = float(input('Digite o valor di seu sálario R$: '))
if salario <=1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print(f'Seu sálario de R${salario:.2f} com aumento ficou R${novo:.2f}')
'''