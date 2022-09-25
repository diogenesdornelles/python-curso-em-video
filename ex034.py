
print('='*6, 'DESAFIO 34/AULA10', '='*6)
salario = float(input('Informe o salário do funcionário: '))
if salario > 1250.00:
    novosalario = salario*1.10
    perc = 10
else:
    novosalario = salario*1.15
    perc = 15
print('O salário era de R$ {:.2f}. Com o aumento de {:.2f}%, passa a ser de R$ {:.2f}.'.format(salario, perc, novosalario))
