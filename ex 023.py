'''
crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

'''

cidade = str(input('Digite o nome de uma cidade: ')).upper().strip()
cid = cidade.split()
print('SANTO' in cid[0])

#exemplo que funciona tambem
#print(cidade[:5].upper() == 'SANTO')