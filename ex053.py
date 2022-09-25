
print('='*6, 'DESAFIO 52/AULA13', '='*6)
print('-=-'*20)
frase = str(input('Digite uma frase: ')).strip().upper()
lista = frase.split()
frase1 = "".join(lista)
t = 0
for c in range(0, len(frase1)):
    n1 = int(len(frase1) - c)
    if (frase1[c]) == (frase1[n1 - 1]):
        t = t + 1
print(f'O inverso de {frase1} é ', end='')
for c in range(0, len(frase1)):
    n1 = int(len(frase1) - (c + 1))
    print((frase1[n1]), end='')
print('.')
if t == len(frase1):
    r = 'é um PALÍNDROMO'
else:
    r = 'não é um PALÍNDROMO'
print(f'\nA frase "{frase.lower().capitalize()}" {r}.')



