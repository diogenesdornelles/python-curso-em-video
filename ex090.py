# print('=' * 6, 'DESAFIO 90/AULA19', '=' * 6)
# print('-=-' * 20)
aluno = {'Nome': str(input('Nome: ')), 'Média': float(input('Média: '))}
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Em recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
