'''
crie uma tupla totalmente preenchida
com uma contagem por extenso de 0 até 20.

devera ler um numero pelo teclado
(entre 0 e 20) e mostra-lo por extenso.

somente entre esse valor
mostra escrito o numero vinte, zero etc.

'''
# contagem = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
# extenso = ('um','dois','três','quatro','cinco','seis', 'sete','oito','nove','dez','onze', 'doze', 'treze',
# 'catorze','quinze', 'dezesseis','dezessete', 'dezoito','dezenove','vinte')

# while True:
#     numero = int(input('digite um numero: '))
#     for a in contagem:
#         if a == numero:
#             print(extenso[a-1])
    
#     r = input('continuar: ')
#     if r == 's':
#         pass
#     elif r == 'n':
#         break

contagem =('zero','um','dois','três','quatro',
           'cinco','seis','sete','oito','nove',
           'dez','onze','doze','treze','catorze', 
           'quinze', 'dezesseis','dezessete', 
           'dezoito','dezenove','vinte')

while True:
    num = int(input('Digite um numero de 0 a 20: '))
    if num >= 0 and num <= 20:
        break
    print(f'tente novamente!')

print(f'O número digitado escrito em extenso é {contagem[num]}')




        
