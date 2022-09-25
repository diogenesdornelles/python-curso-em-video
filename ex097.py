# print('=' * 6, 'DESAFIO 97/AULA20', '=' * 6)
# print('-=-' * 20)

#  início da função:
def escreva(text1):
    a = len(text1) + 4

    def linha():
        print('~' * a, end='')

    linha()
    print()
    print(f'  {text1} ')
    linha()
    print()


#  início do programa principal:
for c in range(3):
    escreva(str(input('Digite um texto qualquer: ')))
