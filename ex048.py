
print('='*6, 'DESAFIO 48/AULA13', '='*6)
print('-=-'*20)
sum = 0
cont = 0
for c in range(1, 501, 2):
   if c % 2 != 0 and c % 3 == 0:
       sum += + c
       cont += + 1
       print(f'..{c}')
print(f'\bA soma de todos os {cont} termos é {sum}.')

