###Crie um programa que leia o nome completo de uma pessoa e mostre:

print('='*6, 'DESAFIO 22/AULA09', '='*6)
name = str(input('Digite o nome completo da pessoa: ')).strip()
maiusc = name.upper()
minusc = name.lower()
letras = len(name) - name.count(' ')
indice = name.find(' ')
primeironome = len(name[0:indice])
print('Analisando o seu nome...:')
print('Seu nome em maiúsculas: {};'.format(maiusc))
print('Seu nome em minúsculas: {};'.format(minusc))
print('Seu nome tem ao todo: {} letras; e'.format(letras))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(name[0:indice], primeironome))


