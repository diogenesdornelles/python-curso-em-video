# print('=' * 6, 'DESAFIO 103/AULA21', '=' * 6)
# print('-=-' * 20)

def ficha(x='<desconhecido>', y=0):
    print(f'O jogador {x} fez {y} gol(s) no campeonato.')


print('--' * 20)
a = str(input('Nome do jogador: '))
b = str(input('Número de gol(s): '))  # validação para valor numérico. 1) Deixar valor 'str' ('int' não aceita em
# branco)
if b.isnumeric():
    b = int(b)  # retorna str para int.
else:
    b = 0  # se não for numérico, retorna str para 0.
if a.strip() == '':
    ficha(y=b)
else:
    ficha(a, b)
