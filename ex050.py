
print('='*6, 'DESAFIO 50/AULA13', '='*6)
print('-=-'*20)
sum = 0
cont = 0
for c in range(1, 7):
    numb = int(input(f'Digite o {c}º valor:'))
    if numb % 2 == 0:
        sum += numb
        cont += 1
print(f'Você informou {cont} valores pares. A soma dos valores pares é {sum}.')
