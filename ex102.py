# print('=' * 6, 'DESAFIO 102/AULA21', '=' * 6)
# print('-=-' * 20)

def fatorial(n, show=True):
    """
    -> calcula o fatorial de um número
    :param n: int. O número a ser calculado.
    :param show: bool. Opcional: mostrar ou não a conta.
    :return: int. Retorna o fatorial do n.
    """
    s = 1
    for c in range(n, 0, -1):
        s *= c
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            elif c == 1:
                print(f'{c} ', end='')
    print(' = ', end=' ')
    return s


fat = fatorial(int(input('Informe um número: ')), bool(input('Deseja mostrar cálculo?[Enter para não]: ')))
print(f'{fat}')
help(fatorial)
