from datetime import date
print('='*6, 'DESAFIO 32/AULA10', '='*6)
ano = int(input('Qual ano a ser analisado? Coloque 0 par aanalisar o ano atual.'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
print('--FIM--')
