print('='*6, 'DESAFIO 43/AULA12', '='*6)
print('-=-'*20)
b = float(input('Informe o peso do paciente(kg): '))
h = float(input('Informe a altura do paciente(m): '))
IMC = b / (h ** 2)
if IMC <= 18.5:
    frase = 'Abaixo do peso ideal'
elif IMC > 18.5 and IMC < 25:
    frase = 'Peso ideal'
elif IMC >= 25 and IMC < 30:
    frase = 'Sobrepeso'
elif IMC >= 30 and IMC <= 40:
    frase = 'Obesidade'
else:
    frase = 'Obesidade móbida'
print('IMC: {:.2f}; Status: {}.'.format(IMC, frase))
