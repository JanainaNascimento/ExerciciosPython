while True:
    salário = float(input('Digite o valor do seu salário atual :\n'))

    if salário < 1000:
        salário = salário * 1.5
    elif salário < 2500:
        salário = salário * 1.3
    elif salário < 4000:
        salário = salário * 1.2
    elif salário <= 6000:
        salário = salário * 1.1
    else:
        print(f'Seu salário final é de {salário}!\n')
    print(f'Salário reajustado para {salário}\n')

    escolha = input('Quer continuar?(S/N)')

    if escolha == 's' or escolha == 'S':
        pass
    elif escolha == 'n' or escolha == 'N':
        break
    else:
        print('opção inválida!')
        break