from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.wikipedia.org/")

# Encontramos el elemento de la barra de búsqueda:
search = browser.find_element_by_id("searchInput")
# Le metemos el input:
search.send_keys("Bad Bunny")
# Presionamos la leta Enter para buscar:
search.send_keys(Keys.RETURN)

time.sleep(5)
# Cerramos el browser:
browser.quit()
