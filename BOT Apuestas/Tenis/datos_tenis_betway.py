import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


browser = webdriver.Chrome(
    ChromeDriverManager().install(), options=options)
browser.get("https://betway.es/es/sports/cpn/tennis/231")
time.sleep(3)


def datos_tenis_betway():

    try:
        # Hay que hacer esto para que pinche bien sobre el botón al cambiar de tipo de partido:
        html = browser.find_element_by_tag_name('html')
        html.send_keys(Keys.ARROW_DOWN)
        html.send_keys(Keys.ARROW_DOWN)
        html.send_keys(Keys.ARROW_DOWN)
        html.send_keys(Keys.ARROW_DOWN)

        # ATP:

        elements = browser.find_elements_by_class_name('oneLineEventItem')

        partidos_dict = {}
        for element in elements:
            equipos = element.find_elements_by_class_name('teamName')
            equipo1 = equipos[0].text[:-1].replace("● ", "")
            equipo2 = equipos[1].text.replace(" ●", "")

            cuotas = element.find_element_by_class_name(
                "eventMarket").text.split("\n")

            if cuotas != ["Cancelado"]:
                partidos_dict[equipo1 + '- '+equipo2] = cuotas

        # WTA:

        botones = browser.find_elements_by_class_name(
            "contentSelectorItemButton")
        botones[-2].click()

        time.sleep(1)

        elements = browser.find_elements_by_class_name('oneLineEventItem')

        for element in elements:
            equipos = element.find_elements_by_class_name('teamName')
            equipo1 = equipos[0].text[:-1].replace("● ", "")
            equipo2 = equipos[1].text.replace(" ●", "")

            cuotas = element.find_element_by_class_name(
                "eventMarket").text.split("\n")

            if cuotas != ["Cancelado"]:
                partidos_dict[equipo1 + '- '+equipo2] = cuotas

        # Challenger:
        botones = browser.find_elements_by_class_name(
            "contentSelectorItemButton")
        botones[-1].click()
        time.sleep(1)

        elements = browser.find_elements_by_class_name('oneLineEventItem')

        for element in elements:
            equipos = element.find_elements_by_class_name('teamName')
            equipo1 = equipos[0].text[:-1].replace("● ", "")
            equipo2 = equipos[1].text.replace(" ●", "")

            cuotas = element.find_element_by_class_name(
                "eventMarket").text.split("\n")

            if cuotas != ["Cancelado"] and '-' not in cuotas:
                partidos_dict[equipo1 + '- '+equipo2] = cuotas

    except:
        print("Betway ha fallado")

    browser.quit()

    return partidos_dict
