while True:
    a = input("Digite algo:")
    print(" o tipo dessa variavel é", type(a))
    print("Tem espaço?", a.isspace())
    print("Tem letra?", a.isalpha())


    r = input('Deseja repetir?[s]/[n]: ')
    if r == 's' or r == 'S':
        pass
    elif r == 'n' or r == 'N':
        print("finalizado!")
        break
    else:
        print('opção inválida!') #usado quando so se for 's' ou 'n' se não fecha
    break


