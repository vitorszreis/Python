# - Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usuário

import requests
from bs4 import BeautifulSoup

url_base = 'https://www.mercadolivre.com.br/'

produto = input('Qual produto voce deseja? ')

response = requests.get(url_base + produto)

site = BeautifulSoup(response.text, 'html.parser')

item = site.find('div', attrs = {'class': 'poly-card poly-card--list'})

print(item.prettify())   

