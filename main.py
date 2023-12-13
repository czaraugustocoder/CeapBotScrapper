from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import re
from datetime import date

servico = Service(ChromeDriverManager().install())

opcoes = webdriver.ChromeOptions()

#opcoes.add_argument("--headless")

navegador = webdriver.Chrome(service=servico, options=opcoes)
print("conectando ao serviço")

navegador.get('https://www.aleam.gov.br/transparencia/controle-de-cota-parlamentar/')

time.sleep(10)

mes = Select(navegador.find_element(By.ID, "mes"))

time.sleep(5)

mes.select_by_visible_text('Junho')
print("clicou no mês")

time.sleep(5)

deputado = Select(navegador.find_element(By.ID, "dados"))

time.sleep(5)

deputado.select_by_visible_text('Abdala Fraxe')
print("clicou no nome")

time.sleep(5)

botton = navegador.find_element(By.XPATH, '/html/body/div[2]/section[2]/div/div/div/div/div/div/div[1]/form/div/button')
# clicando em um botão
botton.click()
print("clicou no botão com sucesso")

time.sleep(10)

pagina_html = BeautifulSoup(navegador.page_source,'html.parser')
print(pagina_html)

input()