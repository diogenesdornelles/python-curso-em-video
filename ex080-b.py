list_1 = []
c = maj = min = 0
while True:
    n = int(input('Digite um valor: '))
    if c == 0:
        maj = min = n
        list_1.insert(c, n)
        print('Adicionado ao final da lista...')
    elif c == 1:
        if n > maj:
            list_1.insert(c, n)
        else:
            list_1.insert((c - 1), n)
        print(f'Adicionado na posição {list_1.index(n)} da lista...')
    elif 1 < c < 5:
        if list_1[0] > n:
            list_1.insert(0, n)
        elif list_1[0] <= n <= list_1[-1]:
            for i in range(0, len(list_1) - 1):
                if list_1[i] < n < list_1[i + 1]:
                    list_1.insert(i, n)
                elif list_1[i] == n:
                    list_1.insert(i, n)
        elif list_1[-1] < n:
            list_1.insert(-1, n)
        print(list_1)
        print(f'Adicionado na posição {list_1.index(n)} da lista...')
    c += 1
    if c == 5:
        break
