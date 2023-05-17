# Importe as bibliotecas necessárias
from selenium import webdriver
import time

# Inicie o driver do Selenium para o Edge
driver = webdriver.Edge()

# Abra algumas abas
driver.get("https://www.google.com")
driver.execute_script("window.open('https://www.python.org')")
driver.execute_script("window.open('https://www.youtube.com')")

# Aguarde alguns segundos para que as páginas sejam carregadas
time.sleep(3)

# Alterne o foco para cada aba e obtenha as URLs
urls = []
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    urls.append(driver.current_url)

# Imprima as URLs
print(urls)

# Encerre o driver
driver.quit()
