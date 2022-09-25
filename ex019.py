#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo
# o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
print('='*6, 'DESAFIO 19/AULA08', '='*6)
student1 = input('informe o nome do primeiro aluno: ')
student2 = input('informe o nome do segundo aluno: ')
student3 = input('informe o nome do terceiro aluno: ')
student4 = input('informe o nome do quarto aluno: ')
sort = random.choice([student1, student2, student3, student4])
print('O aluno sorteado para apagar o quadro foi {}.'.format(sort))
