# print('=' * 6, 'DESAFIO 70/AULA15', '=' * 6)
# print('-=-' * 20)
text1 = 'LOJA SUPER BARATÃO'
text2 = 'FIM DO PROGRAMA'
tot = c = cheap = 0
cheapest = option = ' '
print('--' * 20)
print(f'{text1:^40}')
print('--' * 20)
while True:
    option = ' '
    product = str(input('Nome do produto: '))
    price = float(input('Preço: R$ '))
    tot += price
    if price > 1000:
        c += 1
    if cheap == 0:
        cheap = price
        cheapest = product
    elif price < cheap:
        cheap = price
        cheapest = product
    while option not in 'SsNn':
        option = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if option == 'N':
        break
print(f'{text2:-^40}')
print(f'O total da compra foi R$ {tot:.2f}.')
print(f'Temos {c} produto custando mais de R$ 1000,00.')
print(f'O produto mais barato foi um(a) {cheapest} que custa R$ {cheap:.2f}.')
