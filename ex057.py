
print('='*6, 'DESAFIO 57/AULA14', '='*6)
print('-=-'*20)
man = wom = 0
c = 1
ans = ' '
while ans != 'N':
    sex = str(input(f'Informe o sexo da {c}ª pessoa[M/F]: ')).upper().strip()[0]
    if sex == 'M' or sex == 'F':
        if sex == 'M':
            man += 1
            print('Sexo masculino registrado com sucesso!')
        if sex == 'F':
            wom += 1
            print('Sexo feminino registrado com sucesso!')
        c += 1
        print('Deseja informar outro registro [S/N]?')
        ans = str(input()).upper()
    else:
        print('Resposta inválida! Informe "M"(para Masculino) ou "F"(para Feminino):')
print(f'Foram informadas {man} pessoas do sexo masculino e {wom} pessoas do sexo feminino.')
