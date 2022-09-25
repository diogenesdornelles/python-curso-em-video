# ler notas de auluno e mostrar média
print('='*6, 'DESAFIO 07/AULA07', '='*6)
value1 = float(input('Informe a primeira nota do aluno: '))
value2 = float(input('Informe a segunda nota do aluno: '))
m = (value1 + value2)/2
print('As notas do aluno foram {:.1f} e {:.1f} e a média obtida foi {:.2f}'.format(value1, value2, m))
