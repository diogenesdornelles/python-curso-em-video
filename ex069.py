# print('=' * 6, 'DESAFIO 69/AULA15', '=' * 6)
# print('-=-' * 20)
text1 = 'CADASTRE UMA PESSOA'
text2 = 'FIM DO PROGRAMA'
maj = man = wom_y = 0
while True:
    sex = option = ' '
    print('--' * 20)
    print(f'{text1:^40}')
    print('--' * 20)
    age = int(input('Idade: '))
    if age >= 18:
        maj += 1
    while sex not in 'FfMn':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sex == 'M':
            man += 1
        if sex == 'F' and age < 20:
            wom_y += 1
    print('--' * 20)
    while option not in 'SsNn':
        option = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if option == 'N':
        break
print(f'{text2:=^40}')
print(f'Total de pessoas com mais de 18 anos: {maj}.')
print(f'Ao todo temos {man} homens cadastrados.')
print(f'E temos {wom_y} mulheres com menos de 20 anos.')

