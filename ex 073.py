'''
crie uma tupla preenchida com os 20 primeiros colocados da tabela
do campeonato brasileiro de futebol, nas ordem de colocação. depois mostre:
a) apenas os 5 primeiros colocados.
b) os ultimos 4 colocados da tabela.
c) uma lista como times em ordem alfabetica
d)em que posição na tabela esta o time da chapecoense.
'''

times = ('Sao Paulo','Internacional','Atlético','Flamengo','Grêmio','Palmeiras',
    'Fluminense','Santos','Corinthians','Athletico','Ceará','Atlético',
    'Bragantino','Sport','Fortaleza','Vasco','Bahia','Goiás','Botafogo','Coritiba')
print('****' * 30)
print(f'Os cinco primeiros colocados são: {times[0:5]}') 
print('****' * 30)
print(f'Os ultimos quatro colocados são: {times[-4:]}')
print('****' * 30)
print(f'Times listados em ordem alfabetica: {sorted(times)}')
print('****' * 30)
print(f'O Ceará está na {times.index("Ceará")+1}º posição')
print('****' * 30)
