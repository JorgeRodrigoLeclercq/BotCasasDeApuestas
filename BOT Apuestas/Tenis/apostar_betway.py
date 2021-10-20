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


def apostar_betway(usuario, contraseña, partido, cuota, dinero):

    time.sleep(2)

    # Vamos a quitar las cookies:
    browser.find_element_by_class_name("cookiePolicyAcceptButton").click()

    # Iniciamos sesión:
    us = browser.find_element_by_class_name("loginInputs").find_element_by_class_name(
        "usernameInput").find_element_by_css_selector("input")
    us.send_keys(usuario)

    con = browser.find_element_by_class_name("loginInputs").find_element_by_class_name(
        "passwordInput").find_element_by_css_selector("input")
    con.send_keys(contraseña)

    browser.find_element_by_class_name("submitButton").click()

    # Hacemos un ajuste:
    cuota = str(cuota).replace(".", ",")
    if len(cuota.split(",")[1]) == 1:
        cuota = cuota + "0"
    print(cuota)

    # Hay que hacer esto para que pinche bien sobre el botón al cambiar de tipo de partido:
    html = browser.find_element_by_tag_name('html')

    partido_apostar = None

    # Miramos si el partido está en el ATP:
    elements = browser.find_elements_by_class_name('oneLineEventItem')

    for elemento in elements:
        equipos = elemento.find_elements_by_class_name('teamName')
        equipo1 = equipos[0].text[:-1].replace("● ", "")
        equipo2 = equipos[1].text.replace(" ●", "")
        nombre = equipo1 + '- '+equipo2

        if nombre == partido:
            partido_apostar = elemento
            break

    # Si no lo ha encontrado nos movemos al WTA
    if not partido_apostar:

        botones = browser.find_elements_by_class_name(
            "contentSelectorItemButton")
        botones[-2].click()

        time.sleep(1)

        elements = browser.find_elements_by_class_name('oneLineEventItem')

        for elemento in elements:

            equipos = elemento.find_elements_by_class_name('teamName')
            equipo1 = equipos[0].text[:-1].replace("● ", "")
            equipo2 = equipos[1].text.replace(" ●", "")
            nombre = equipo1 + '- '+equipo2

            if nombre == partido:
                partido_apostar = elemento
                break

    # Si no lo ha encontrado nos movemos a Challenger:
    if not partido_apostar:

        botones = browser.find_elements_by_class_name(
            "contentSelectorItemButton")
        botones[-1].click()

        time.sleep(1)

        elements = browser.find_elements_by_class_name('oneLineEventItem')

        for elemento in elements:

            equipos = elemento.find_elements_by_class_name('teamName')
            equipo1 = equipos[0].text[:-1].replace("● ", "")
            equipo2 = equipos[1].text.replace(" ●", "")
            nombre = equipo1 + '- '+equipo2

            if nombre == partido:
                partido_apostar = elemento
                break

    # Si ha encontrado el partido entonces apostamos:
    if partido_apostar:
        cuotas = partido_apostar.find_elements_by_class_name("baseOutcomeItem")

        elemento_clickar = None
        for element in cuotas:
            if element.text == str(cuota).replace(".", ","):
                elemento_clickar = element

        elemento_clickar.click()

        time.sleep(1)

        hueco = html.find_element_by_class_name("stakeInput")
        hueco.send_keys(dinero)

    # browser.quit()
