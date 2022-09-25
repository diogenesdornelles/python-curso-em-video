
def leiaDinheiro():
    while True:
        x1 = str(input('Digite o preço: R$ ')).strip()
        x = x1
        a = x.find(',')
        b = x.find('.')
        x = x.replace(',', '')
        x = x.replace('.', '')
        f = x.isnumeric()
        if a > 0:
            x = x[0:a] + '.' + x[a:]
        if b > 0:
            x = x[0:b] + '.' + x[b:]
        if f:
            break
        else:
            print(f'\033[0;31mERRO! "{x1}" é um preço inválido!.\033[m')
    return x
