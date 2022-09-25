
print('='*6, 'DESAFIO 31/AULA10', '='*6)
distancia = float(input('Digite a distância da viagem(KM): '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    passagem = float(distancia * 0.5)
    print('Preço da passagem: R$ {:.2f}'.format(passagem))
else:
    passagem = float(distancia * 0.45)
    print('Preço da passagem: R$ {:.2f}'.format(passagem))
print('--FIM--')
