# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
# leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
print('='*6, 'DESAFIO 20/AULA08', '='*6)
student1 = input('informe o nome do primeiro aluno: ')
student2 = input('informe o nome do segundo aluno: ')
student3 = input('informe o nome do terceiro aluno: ')
student4 = input('informe o nome do quarto aluno: ')
sort = student1, student2, student3, student4
studentlist = random.choices(sort, k=4)
print(type(studentlist))
print('A apresentação se dará na seguinte ordem: {}.'.format(studentlist))
