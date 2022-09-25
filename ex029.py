# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
print('='*6, 'DESAFIO 29/AULA10', '='*6)
velocidade = float(input('Digite a velocidade atual do carro(KM/H): '))
if velocidade > 80:
    multa = float((int(velocidade - 80))*7.00)
    print('MULTADO! Você excedeu o limite permitido de 80km/h.')
    print('Você deve pagar uma multa no valor de R$ {}!'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança.')
print('--FIM--')
