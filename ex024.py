
print('='*6, 'DESAFIO 24/AULA09', '='*6)
cidade = str(input('Digite o nome de uma cidade: ')).strip()
cidadeup = cidade.upper()
santo = cidadeup.find('SANTO'[0:5])
if santo == -1:
    print("A cidade {} não começa com 'SANTO'.".format(cidade))
else:
    print("A cidade {} começa com 'SANTO'.".format(cidade))

#print(cidade[:5].uppser() == 'SANTO') - retorna verdadeiro ou falso
