import pickle
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# Ejercicio de Esperas:
class Test3(unittest.TestCase):

    def setUp(self):
        navegador = '2'  # input('Elija navegador: 1-Firefox 2-Chrome: ')
        if navegador == '1':
            self.driver = webdriver.Firefox(executable_path=r'C:\selenium_drivers\firefox\geckodriver.exe')
        else:
            self.driver = webdriver.Chrome(executable_path=r'C:\selenium_drivers\chrome\chromedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('http://www.google.es')
        driver.implicitly_wait(10)

        # Añadimos las cookies necesarias para que no pida que las aceptemos
        doc = open("cookies.pkl", "rb")
        cookies = pickle.load(doc)
        for cookie in cookies:
            driver.add_cookie(cookie)
        doc.close()

        # Por si tuvieramos que guardar las cookies, se incluye esta instrucción y se comenta la carga de cookies
        # pra que se genere el documento con las cookies, y volvemos a ejecutar con esta instrucción comentada
        # y la de cargar cookies descomentada
        # doc = open("cookies.pkl", "wb")
        # pickle.dump(driver.get_cookies(), doc)
        # doc.close()

        # Recargamos con las cookies
        driver.refresh()

        # Esperamos a que el campo “Buscar” sea visible
        print('Esperamos a que el campo “Buscar” sea visible ...')
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        print('Listo!')

        # Le decimos que en el campo seleccionado escriba: "Buscar”
        element.send_keys('Buscar')

        # Esperamos a que el botón “Buscar en Google” sea cliclable
        print('Esperamos a que el botón “Buscar en Google” sea cliclable ...')
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@value="Buscar con Google"]')))
        print('Listo!')

        # Pulsar el botón “Buscar en Google"
        element.click()

        # Esperamos a que se muestre el enlace “Siguiente” de la paginación de los resultados

        print('Esperamos a que se muestre el enlace “Siguiente” de la paginación de los resultado ...')
        click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Siguiente')))
        print('Listo!')

        # Pulsar el enlace “Siguiente”
        click.click()

        # Esperamos 2 segundos
        print('Esperamos 2 segundos')
        sleep(2)
        print('Hemos esperado')

        # Pulsar la opción de menú “Herramientas”
        opherramientas = driver.find_element_by_xpath('//*[@id="hdtb-tls"]')
        opherramientas.click()
        # Esperar a que se muestre la opción “Todos los resultados” y lo pulsamos
        try:
            print('Esperamos a que se muestre la opción “Todos los resultados" ...')
            todosres = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="hdtbMenus"]/div/span[4]')))
            sleep(2)
            todosres.click()
            print('Listo!')
        except Exception as e:
            print(e)
            print('ERROR DALE A MANO!!!!!')
            sleep(5)

        # Pulsar en la opción “Verbatim”
        print('Pulsamos en la opción "Verbatim"')
        verbatim = driver.find_element_by_link_text('Verbatim')
        verbatim.click()
        print('Listo!')
        sleep(2)

    def tearDown(self):
        print('fin')
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
