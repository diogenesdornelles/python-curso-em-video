#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
print('='*6, 'DESAFIO 27/AULA09', '='*6)
name = str(input('Digite o nome completo de uma pessoa: ')).strip()
lista = name.split()
ind = name.rfind(' ')
name1 = name[ind:]
print('Primeiro nome: {}.'.format(lista[0]))
print('Último nome: {}.'.format(name1))
#print('Último nome: {}.'.format(lista[len(lista)-1])) solução Gustavo.
