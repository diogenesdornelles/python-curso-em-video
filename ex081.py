# print('=' * 6, 'DESAFIO 81/AULA17', '=' * 6)
# print('-=-' * 20)
list_1 = []
while True:
    list_1.append(int(input('Digite um número: ')))
    r = str(input('Deseja digitar outro número?[S/N]')).strip().upper()[0]
    while r not in 'SsNn':
        r = str(input('ERRO! Deseja digitar outro número?[S/N]')).strip().upper()[0]
    if r == 'N':
        break
print('-=-' * 20)
print(f'Foram digitados {len(list_1)} números')
list_1.sort(reverse=True)
print(f'Os números digitados, na ordem decrescente, foram: {list_1}')
if 5 in list_1:
    print('O valor 5 faz parte da lista!')
elif 5 not in list_1:
    print('O valor 5 não faz parte da lista')

