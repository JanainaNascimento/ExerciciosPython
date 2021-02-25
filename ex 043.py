'''
ler peso e a altura de uma pessoa . calcule
seu imc e mostre seu status, de acordo com a tabela abaixo:

abaixo de 18.5 - abaixo do peso

entre 18.5 e 25 - peso ideal

25 até 30  - sobrepeso

30 até 40 - obesidade

acima de 40 - obesidade morbida

'''
peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
print('\n')
imc = peso/(altura**2)
print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc <25 :#if imc 18.5 <= imc < 25:
    print('Peso normal.')
elif imc >= 25 and imc < 30:#if imc 25 <= imc < 30:
    print('Sobrepeso.')
elif imc >= 30 and imc <40:#if imc 30 <= imc < 40:
    print('Obesidade.')
elif imc >=40:
    print('Obesidade morbida')


print(20*'--')
titulo = 'TABELA DE PESO'
print(f'''{titulo:^30}
Abaixo de 18.5 - ABAIXO DO PESO
Entre 18.5 e 25 - PESO NORMAL
Entre 25 até 30  - SOBREPESO
Entre 30 até 40 - OBESIDADE
Acima de 40 - OBESIDADE MÓRBIDA''')