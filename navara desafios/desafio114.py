import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError as e:
    print(f'Erro de URL: {e.reason}')
except urllib.error.HTTPError as e:
    print(f'Erro HTTP: {e.code} - {e.reason}')
except Exception as e:
    print(f'Ocorreu um erro inesperado: {e}')
else:
    print('Tudo ok!')
