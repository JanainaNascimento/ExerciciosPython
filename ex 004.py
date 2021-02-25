# n = input('digite algo: ')
# print(n.isnumeric())#verifica se o valor digitado é um número ou não
# print(n.isalpha())#verifica se o valor digitado é letra
# print(n.isspace())#verifica se foram digitados espaços
# print(n.isascii())#verificar se foram digitados caracters especiais
# print(n.isalnum())#verfica se foi digitado números e letras
# print(n.isdigit())#verfica se tem inteiros positivos
# print(n.isupper())#verificar se so foi digitado letras maisculas
# print(n.islower())#verifica se esta tudo em minusculas
# print(n.istitle())#verfica se esta capitalizada a primeira letra é maiscula

n = input('valor:')
while not n.isnumeric():
    n = input('digite numeros: ')
print('fim')
