'''
leia o primeiro termo e a razão de uma Progressão aritmetica,
No final,mostre os 10 primeiros termos dessa progressão
'''

print('=='*20)
print('\t\t10 termos de uma PA')
print('=='*20)

primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
décimo = primeiro + (10-1) * razão
for i in range(primeiro,décimo + razão,razão):
    print(i, end=' → ')
print('Fim!')
