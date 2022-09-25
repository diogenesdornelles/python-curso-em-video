#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
print('='*6, 'DESAFIO 40/AULA12', '='*6)
print('-=-'*20)
n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a primeira nota do aluno: '))
media = (n1 + n2)/2
if media < 5:
    status = 'REPROVADO!'
elif (media >= 5) and (media < 7):
    status = 'RECUPERAÇÃO!'
else:
    status = 'APROVADO!'
print('As notas foram {} e {}, sendo que a média foi {:.2f}. O aluno está {}.'.format(n1, n2, media, status))
