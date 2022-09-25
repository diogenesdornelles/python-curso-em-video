# print('=' * 6, 'DESAFIO 113/AULA23', '=' * 6)
# print('-=-' * 20)
def leiaInt(msg):
    while True:
        try:
            valor1 = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            return 0
        else:
            return valor1


def leiaFloat(msg):
    while True:
        try:
            valor2 = float(input(msg))
        except (ValueError, TypeError):
            print('Erro! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            return 0
        else:
            return valor2


n = leiaInt('Digite um valor numérico inteiro: ')
p = leiaFloat('Digite um valor numérico real: ')
print(f'Você digitou o número inteiro {n} e o número real {p}.')
