import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('O site Youtube não está acessível')
else:
    print('Consegui acessar o site Youtube com sucesso!')
