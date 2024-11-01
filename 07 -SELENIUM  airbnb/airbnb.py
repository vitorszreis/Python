from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
options.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options=options)

navegador.get('https://www.airbnb.com')

sleep(2)

wait = WebDriverWait(navegador, 10)
campo_busca = wait.until(EC.element_to_be_clickable((By.ID, "bigsearch-query-location-input")))


campo_busca.send_keys("Rochester, NY")
campo_busca.send_keys(Keys.ENTER)

data_inicial = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='12/11/2024']")))
data_inicial.click()

data_final = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='16/11/2024']")))
data_final.click()

hospedes_div = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='structured-search-input-field-guests-button']"))
)
hospedes_div.click()

increase_guests_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="stepper-adults-increase-button"]'))
)
increase_guests_button.click()

search_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="structured-search-input-search-button"]'))
)
search_button.click()

sleep(5)

site = BeautifulSoup(navegador.page_source, 'html.parser')

listings = site.find_all('div', {'class': 'g1qv1ctd'})
for listing in listings:

    titulo = listing.find('div', {'data-testid': 'listing-card-title'})
    titulo_texto = titulo.get_text(strip=True) if titulo else 'Título não encontrado'

    descricao = listing.find('div', {'data-testid': 'listing-card-subtitle'})  
    descricao_texto = descricao.get_text(strip=True) if descricao else 'Descrição não encontrada'

    preco = listing.find('span', {'class': '_11jcbg2'})  
    preco_texto = preco.get_text(strip=True) if preco else 'Preço não encontrado'

    print(f"Título: {titulo_texto}")
    print(f"Descrição: {descricao_texto}")
    print(f"Preço por noite: {preco_texto}")
    print("----------")
