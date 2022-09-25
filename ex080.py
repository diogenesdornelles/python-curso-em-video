# print('=' * 6, 'DESAFIO 80/AULA17', '=' * 6)
# print('-=-' * 20)
list_1 = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > list_1[-1]:
        list_1.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(list_1):
            if n <= list_1[pos]:
                list_1.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista ...')
                break
            pos += 1
print('-=-' * 20)
print(f'Os valores digitados em ordem foram {list_1}')





