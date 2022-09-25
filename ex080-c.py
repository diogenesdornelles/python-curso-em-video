list_1 = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        list_1.append(n)
        print('Adicionado ao final da lista...')
        print(list_1)
    else:
        list_1.append(n)
        print(list_1)
        for i in range(0, c - 1):
            for j in range(i + 1, c):
                if list_1[i] > list_1[j]:
                    aux = list_1[i]
                    list_1[i] = list_1[j]
                    list_1[j] = aux
        print(f'Adicionado na posição {list_1.index(n)} da lista...')



