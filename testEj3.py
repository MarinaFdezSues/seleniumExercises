import pickle
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Ejercicio de Esperas:
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


class PythonOrgSearch(unittest.TestCase):

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
        # Y le decimos que busque el campo llamado 'q' -> El campo de Buscar
        ## element = wait.until(EC._find_element(By.NAME('q')))
        # WebDriverWait(driver, timeout=3).until(some_condition)
        try:
            print('Esperamos a que el campo “Buscar” sea visible ...')
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
            print('Listo!')
        except:
            print('ERROR!!!!!')

        # Le decimos que en el campo seleccionado escriba: "Buscar”
        element.send_keys('Buscar')

        # Esperamos a que el botón “Buscar en Google” sea cliclable
        # Y buscamos el botón 'Buscar en Google' con xpath
        try:
            print('Esperamos a que el botón “Buscar en Google” sea cliclable ...')
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@value="Buscar con Google"]')))
            print('Listo!')
        except:
            print('ERROR!!!!!')
        # Pulsar el botón “Buscar en Google"
        element.click()


        # Esperamos a que se muestre el enlace “Siguiente” de la paginación de los resultados
        #click = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Siguiente')))
        try:
            print('Esperamos a que se muestre el enlace “Siguiente” de la paginación de los resultado ...')
            click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Siguiente')))
            print('Listo!')
        except:
            print('ERROR!!!!!')

        # Pulsar el enlace “Siguiente”
        click.click()

        # Esperamos 2 segundos
        print('Esperamos 2 segundos+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        sleep(2)
        print('Hemos esperado++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

        # Pulsar la opción de menú “Herramientas”
        # //*[@id="hdtb-tls"]
        opherramientas = driver.find_element_by_xpath('//*[@id="hdtb-tls"]')
        opherramientas.click()
        # Esperar a que se muestre la opción “Todos los resultados”
        # Y lo pulsamos
        try:
            print('Esperamos a que se muestre la opción “Todos los resultados" ...')
            todosres = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hdtbMenus"]/div/span[4]')))
            sleep(2)
            todosres.click()
            print('Listo!')
        except Exception as e:
            print(e)
            print('ERROR DALE A MANO!!!!!')
            sleep(5)


        # Pulsar en la opción “Verbatim”
        verbatim = driver.find_element_by_link_text('Verbatim')
        verbatim.click()
        sleep(5)



    def tearDown(self):
        print('fin')
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
