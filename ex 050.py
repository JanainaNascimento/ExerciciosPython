'''
leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares
se o valor digitado for impar desconsidere-o.
'''
soma = 0
cont = 0
for i in range(1,7,1):
    n = int(input(f'Digite o {i}º numero:'))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você digitou {cont} números pares e a soma deles é: {soma}')