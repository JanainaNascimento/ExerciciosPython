'''
crie uma tupla com varias palavras (não usar acentos). depois disso,
voce deve mostrar, para cada palavra, quais são as suas vogais.

ex:
 na palavra aprender temos a e e
'''

palavras = ('jardim', 'comida', 'jantar',
            'aprender', 'amigos', 'trabalho',
            'estagio','emprego','sucesso',
            'experiencia','chocolate','redes',
            'livro','seguranca', 'dados')

for palavra in palavras:
    print(f'\nna palavra {palavra} temos ', end='')
    
    for letra in palavra:
        
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            