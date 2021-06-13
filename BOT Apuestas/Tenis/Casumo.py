import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.casumo.es/sports#filter/tennis")

time.sleep(2)

def datos_tenis_casumo():
    driver.maximize_window()

    time.sleep(5)

    seccionesAbiertas = driver.find_elements_by_class_name("HmVrK")

    for seccionAbierta in seccionesAbiertas:
        seccionAbierta.click()

    time.sleep(5)

    background = driver.find_element_by_xpath("//body")

    for i in range(3):
        background.send_keys(Keys.ARROW_DOWN)
        background.send_keys(Keys.ARROW_DOWN)

    time.sleep(5)
    seccionesCerradas = driver.find_elements_by_class_name("jepkPT")

    for seccionCerrada in seccionesCerradas[::-1]:
        seccionCerrada.click()

    time.sleep(3)

    apartadoAbiertoLive = driver.find_element_by_class_name("KambiBC-betoffer-labels")
    apartadoAbiertoLive.click()

    time.sleep(3)

    Live = driver.find_element_by_class_name("sc-fzoLag")
    apartadosCerradosLive = Live.find_elements_by_class_name("KambiBC-betoffer-labels")

    for apartadoCerradoLive in apartadosCerradosLive[::-1]:
        apartadoCerradoLive.click()

    partidos_dict = {}

    time.sleep(3)

    partidos = driver.find_elements_by_class_name("KambiBC-event-item__event-wrapper")

    for partido in partidos:
        equipos = partido.find_elements_by_class_name("KambiBC-event-participants__name")
        equipo1 = equipos[0].text
        equipo2 = equipos[1].text
        cuotas = partido.find_elements_by_class_name("golQFD")

        if len(cuotas) >= 2:
            cuota1 = cuotas[0].text
            cuota2 = cuotas[1].text
            partidos_dict[equipo1 + ' - ' + equipo2] = [cuota1, cuota2]

    return partidos_dict