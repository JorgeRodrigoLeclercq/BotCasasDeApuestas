
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def datos_futbol_betfair():
    browser = webdriver.Chrome(options=options)
    browser.get("https://www.betfair.es/sport/inplay")

    time.sleep(5)

    # Nos quitamos el botón de las cookies:
    try:
        cookies = browser.find_element_by_id("onetrust-accept-btn-handler")
        cookies.click()
    except:
        pass

    # Estos son los live:
    partidos_live = {}
    try:
        live = browser.find_element_by_class_name(
            "section-list")

        # Cogemos toda la lista de partidos:
        partidos = BeautifulSoup(
            live.get_attribute('innerHTML'), 'html.parser')

        # Cada partido:
        partidos_bak = partidos.find_all(
            'li', attrs={'class': 'com-coupon-line avb-row market-1x2 large'})

        for partido in partidos_bak:
            # El nombre de los equipos (usamos las funciones anónimas lambda para coger clases que empiecen por una string ya que hay casos donde le meten una id única a cada clase y queremos coger por ejemplo todas las clases que empiecen con event-name):
            equipos = partido.find('div',
                                   attrs={'class': lambda e: e.startswith('event-name-info ui-market') if e else False}).find_all('span', attrs={'class': lambda e: e.endswith('team-name') if e else False})

            equipos = equipos[0].text.replace(
                "\n", "") + ' - ' + equipos[1].text.replace("\n", "")

            # Las cuotas:
            cuotas = []
            for ultag in partido.find_all('ul', {'class': 'runner-list-selections'}):
                for litag in ultag.find_all('li'):
                    if litag.text != '\n':
                        cuotas.append(litag.text.replace("\n", ""))

            partidos_live[equipos] = cuotas
    except:
        pass

    # for [key, value] in partidos_live.items():
    #     print(key+' : '+f'{value}')

    # Los próximos partidos:
    proximos = browser.find_element_by_class_name("events-body")

    lista_proximos = [[]]
    contador = 1
    contador_lista = 0
    for dato in proximos.text.split("\n"):
        if dato != "Irá A En Juego" and dato != "En Directo" and dato != "SUSPENDIDO" and dato != "En TV" and dato != "En directo":
            if contador % 4 != 0:
                lista_proximos[contador_lista].append(dato)
                contador += 1
            else:
                lista_proximos[contador_lista].append(dato)
                contador_lista += 1
                contador = 1
                lista_proximos.append([])

    partidos_proximos = {}
    for lista in lista_proximos:
        try:
            if lista:
                partidos_proximos[lista[3]
                                  [:-6].replace(" Mañana", "")] = lista[0:3]
        except:
            pass

    # for [key, value] in partidos_proximos.items():
    #     print(key+': '+f'{value}')
    browser.quit()

    return {**partidos_live, **partidos_proximos}
