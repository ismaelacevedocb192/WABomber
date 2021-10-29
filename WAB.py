from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome('chromedriver')
lista = pd.read_excel("ListaDestinatarios.xlsx")

driver.get("https://web.whatsapp.com")
desselecciona = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[3]/label/input')
desselecciona.click()
input("Presiona cualquier tecla para continuar")

for linea in range(len(lista)):
    driver.get(f'https://web.whatsapp.com/send?phone=+52{lista["Número"][linea]}')
    time.sleep(10)
    text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
    text_box.click()
    text_box.send_keys(lista["Mensaje"][linea]+Keys.ENTER)

driver.close()
driver.quit()