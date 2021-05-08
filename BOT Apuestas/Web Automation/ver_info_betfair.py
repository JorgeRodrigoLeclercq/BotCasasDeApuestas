from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.betfair.es/sport/inplay")

time.sleep(2)

# Nos quitamos el botón de las cookies:
cookies = browser.find_element_by_id("onetrust-accept-btn-handler")
cookies.click()

# Vamos a coger toda la lista de deportes:
deportes = browser.find_elements_by_class_name("ip-sport")
deportes_id = [deporte.id for deporte in deportes]

# Vamos a coger de cada deporte cada partido (vamos a hacerlo de momento para uno solo):
general = browser.find_elements_by_class_name(
    "details-event")

# Esto no funciona:
# for element in general:
#     print(''.join(element.text.replace("Irá A En Juego",
#                                        "").replace("En Directo", "").replace("Mañana", "").split(" "))[:-5])
#     print("\n")

print(general[0].get_attribute('innerHTML'))
# browser.quit()
