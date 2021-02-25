#tabuada

while True: #loop principal
    n = int(input('Digite um número: '))
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')

    r = input('Deseja repetir?[s]/[n]: ')
    if r == 's' or r == 'S':
        pass
    elif r == 'n' or r == 'N':
        break
    else:
        print('opção inválida!') #usado quando so se for 's' ou 'n' se não fecha
        break

'''
while True: #loop principal
    n = int(input('Digite um número: '))
    for i in range (1,11):
            print(f'{n} x {i} = {n*i:4.1f}')
    r = input('Deseja repetir?[s]/[n]: ')
    if r == 'n' or r == 'N':
        break
print('fim!')


for x in range(5):
    print(x, end="  ") # end=" " da um espaço entre os números
    #esse for tem esse resultado '0  1  2  3  4'

for x in range(0, 11):
    print(x, end="  ")  # da um espaço entre os números
   #esse for tem esse resultado '0  1  2  3  4  5  6  7  8  9  10'
   #ele faz do 0 ao 10, pois não faz o 11 o último número

for x in range(0, 11, 2):
    print(x, end="  ")  # da um espaço entre os números
    #esse for tem esse resultado '0  2  4  6  8  10'
    #ele faz do 0 ao 10 e pulando duas casas



for i in [1, 2, 3]:
    senha = int(input("Digite a sua senha numérica: "))
    if senha == 1234:
        print("SENHA CORRETA")
        break
    else:
        print("SENHA INCORRETA")
else: print("VOCÊ ATINGIU AS TRÊS TENTATIVAS")
'''