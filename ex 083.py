'''
crie um programa onde o usuario digite uma expressao qualquer
que use parenteses. seu aplicativo devera analisar se a expressao passada
esta com os parenteses na ordem correta.

exemplos de uso correto: (()), ()
exemplos de uso errado: ((), (

'''
exp = str(input('Digite uma expressão com (): '))
lista = []
for i in exp:
    if i == '(':
        lista.append('(')
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida')
else:
    print(f'Sua expressão está inválida')



