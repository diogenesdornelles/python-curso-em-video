
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*20)
r1 = float(input('Digite o primeiro seguimento: '))
r2 = float(input('Digite o segundo seguimento: '))
r3 = float(input('Digite o terceiro seguimento: '))
print('-=-'*20)
print('Pode haver um triângulo de seguimentos {}, {} e {}?'.format(r1, r2, r3))
print('-=-'*20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('SIM. Os seguimentos formam um triângulo equilátero.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('SIM. Os seguimentos formam um triângulo osósceles.')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('SIM. Os seguimentos formam um triângulo escaleno.')
else:
    print('NÃO. Os seguimentos não podem formar um triângulo.')
print('-=-' * 20)
print('--FIM--')
