from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(options=options)
browser.get("https://sports.bwin.es/es/sports/tenis-5/apuestas")


def datos_tenis_bwin():

    # Ahora ya vamos a coger todos los partidos:
    main = BeautifulSoup(browser.find_elements_by_class_name(
        'column-wrapper')[1].get_attribute('innerHTML'), 'html.parser')

    partidos_live = main.find_all('div', attrs={'class': 'grid-event-wrapper'})

    partidos_dict = {}
    try:
        for partido in partidos_live:
            equipos = partido.find_all(
                'div', attrs={'class': 'participant-wrapper ng-star-inserted'})

            # Hay que poner el .strip(" ") para quitar el hueco que deja al final
            equipo1 = equipos[0].text.strip(
                " ")[:-3] if (equipos[0].text[0]) == " " else equipos[0].text[-3:-1]
            equipo2 = equipos[1].text.strip(
                " ")[:-3] if (equipos[1].text[0]) == " " else equipos[1].text[-3:-1]

            equipos_bak = equipo1.replace(
                "/", " / ") + ' - ' + equipo2.replace("/", " / ")

            cuotas = partido.find_all(
                'ms-option', attrs={'class': 'grid-option ng-star-inserted'})[0:2]

            cuotas = [cuota.text for cuota in cuotas]
            for cuota in cuotas:
                if cuota == "":
                    cuotas[cuotas.index(cuota)] = "0"

            if cuotas and len(cuotas) == 2:
                partidos_dict[equipos_bak.replace("Reserves", "")] = cuotas
    except:
        pass

    browser.quit()

    return partidos_dict

    # for [key, value] in partidos_dict.items():
    #     print(key+': '+f'{value}')
