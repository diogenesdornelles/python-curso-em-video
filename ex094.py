# print('=' * 6, 'DESAFIO 94/AULA19', '=' * 6)
# print('-=-' * 20)
pessoas = dict()
todas_pessoas = list()
todas_mulheres = list()
acima_media = list()
c = 1
while True:
    pessoas[f'nome{c}'] = str(input('Nome: '))
    sex = str(input('Sexo[M/F]: ')).upper().strip()[0]
    while sex not in 'MmFf':
        sex = str(input('ERRO! Sexo[M/F]: ')).upper().strip()[0]
    pessoas[f'sexo{c}'] = sex
    pessoas[f'idade{c}'] = int(input('Idade: '))
    todas_pessoas.append(pessoas.copy())
    pessoas.clear()
    r = str(input('Deseja continuar[S/N]: ')).upper().strip()[0]
    while r not in 'SsNn':
        r = str(input('ERR! Deseja continuar[S/N]: ')).upper().strip()[0]
    if r in 'Nn':
        break
    c += 1
print('-=-' * 20)
soma = c = 0
for c in range(len(todas_pessoas)):
    for k, v in todas_pessoas[c].items():
        if k == f'idade{c + 1}':
            soma = soma + v
        if k == f'sexo{c + 1}':
            if v == 'F':
                todas_mulheres.append(todas_pessoas[c][f'nome{c + 1}'])
media = soma/len(todas_pessoas)
for c in range(len(todas_pessoas)):
    for k, v in todas_pessoas[c].items():
        if k == f'idade{c + 1}':
            if v > media:
                acima_media.append(todas_pessoas[c][f'nome{c + 1}'])
print(f'- Foram cadastradas {len(todas_pessoas)} pessoas.')
print(f'- A média de idade do grupo é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for k, c in enumerate(todas_mulheres):
    if len(todas_mulheres) == 1:
        print(f'{c}.')
    elif len(todas_mulheres) == 2:
        if k == 0:
            print(f'{c}', end=' e ')
        else:
            print(f'{c}.')
    elif len(todas_mulheres) > 2:
        if k <= (len(todas_mulheres) - 3):
            print(f'{c}', end=', ')
        elif k == (len(todas_mulheres) - 2):
            print(f'{c}', end=' e ')
        elif k == len(todas_mulheres) - 1:
            print(f'{c}.')
print(f'- As pessoas acima da média de idade são: ', end='')
for k, c in enumerate(acima_media):
    if len(acima_media) == 1:
        print(f'{c}.')
    elif len(acima_media) == 2:
        if k == 0:
            print(f'{c}', end=' e ')
        else:
            print(f'{c}.')
    elif len(acima_media) > 2:
        if k <= (len(acima_media) - 3):
            print(f'{c}', end=', ')
        elif k == (len(acima_media) - 2):
            print(f'{c}', end=' e ')
        elif k == len(acima_media) - 1:
            print(f'{c}.')
