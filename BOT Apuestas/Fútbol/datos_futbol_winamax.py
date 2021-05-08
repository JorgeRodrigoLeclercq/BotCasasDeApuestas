
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def datos_futbol_winamax():
    browser = webdriver.Chrome(options=options)
    browser.get("https://www.winamax.es/apuestas-deportivas/sports/1")
    time.sleep(5)

    # # Hacemos esto para que baje hasta abajo de la página porque si no no coge todos los partidos porque no se cargan
    # background = browser.find_element_by_xpath("//body")
    # background.click()
    # for i in range(25):
    #     background.send_keys(Keys.PAGE_DOWN)
    #     time.sleep(0.7)

    partidos = BeautifulSoup(browser.find_element_by_class_name(
        "iFsfAp").get_attribute('innerHTML'), 'html.parser').find_all(
        'a', attrs={'class': lambda e: e.endswith('hRjAwS') if e else False})

    partidos_dict = {}
    for partido in partidos:
        try:
            equipos = partido.find_all(
                'div', attrs={'class': 'sc-eOuESm dxvkAc'})
            equipo1 = equipos[0].text
            equipo2 = equipos[1].text

            cuotas = partido.find_all(
                'div', attrs={'class': 'sc-bJydzv bqtKXY'})
            cuotas = [cuota.text[:-1].replace("--", "0") for cuota in cuotas]

            if "Más de" not in cuotas[0] and cuotas != ['0', '0', '0']:
                partidos_dict[equipo1 + ' - ' + equipo2] = cuotas
        except:
            pass

    # for [key, value] in partidos_dict.items():
    #     print(key+': '+f'{value}')

    browser.quit()

    return partidos_dict
