'''
n1 = int(input('Digite um número:\n'))
print(f'O sucessor de é {n1+1} e o antecessor é {n1-1}')


n1 = int(input('Digite um número: \n'))
print(f'O dobro de {n1} é {n1*2:.2f}\ne o triplo é {n1*3:.2f} \n', end= '')
print(f'e raiz quadrada é {pow(n1,(1/2)):.2f}')
#fazer potencia base**(expoente) e pow(base,(expoente))

n1 = float(input('Digite a primeira nota: \n'))
n2 = float(input('Digite a segunda nota: \n'))
m = (n1+n2)/2
print(f'A média do aluno é {m:.1f}')


m = float(input('Digite um valor em metros:\n'))
c = m*100
mm = m*1000
km =m /1000
hm = m / 100
dm = m * 10
dam = m /10
print(f'O valor de {m:.1f}m\n ', end='')
print(f'{c:.2f} cm\n{mm:.2f} mm')
print(f'{km} Km')
print(f'{hm} hm')
print(f'{dm} dm')
print(f'{dam} dam')




#Tabuada
n = int(input('Digite um número:'))
for i in range(1,11):
    print(f'{n}x{i}={n*i}')


#reais para dolares
dinheiro = float(input('Quanto você tem na carteira?  R$'))
dólar = dinheiro/5.62
print(f'Com esse valor R${dinheiro:.2f} você pode comprar este valor em dólares ${dólar:.2f}')

#dolares para reais
d = float(input('Digite um valor em dolares? $'))
reais = d * 5.62
print(f'com esse valor ${d:.2f} você pode compra esse valor em reais R${reais:.2f}')



l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = a*l
print(f'A sua parede tem a dimensão de {l}x{a} e sua area é de {area:.2f}m²')
tinta= area/2
print(f'A quantidade necessária de tinta para pintar a parede é {tinta}l de tinta')


#desconto de 5%
p = float(input('Digite o valor do produto R$:\n'))
n = p - (p * 5/100)
print(f'O valor do produto com desconto de 5% é de R${n:.2f}')
#acrescimo de 15%


#aumento 15%
salario = float(input('Digite o valor do seu atual salário :R$'))
novoSal = salario + (salario*15/100)
print(f'Seu salário de R${salario} com 15% de aumento ficou sendo R${novoSal}')


c = float(input('Digite uma temperatura em graus ºC: '))
f = c * 1.8 + 32
print(f'A temperatura em graus fahrenheit é °F{f:.1f}')


km = float(input('Digite quantos km foram rodados: '))
dias = int(input('Por quantos dias foi alugado ?'))
preco = (dias * 60)+(0.15 * km)
print(f'A quantidade a pagar por {dias} dias e {km:.2f} km rodados é: R${preco:.2f}')

'''