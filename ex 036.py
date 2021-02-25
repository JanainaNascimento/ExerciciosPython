'''
escreva um programa para aprovar um emprestimo bancario para a compra de uma casa .
pergunte o valor da casa , o salario do comprador e em quantos anos ele vai pagar
a prestação mensal , não pode execeder 30% do salario ou entao o emprestimo sera negado
'''

valorcasa = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite seu salário R$: '))
anos = int(input('Em quantos anos pretende pagar?: '))

prestação = valorcasa / (anos * 12)
minimopago = salario * 30/100

print(f'Para pagar uma casa de R${valorcasa:.2f} em {anos} anos a prestação sera de R${prestação:.2f}')
if prestação <= minimopago:
    print('O empréstimo foi ACEITO!')
else:
    print('O empréstimo foi NEGADO!')

