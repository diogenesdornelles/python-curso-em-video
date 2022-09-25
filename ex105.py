# print('=' * 6, 'DESAFIO 105/AULA21', '=' * 6)
# print('-=-' * 20

def notas(*x, sit=False):
    """
    -> Esta função recebe diversos valores e os retorna num dicionário informando total
    de valores, maior deles e sua média, bem como situação, caso argumento sit verdadeiro.
    :param * x: float. Valores opcionais referentes às notas.
    :param sit: bool. Valor booleano que determina mostrar a situação
    :return dicionário turma com informações sobre média, total de notas e situação da turma
    """
    maj = total = 0
    turma = {'total': len(x)}
    for c in range(len(x)):
        if x[c] > maj:
            maj = x[c]
        total += x[c]
    turma['maior'] = maj
    media = round(total / len(x), 2)
    turma['média'] = media
    if media >= 7:
        t = 'BOA'
    elif 7 > media >= 5:
        t = 'RAZOÁVEL'
    elif 5 > media:
        t = 'RUIM'
    if sit:
        turma['situação'] = t
    return turma


resp = notas(7, 10, 9.52, 4.9, 10, 8.7, 5.6, sit=True)
print('—' * 30)
print(resp)
help(notas)

