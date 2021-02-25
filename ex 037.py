'''
escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual sera a base de conversão;
1 para binario
2 para octal
3 para hexadecimal

'''
while True:
      num = int(input('Digite um número inteiro: '))
      print('''Escolha em qual base você quer fazer a conversão:'
1- BINÁRIO
2- OCTAL
3- HEXADECIMAL''')
      opção = int(input('Digite o número correspondente: '))

      if opção == 1:
            print(f'O decimal {num} convertido para Binário é igual a {bin(num)[2:]}')
      elif opção == 2:
            print(f'O decimal {num} convertido para Octal é igual a {oct(num)[2:]}')
      elif opção == 3:
            print(f'O decimal {num} convertido para Hexadecimal é igual a {hex(num)[2:]}')
      else:
            print('Valor inválido. Tente Novamente!')

      resp = input('Deseja repetir [S/N] ').upper()
      if resp == 'NÃO' or resp == 'NAO' or resp == 'N':
            print('Fim!')
            break



