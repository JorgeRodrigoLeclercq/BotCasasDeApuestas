from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.betfair.es/")

time.sleep(2)

# Nos quitamos el botón de las cookies:
cookies = browser.find_element_by_id("onetrust-accept-btn-handler")
cookies.click()

# El hueco del correo:
correo = browser.find_element_by_id("ssc-liu")
correo.send_keys("andresmireles2001@gmail.com")

# El hueco de la contraseña:
contraseña = browser.find_element_by_id("ssc-lipw")
contraseña.send_keys("eyquetal")

# El botón para iniciar sesión:
boton_login = browser.find_element_by_id("ssc-lis")
boton_login.click()

time.sleep(2)
browser.quit()
