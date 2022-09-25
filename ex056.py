
print('='*6, 'DESAFIO 56/AULA13', '='*6)
print('-=-'*20)
sum = 0
mo = 0
w = 0
for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    name = str(input(f'Nome: ').strip())
    age = int(input(f'Idade: '))
    sex = str(input(f'Sexo[M/F]: ').upper().strip())
    sum += age
    if sex == 'M' and age > mo:
        mo = age
        nameno = name
    if sex == 'F' and age < 20:
        w = w + 1
media = float(sum/4)
print(f'A média de idade do grupo é {media} anos.')
print(f'O homem mais velho do grupo é {nameno}, com {mo} anos.')
print(f'Quantidade de mulher(es) com menos de 20 anos: {w}.')
