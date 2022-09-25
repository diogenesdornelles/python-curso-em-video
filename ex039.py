from datetime import date
print('='*6, 'DESAFIO 39/AULA12', '='*6)
print('-=-'*20)
born = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - born
print('Quem nasceu em {} tem {} anos de idade em {}'.format(born, idade, ano))
if idade == 18:
    print('Atenção: você completou {} anos em {}. Aliste-se já!'.format(idade, ano))
elif idade < 18:
    tempo = 18 - idade
    print('O alistamento será no ano de {}.'.format(born + 18))
    print('Faltam {} anos para o alistamento militar obrigatório.'.format(tempo))
else:
    tempo = abs(18 - idade)
    print('O alistamento foi no ano de {}.'.format(born + 18))
    print('Já deveria ter se alistado há {} anos.'.format(tempo))
