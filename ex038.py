#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
print('='*6, 'DESAFIO 38/AULA12', '='*6)
print('-=-'*20)
numb1 = int(input('Digite um número: '))
numb2 = int(input('Digite outro número: '))
if numb1 > numb2:
    print('O primeiro valor é maior')
elif numb1 < numb2:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dos são iguais.')
