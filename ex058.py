print('='*6, 'DESAFIO 58/AULA14', '='*6)
print('-=-'*20)
from random import randint
numb2 = -1
c = 1
print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
numb1 = randint(0, 10)
while numb1 != numb2:
    numb2 = int(input('Em que número pensei?'))
    print('PROCESSANDO...')
    if numb1 == numb2:
        print('PARABÉNS! Você conseguiu vencer!')
    else:
        if numb1 > numb2:
            print(f'Você ERROU! É mais que {numb2}!')
        else:
            print(f'Você ERROU! É menos que {numb2}!')
        c += 1
print(f'O número sorteado foi {numb1}. Você precisou de {c} tentativas.')
