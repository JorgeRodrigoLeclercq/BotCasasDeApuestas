from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")
# Hay que tener cuidado con la version del ChromeDriver que instalas,
# a mi me dio problemas y tuve que cambiar de la de 83 a 81

# Con esto buscamos el elemento de la página que es Sign in:
signin_link = browser.find_element_by_link_text("Sign in")
# Con esto hacemos que se clique el botón de Sign in:
signin_link.click()

# Ahora queremos rellenar el hueco de Sign in, en este caso localizamos ese
# elemento mediante su id ya que es único en toda la página, este id lo encontramos
# al hacer click derecho e inspeccionar y donde ponga id = ...

username_box = browser.find_element_by_id("login_field")
# Este comando rellena el hueco con lo que escribas:
username_box.send_keys("soytricker")

# Hacemos lo mismo con el hueco de password:
password_box = browser.find_element_by_id("password")
password_box.send_keys("SonsOfAguirre86")
password_box.submit()

# Hasta aquí ya nos habríamos logeado y todo, ahora queremos comprobar si todo ha salido bien
assert "soytricker" in browser.page_source
# Esto es específico de github, lo que hacemos es ver si la paabra soytricker (nuestro nombre de usuario)
# aparece en la página en la que estamos lo que significaría que todo ha salido bien y que estamos logeados

# Como vemos, si ponemos un nombre de usuario que no sea el nuestro, al comprobar si está de una exception

browser.quit()  # Para cerrarlo
