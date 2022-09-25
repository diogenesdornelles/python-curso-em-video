# print('=' * 6, 'DESAFIO 96/AULA20', '=' * 6)
# print('-=-' * 20)

#  função área
def area():
    tam = l * c
    return tam


#  programa principal
print('Controle de Terrenos: ')
print('—' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
s = area()
print(f'A área do terreno {l:.2f}X{c:.2f} é de {s:.2f}m².')
