'''
calcule o valor a ser pago por um produto.
considerando o seu preço normal e condição de pagamento:

a vista dinheiro/cheque - 10% de desconto

a vista no cartão - 5% de desconto

em até 2x no cartao - preco normal

3x no cartao - 20% de juros

'''
nome = 'LOJAS JANAÍNA'
print(f'{nome:=^40}')
valorproduto = float(input('Digite o valor do produto R$: '))
print('''SELECIONE A FORMA DE PAGAMNETO:
[ 1 ] Á vista Dinheiro/Cheque - 10% de Desconto
[ 2 ] Á vista no cartão - 5% de Desconto
[ 3 ] Em até 2x no cartão - Sem juros
[ 4 ] 3x no cartão ou mais - 20% de Juros ''')
opção = int(input('Escolha uma opção de pagamento:'))

if opção == 1:
    dinheirocheque = valorproduto - (valorproduto * 10 / 100)  # 10% de desconto
    print(f'O valor do produto é R${valorproduto:.2f} e você escolheu pagar á vista Dinheiro/Cheque\nteve 10% de desconto', end=' ')
    print(f'e pagará R${dinheirocheque:.2f} pelo produto!')
elif opção == 2:
    avistacartao = valorproduto - (valorproduto * 5 / 100)  # 5% de desconto
    print(f'O valor do produto é R${valorproduto:.2f} e você escolheu pagar á vista no cartão\nteve 5% de desconto', end=' ')
    print(f'e pagará R${avistacartao:.2f} pelo produto!')
elif opção == 3:
    total = valorproduto
    parcela = total /2
    print(f'O valor do produto é R${valorproduto:.2f} e você escolheu pagar em até 2X no cartão\npagará o valor Sem Juros', end=' ')
    print(f'em 2X o valor da parcela será R${parcela:.2f}\ne o valor total R${valorproduto:.2f}')
elif opção == 4:
    total = valorproduto + (valorproduto * 20/100)
    totalparcelas = int(input('Deseja pagar em quantas vezes no cartão?'))
    parcelas = total / totalparcelas
    print(f'O valor do produto é R${valorproduto:.2f} e você escolheu pagar', end=' ')
    print(f'em \n{totalparcelas}X no cartão e pagará parcelas de R${parcelas:.2f} terá 20% de juros')
    print(f'O total será de R${total:.2f}')

