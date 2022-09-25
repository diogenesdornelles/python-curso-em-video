#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo
# será negado.
print('='*6, 'DESAFIO 36/AULA12', '='*6)
print('-=-'*20)
value = float(input('Informe o valor do imóvel: R$ '))
wage = float(input('informe o salário mensal do comprador: R$ '))
time = int(input('Informe a quantidade de anos do financiamento: '))
prest = value/(time*12)
if prest >= wage*0.3:
    print('Empréstimo NEGADO. Motivo: prestação mensal superior a 30% do salário comprovado.')
else:
    print('Empréstimo CONCEDIDO. Prestação mensal no valor de R$ {:.2f}.'.format(prest))
