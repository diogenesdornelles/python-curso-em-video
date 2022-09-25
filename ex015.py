# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print('='*6, 'DESAFIO 14/AULA07', '='*6)
day = int(input('Quantos dias alugado: '))
km = float(input('Quantos Km(s) foram percorridos: '))
value = day*60 + 0.15*km
print('O total a pagar é de R$ {:.2f}.'.format(value))
