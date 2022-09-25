
print('='*6, 'DESAFIO 25/AULA09', '='*6)
name = str(input('Digite o seu nome completo: ')).strip()
nameup = name.upper()
silva = nameup.find('SILVA')
if silva == -1:
    print("O nome {} não contém 'SILVA'.".format(name))
else:
    print("O nome {} contém 'SILVA' na posição {}.".format(name, silva))

#print('Seu nome tem Silva? {}'.format('silva in nome.lower())) retorna true or false
#print('Seu nome tem Silva? {}'.format(nome[:5] == 'Silva')) retorna true or false