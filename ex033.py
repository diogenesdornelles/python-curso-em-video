#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('='*6, 'DESAFIO 33/AULA10', '='*6)
numb1 = int(input('Digite o primeiro número: '))
numb2 = int(input('Digite o segundo número: '))
numb3 = int(input('Digite o terceiro número: '))
if numb1 > numb2 and numb1 > numb3:
    print('O número {} é o maior'.format(numb1))
if numb2 > numb1 and numb2 > numb3:
    print('O número {} é o maior'.format(numb2))
if numb3 > numb1 and numb3 > numb2:
    print('O número {} é o maior'.format(numb3))
if numb1 < numb2 and numb1 < numb3:
    print('O número {} é o menor'.format(numb1))
if numb2 < numb1 and numb2 < numb3:
    print('O número {} é o menor'.format(numb2))
if numb3 < numb1 and numb3 < numb2:
    print('O número {} é o menor'.format(numb3))
print('--FIM--')
