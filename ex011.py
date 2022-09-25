# ler altura e largura parede e dizer área e quantidade de tinta
print('='*6, 'DESAFIO 11/AULA07', '='*6)
h = float(input('informe a altura da parede: '))
w = float(input('informe a largura da parede: '))
print('A parede possui {:.3f} m².\nSerão necessários {:.3f} litros de tinta para pintá-la.'.format(h*w, h*w/2))
