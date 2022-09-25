# print('=' * 6, 'DESAFIO 66/AULA15', '=' * 6)
# print('-=-' * 20)
c = s = 0
while True:
    numb = int(input('Digite um número (999 para parar): '))
    if numb == 999:
        break
    c += 1
    s += numb
print(f'Foram digitados {c} valores e a soma deles é {s}!.')


