from datetime import date
print('='*6, 'DESAFIO 54/AULA13', '='*6)
print('-=-'*20)
m = 0
g = 0
y = date.today().year
for c in range(0, 7):
    n = int(input(f'Digite o ano de nascimento da {c + 1}ª pessoa: '))
    if y - n >= 21:
        m += 1
    else:
        g += 1
print(f'O número de pessoas maiores de idade é {m} e número de menores de idade é {g}')


