# print('=' * 6, 'DESAFIO 71/AULA15', '=' * 6)
# print('-=-' * 20)
text1 = 'BANCO CEV'
text2 = 'Volte sempre ao BANCO CEV! Tenha um bom dia!'
print('==' * 20)
print(f'{text1:^40}')
print('==' * 20)
valor = int(input('Que valor você quer sacar: R$ '))
c1 = 50
c2 = 20
c3 = 10
c4 = 1
n1 = n2 = n3 = n4 = 0
while True:
    if valor % c1 == 0:
        n1 = int(valor/c1)
        break
    else:
        n1 = valor//c1
    if (valor - n1*c1) % 20 == 0:
        n2 = int((valor-n1*c1)/c2)
        break
    else:
        n2 = (valor-n1*c1)//20
    if (valor-n1*c1-n2*c2) % 10 == 0:
        n3 = int((valor-n1*c1-n2*c2)/c3)
        break
    else:
        n3 = (valor-n1*c1-n2*c2)//10
    n4 = int((valor-n1*c1-n2*c2-n3*c3)/c4)
    break
if n1 != 0:
    print(f'Total de {n1} cédula(s) de R$ 50,00')
if n2 != 0:
    print(f'Total de {n2} cédula(s) de R$ 20,00')
if n3 != 0:
    print(f'Total de {n3} cédula(s) de R$ 10,00')
if n4 != 0:
    print(f'Total de {n4} cédula(s) de R$ 1,00')
print('==' * 20)
print(f'{text2}')
