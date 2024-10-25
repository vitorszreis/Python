import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

posts = site.findAll('div', attrs = {'class': 'feed-post-body'})

#titulo = posts.findAll('a', attrs = {'class': 'feed-post-link gui-color-primary gui-color-hover'})

for post in posts:

    titulo = post.find('a', attrs={'class': 'feed-post-link'})
    
    subtitulo = post.find('div', attrs={'class': 'feed-post-body-resumo'})
    
    if subtitulo:
        print("Subtítulo:", subtitulo.text)
        lista_noticias.append([titulo.text,subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text,'', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Titulo','Subtitulo','link'])

news.to_excel('noticias.xlsx', index=False)
    
print(news)  