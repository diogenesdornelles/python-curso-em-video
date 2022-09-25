sex = str(input(f'Informe o sexo da pessoa[M/F]: ')).upper().strip()[0]
while sex not in 'MnFf':
    sex = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()[0]
if sex.upper() == 'F':
    sex = str('feminimo')
else:
    sex = str('masculino')
print(f'Sexo {sex} registrado com sucesso!')
