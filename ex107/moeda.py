def moeda(x=0):
    g = f'R${x:.2f}'
    t = g.replace('.', ',')
    return t


def aumentar(x=0, z=False, y=0):
    x = float(x * (1 + y/100))
    if z is not False:
        moeda(x)
        v = moeda(x)
        return v
    else:
        return x


def diminuir(x=0, z=False, r=0):
    x = float(x * (1 - r/100))
    if z:
        moeda(x)
        v = moeda(x)
        return v
    else:
        return x


def dobro(x=0, z=False):
    x = x * 2
    if z is True:
        moeda(x)
        v = moeda(x)
        return v
    else:
        return x


def metade(x=0, z=False):
    x = float(x/2)
    return x if z is False else moeda(x)


def resumo(x=0, y=0, r=0):
    text = 'RESUMO DO VALOR'
    print('—' * 29)
    print(' ' * 7, text, ' ' * 7)
    print('—' * 29)
    print(f'{"Preço analisado:":<20} {moeda(x)}')
    print(f'{"Dobro do preço:":<20} {dobro(x, True)}')
    print(f'{"Metade do preço:":<20} {metade(x, True)}')
    print(f'{y}{"% de aumento:":<18} {aumentar(x, True, y)}')
    print(f'{r}{"% de redução":<18} {diminuir(x, True, r)}')
