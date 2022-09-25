# print('=' * 6, 'DESAFIO 77/AULA16', '=' * 6)
# print('-=-' * 20)
tuple_01 = ('aprender',
            'programar',
            'linguagem',
            'python',
            'curso',
            'gratis',
            'estudar',
            'praticar',
            'trabalhar',
            'mercado',
            'programador',
            'futuro',
            'viajar',
            'sistema',
            'anotar',
            'inconstitucional',
            'contrato')
for c in range(0, len(tuple_01)):
    print(f'\nNa palavra {tuple_01[c].upper()} temos', end=' ')
    for i in range(0, len(tuple_01[c])):
        if (tuple_01[c][i] == 'a') or \
           (tuple_01[c][i] == 'e') or \
           (tuple_01[c][i] == 'i') or \
           (tuple_01[c][i] == 'o') or \
           (tuple_01[c][i] == 'u'):
            n = tuple_01[c][i]
            print(f'{n}', end=' ')

# Guanabara
# for p in tuple_01:
#     print(f'\nNa palavra {tuple_01[c].upper()} temos', end=' ')
#     for letra in p:
#          if letra.lower() in 'aeiou':
#              print(letra, end='')
