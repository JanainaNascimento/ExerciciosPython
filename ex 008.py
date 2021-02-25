while True: #loop principal
    n = int(input('Digite um número: '))
    i = 1
    while i <11:
        print(f'{n} x {i} = {n * i:1.0f}')
        i += 1
    r = input('Deseja repetir?[s]/[n]: ')
    if r == 'n' or r == 'N':
        break
print('fim!')
