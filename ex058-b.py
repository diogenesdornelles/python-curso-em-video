from random import randint
computador = randint(0, 10)
print('Sou seu computador...A de pensar em um número entre 1 e 10.')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente uma vez.')
        elif jogador > computador:
            print('Menos.. Tente uma vez.')
print(f'Acertou com {palpites} tentativas')
