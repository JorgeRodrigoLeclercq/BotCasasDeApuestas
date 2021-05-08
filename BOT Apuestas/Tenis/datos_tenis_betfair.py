
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def datos_tenis_betfair():

    browser = webdriver.Chrome(options=options)
    browser.get("https://www.betfair.es/sport/tennis")

    time.sleep(1)

    # Nos quitamos el botón de las cookies:
    try:
        cookies = browser.find_element_by_id("onetrust-accept-btn-handler")
        cookies.click()
    except:
        pass

    partidos_dict = {}
    try:
        live = browser.find_element_by_class_name(
            "section-list")

        # Cogemos toda la lista de partidos:
        partidos = BeautifulSoup(
            live.get_attribute('innerHTML'), 'html.parser')

        # Cada partido:
        partidos_bak = partidos.find_all(
            'div', attrs={'class':
                          lambda e: e.startswith('event-information ui') if e else False}
        )

        for partido in partidos_bak:
            # El nombre de los equipos (usamos las funciones anónimas lambda para coger clases que empiecen por una string ya que hay casos donde le meten una id única a cada clase y queremos coger por ejemplo todas las clases que empiecen con event-name):
            equipos = partido.find_all('span', attrs={'class': 'team-name'})

            equipos = equipos[0].text.replace(
                "\n", "").replace("• ", "") + ' - ' + equipos[1].text.replace("\n", "").replace("• ", "")

            # Las cuotas:
            cuotas = []
            for ultag in partido.find_all('ul', {'class': 'runner-list-selections'}):
                for litag in ultag.find_all('li'):
                    if litag.text != '\n':
                        cuotas.append(litag.text.replace("\n", ""))

            partidos_dict[equipos] = cuotas
    except:
        pass

    # for [key, value] in partidos_live.items():
    #     print(key+' : '+f'{value}')

    browser.quit()
    return partidos_dict
