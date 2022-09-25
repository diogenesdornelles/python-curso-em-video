# print('=' * 6, 'DESAFIO 72/AULA16', '=' * 6)
# print('-=-' * 20)
list_numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n1 = int(input('Digite um número entre 0 e 20: '))
while n1 < 0 or n1 > 20:
    n1 = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {list_numbers[n1]}.')
