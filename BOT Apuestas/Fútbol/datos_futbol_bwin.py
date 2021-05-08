from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def datos_futbol_bwin():
    browser = webdriver.Chrome(options=options)
    browser.get("https://sports.bwin.es/en/sports/live/football-4")
    time.sleep(5)

    # Hacemos esto para que baje hasta abajo de la página porque si no no coge todos los partidos porque no se cargan
    background = browser.find_element_by_xpath("//body")
    background.click()
    for _ in range(25):
        background.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.7)

    # Ahora ya vamos a coger todos los partidos:
    main = BeautifulSoup(browser.find_element_by_class_name(
        'column-wrapper').get_attribute('innerHTML'), 'html.parser')

    partidos_live = main.find_all('div', attrs={'class': 'grid-event-wrapper'})

    partidos_dict = {}
    try:
        for partido in partidos_live:
            equipos = partido.find_all(
                'div', attrs={'class': 'participant-wrapper ng-star-inserted'})

            # Hay que poner el .strip(" ") para quitar el hueco que deja al final
            equipo1 = equipos[0].text.strip(
                " ") if (equipos[0].text[0]) == " " else equipos[0].text
            equipo2 = equipos[1].text.strip(
                " ") if (equipos[1].text[0]) == " " else equipos[1].text

            equipos_bak = equipo1 + ' - ' + equipo2

            cuotas = partido.find_all(
                'ms-option', attrs={'class': 'grid-option ng-star-inserted'})[0:3]

            cuotas = [cuota.text for cuota in cuotas]
            for cuota in cuotas:
                if cuota == "":
                    cuotas[cuotas.index(cuota)] = "0"

            if cuotas and len(cuotas) == 3:
                partidos_dict[equipos_bak.replace("Reserves", "")] = cuotas
    except:
        pass

    browser.quit()

    return partidos_dict

    # for [key, value] in partidos_dict.items():
    #     print(key+': '+f'{value}')


# Hay que hacer un scroll down para poder coger todos los partidos !!!
