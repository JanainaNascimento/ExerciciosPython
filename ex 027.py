n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
m = (n1+n2)/2
#print('Parabéns' if m >=6.0 else 'estude mais') #condição simplificada
print(f'Sua média é de : {m}')
if m >= 6.0:
    print('Sua média foi boa!')
else:
    print('Sua média foi ruim!')
