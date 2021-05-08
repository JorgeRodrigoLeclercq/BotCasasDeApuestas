from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://betway.es/es/sports")

time.sleep(5)
# Con esto buscamos el elemento de la página que es Sign in:
signin_link = browser.find_element_by_link_text(
    "¿Olvidaste tu nombre de usuario?")
# Con esto hacemos que se clique el botón de Sign in:
signin_link.click()
