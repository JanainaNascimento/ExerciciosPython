'''
ler o ano de nascimento de um jovem e informe, de acordo com sua idade:

-se ele ainda vai se alistar ao serviço militar.
-se é a hora de se alistar.
-se já passou do tempo de alistamento.

Devera mostrar o tempo que falta ou que passou do prazo.

'''

from datetime import date
sexo = str(input('Digite seu sexo (F/M):')).upper()
while True:
    if sexo == 'F':
        print('Você não precisa fazer o alistamento obrigatório!')
        break
    elif sexo == 'M':
        print('Você precisa fazer o alistamento obrigatório!')

    anoatual = date.today().year
    nasc = int(input('Digite seu ano de nascimento:'))
    idade = anoatual - nasc


    if idade <18:
        falta = 18 - idade
        sera = anoatual + falta
        print(f'Você tem {idade} anos de idade, ainda vai se alistar! Faltam {falta} anos!')
        print(f'Seu alistamento será em {sera}!')
    elif idade == 18:
        print(f'Você tem {idade} anos de idade, está na hora de se alistar!')
    elif idade > 18:
        passou = idade - 18
        foi = anoatual - passou
        print(f'Você tem {idade} anos de idade, já passou do tempo de se alistar! Passou {passou} anos do prazo!')
        print(f'Seu alistamneto foi em {foi}!')