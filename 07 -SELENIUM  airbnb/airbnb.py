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


site = BeautifulSoup(navegador.page_source, 'html.parser')

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

