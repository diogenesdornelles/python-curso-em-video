#if p == 1
#   maior = p
#   menor = p
#else

print('='*6, 'DESAFIO 55/AULA13', '='*6)
print('-=-'*20)
ma = 0
mi = 0
for c in range(1, 6):
    w = float(input(f'Informe o peso da {c}ª pessoa(kg): '))
    w1 = w
    w2 = w
    if w1 > ma:
        ma = w1
    if mi == 0:
        mi = w2
    elif mi != 0:
        if mi > w2:
            mi = w2
print(f'O maior peso informado foi {ma}kg e o menor {mi}kg')
