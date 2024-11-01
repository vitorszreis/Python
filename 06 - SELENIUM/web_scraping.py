from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from time import sleep

options = Options()
options.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options=options)

navegador.get('https://www.youtube.com/')

elemento = WebDriverWait(navegador, 10).until(
    EC.visibility_of_element_located((By.NAME, 'search_query'))
)
elemento.send_keys('web scraping em python')

elemento.submit()

sleep(3)

primeiro_video = WebDriverWait(navegador, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="video-title"]'))
)
titulo = primeiro_video.get_attribute("title")

print("Título do primeiro vídeo:", titulo)
 
thumbnail = WebDriverWait(navegador, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="thumbnail"]/yt-img-shadow/img'))
)
thumbnail_url = thumbnail.get_attribute("src")

print("URL da miniatura do primeiro vídeo:", thumbnail_url)


