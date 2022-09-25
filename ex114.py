import urllib.error
import urllib.request

try:
    response = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('O site pudim está inacessível no momento.')
else:
    print('O site pudim está acessível no momento.')
finally:
    print('Obrigado pela preferência!')
