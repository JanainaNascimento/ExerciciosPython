nome = str(input('Digite seu nome;\n'))
a = float(input('Digite sua altura:\n'))
p = float(input('Digite seu peso:\n'))
s = (input('Digite seu sexo (f/m):\n'))

imc = p/(a**2)
if s=="F" or s=="f":
    if imc<20:
        print (f'{nome} Abaixo do peso do sexo {s}')
    elif imc>=20 and imc<=26:
        print (f'{nome} Peso normal do sexo {s}')
else:
    print(f'{nome} Acima do peso do sexo {s}')
if s=="M" or s=="m":
    if imc<20:
        print (f'{nome} Abaixo do peso do sexo {s}')
    elif imc>=20 and imc<=30:
        print (f'{nome} Peso normal do sexo {s}')
else:
    print(f'{nome} Acima do peso do sexo {s}')