'''
calcule a soma entre todos os numeros impares que são multiplos de tres
e que se encontre no intervalo de 1 ate 500.
'''
soma = 0
conta = 0
for n in range(1,501,2):
    if n % 3 == 0:
        soma += n #soma = soma + n
        conta += 1 #conta = conta + 1
print(f'A soma de todos {conta} valores impares que são multiplos de 3 é: {soma}')
