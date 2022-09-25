# print('=' * 6, 'DESAFIO 104/AULA21', '=' * 6)
# print('-=-' * 20)

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um número inteiro válido.')
        return valor


n = leiaInt('Digite um valor numérico: ')
print(f'Você digitou o número {n}.')
