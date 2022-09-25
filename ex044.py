print('='*6, 'DESAFIO 44/AULA12', '='*6)
print('-=-'*20)
value = float(input('Informe o valor das compras: '))
print('-=-'*20)
print('Escolha a condição de pagamento: ')
print('[1] - à vista dinheiro/cheque:  desconto de 10%.')
print('[2] - à vista no cartão: desconto de 5%.')
print('[3] - até 2x no cartão: preço normal.')
print('[4]- 3x ou mais no cartão: juros de 20%.')
print('-=-'*20)
opcao = int(input())
print('Compras no valor de R$ {:.2f}.'.format(value))
if opcao == 1:
    desconto = value*0.9
    print('Com desconto de 10%, as compras ficam no valor à vista de R$ {:.2f}.'.format(desconto))
elif opcao == 2:
    desconto = value*0.95
    print('Com desconto de 5%, as compras ficam no valor à vista de R$ {:.2f}.'.format(desconto))
elif opcao == 3:
    prest = value/2
    print('Sem desconto, as compras ficam em duas parcelas de R$ {:.2f}.'.format(prest))
elif opcao == 4:
    nprest = int(input('Informe a quantidade de parcelas: '))
    juros = value*1.2
    prest = juros/nprest
    print('com juros de 20%, o produto fica no valor de R$ {:.2f}, a ser pago em {} prestações de R$ {:.2f}.'.format(juros, nprest, prest))
else:
    print('Opção Inválida de pagamento. Tente novamemte')
