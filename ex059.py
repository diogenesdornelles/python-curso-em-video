print('=' * 6, 'DESAFIO 59/AULA14', '=' * 6)
print('-=-' * 20)
numb1 = int(input('Digite um número: '))
numb2 = int(input('Digite outro número: '))
option = 1
while 0 < option < 5:
    print('-=-' * 20)
    print('Escolha uma das opções abaixo:')
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos números')
    print('[5] - Sair do programa')
    print('-=-' * 20)
    option = int(input('>>>>> '))
    if option == 1:
            sum = numb1 + numb2
            print(f'O resultado de {numb1} + {numb2} é {sum}')
    elif option == 2:
            mult = numb1 * numb2
            print(f'O resultado de {numb1} X {numb2} é {mult}')
    elif option == 3:
        if numb1 > numb2:
            maj = numb1
        else:
            maj = numb2
        print(f'O maior número entre {numb1} e {numb2} é {maj}')
    elif option == 4:
        numb1 = int(input('Digite um número: '))
        numb2 = int(input('Digite outro número: '))
    elif option == 5:
        print('ENCERRANDO...')
        break
    elif option > 5:
        print('Opção INVÁLIDA: Digite outra opção.')
        option = 4
print('Fim do programa! Volte sempre!')
