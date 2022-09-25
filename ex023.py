from math import trunc
print('='*6, 'DESAFIO 23/AULA09', '='*6)
#matematicamente
numb = int(input('Informe um número entre 0000 e 9999: '))
mil = trunc(numb/1000)
cen = trunc((numb - mil*1000)/100)
dez = trunc((numb - mil*1000 - cen*100)/10)
uni = trunc((numb - mil*1000 - cen*100 - dez*10)/1)
print('unidade: {}'.format(uni))
print('dezena: {}'.format(dez))
print('centena: {}'.format(cen))
print('milhar: {}'.format(mil))
#por string
numb1 = str(input('Informe um número entre 0000 e 9999: '))
mil1 = numb1[0]
cen1 = numb1[1]
dez1 = numb1[2]
uni1 = numb1[3]
print('unidade: {}'.format(uni1))
print('dezena: {}'.format(dez1))
print('centena: {}'.format(cen1))
print('milhar: {}'.format(mil1))
