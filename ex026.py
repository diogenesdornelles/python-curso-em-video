# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela
# aparece a primeira vez e em que posição ela aparece a última vez.
print('='*6, 'DESAFIO 26/AULA09', '='*6)
frase = str(input('Digite uma frase: ')).strip().upper()
n1 = frase.count('A')
n2 = frase.find('A')
n3 = frase.rfind('A')
print("Quantidade de 'A(s)' que aparece(m) na frase: {}".format(n1))
print("Posição em que ela aparece a primeira vez: {}".format(n2))
print("Posição em que ela aparece a última vez: {}".format(n3))
