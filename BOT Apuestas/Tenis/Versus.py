import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://apuestasdeportivas.versus.es/sports/tennis/competitions")

time.sleep(2)

def datos_tenis_versus():
    driver.maximize_window()

    time.sleep(5)

    competicionesBarra = driver.find_element_by_class_name("ButtonBar")
    competiciones = competicionesBarra.find_elements_by_xpath("//button")

    partidos_dict = {}

    for competicion in competiciones:

        competicion.click()

        time.sleep(3)

        seccionesAbiertas = driver.find_elements_by_class_name("ta-expanded")

        for seccionAbierta in seccionesAbiertas:
            boton = seccionAbierta.find_element_by_class_name("ta-Button")
            boton.click()

            time.sleep(1)

        seccionesCerradas = driver.find_elements_by_class_name("ta-collapsed")

        for seccionCerrada in seccionesCerradas[::-1]:
            seccionCerrada.click()

            time.sleep(1)

        partidos = driver.find_elements_by_class_name("EventListItem")

        for partido in partidos:

            equipos = partido.find_element_by_class_name("ta-Participants").text.split("\n")

            cuotas = partido.find_elements_by_class_name("ta-price_text")

            if len(cuotas) >= 2:
                cuota1 = cuotas[0].text
                cuota2 = cuotas[1].text
                partidos_dict[equipos[0] + ' - ' + equipos[1]] = [cuota1, cuota2]

    return partidos_dict






