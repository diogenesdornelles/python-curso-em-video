# print('=' * 6, 'DESAFIO 101/AULA21', '=' * 6)
# print('-=-' * 20)
import datetime


def voto(y):
    age = datetime.date.today().year - y
    if 70 > age > 17:
        r = 'obrigatório'
    elif age < 16:
        r = 'negado'
    else:
        r = 'opcional'
    return [r, age]


t = voto(int(input('Informe o ano de nascimento do eleitor: ')))
print(f'O eleitor tem idade {t[1]} anos, portanto, voto {t[0]}.')
