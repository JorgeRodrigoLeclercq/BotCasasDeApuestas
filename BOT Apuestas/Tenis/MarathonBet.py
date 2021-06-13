import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.marathonbet.es/es/popular/Tennis+-+2398?interval=ALL_TIME")

time.sleep(2)

def datos_tenis_marathonBet():

    driver.maximize_window()

    time.sleep(5)

    partidos = driver.find_elements_by_class_name("sub-row")

    partidos_dict = {}

    for partido in partidos:

        equipos = partido.find_elements_by_class_name("member-link")
        equipo1 = equipos[0].text
        equipo2 = equipos[1].text

        cuotas = partido.find_elements_by_class_name("selection-link")
        cuota1 = cuotas[0].text
        cuota2 = cuotas[1].text

        partidos_dict[equipo1 + ' - ' + equipo2] = [cuota1, cuota2]

        return partidos_dict

















