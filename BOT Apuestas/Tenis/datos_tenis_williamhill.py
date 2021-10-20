from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(
    ChromeDriverManager().install(), options=options)
browser.get(
    "https://sports.williamhill.es/betting/es-es/tenis/partidos/competici%C3%B3n/hoy")
time.sleep(0.5)


def datos_tenis_williamhill():

    SCROLL_PAUSE_TIME = 0.8

    try:
        # Get scroll height
        last_height = browser.execute_script(
            "return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = browser.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        partidos = browser.find_elements_by_class_name("event")

        partidos_dict = {}
        for partidin in partidos:
            partido = BeautifulSoup(
                partidin.get_attribute('innerHTML'), 'html.parser')

            equipos = partido.find('div', attrs={
                'class': "btmarket__link-name btmarket__link-name--ellipsis show-for-desktop-medium"}).text.replace("                        ", "").replace(" v ", " - ").replace("                   ", "").replace("\n ", "")

            cuotas = partido.find_all(
                'div', attrs={'class': 'btmarket__selection'})

            cuotas = [cuota.text[:-1] for cuota in cuotas]

            partidos_dict[equipos] = cuotas
    except:
        print("William Hill ha fallado")

    # for [key, value] in partidos_dict.items():
    #     print(key+': '+f'{value}')

    browser.quit()

    return partidos_dict
