from datetime import date
print('='*6, 'DESAFIO 40/AULA12', '='*6)
print('-=-'*20)
born = int(input('Informe o ano de nascimento do atleta: '))
year = date.today().year
age = year - born
if age <= 9:
    cat = 'MIRIM'
elif age > 9 and age <= 14:
    cat = 'INFANTIL'
elif age > 14 and age <= 19:
    cat = 'JUNIOR'
elif age > 19 and age <= 25:
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'
print('O atleta tem {} anos e está na categoria {}.'.format(age, cat))
