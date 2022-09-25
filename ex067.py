# print('=' * 6, 'DESAFIO 67/AULA15', '=' * 6)
# print('-=-' * 20)
while True:
    numb = int(input('Digite um número para mostrar a tabuada (negativo para parar): '))
    if numb < 0:
        break
    c = 1
    print('-' * 13)
    while c < 11:
        print(f'|{numb} X {c:2} = {numb * c:2}|')
        c += 1
    print('-' * 13)
print('Programa de tabuada ENCERRADO. Volte sempre!')
