#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('='*6, 'DESAFIO 37/AULA12', '='*6)
print('-=-'*20)
numb = int(input('Informe um número qualquer: '))
print('-=-'*20)
print('Escolha a base de conversão numérica:')
print("Digite '1' para binário")
print("Digite '2' para octal")
print("Digite '3' para hexadecimal")
escol = int(input())
print('-=-'*20)
if escol == 1:
    print('O número {} em binário corresponde a {}.'.format(numb, bin(numb)[2:]))
elif escol == 2:
    print('O número {} em octal corresponde a {}.'.format(numb, oct(numb)[2:]))
else:
    print('O número {} em hexadecimal corresponde a {}.'.format(numb, hex(numb)[2:]))
