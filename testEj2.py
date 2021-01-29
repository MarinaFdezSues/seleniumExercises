import pickle
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


# Ejercicio de Localización de Elementos:
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
        driver.implicitly_wait(1)

        # Añadimos las cookies necesarias para que no pida que las aceptemos
        doc = open("cookies.pkl", "rb")
        cookies = pickle.load(doc)
        for cookie in cookies:
            driver.add_cookie(cookie)
        doc.close()

        # Recargamos con las cookies
        driver.refresh()

        # Le decimos que busque el campo llamado 'q' -> El campo de Buscar
        element = driver.find_element_by_name('q')

        # Por si tuvieramos que guardar las cookies, se incluye esta instrucción y se comenta la carga de cookies
        # pra que se genere el documento con las cookies, y volvemos a ejecutar con esta instrucción comentada
        # y la de cargar cookies descomentada
        # doc = open("cookies.pkl", "wb")
        # pickle.dump(driver.get_cookies(), doc)
        # doc.close()

        # Le decimos que en el campo seleccionado escriba: 'Buscar”'
        element.send_keys('Buscar')

        # Buscamos el botón 'Buscar en Google' con xpath
        # div/form/div/div/div/center/input value ="Buscar con Google"
        element = driver.find_element_by_xpath('//input[@value="Buscar con Google"]')
        # print(element)
        element.click()
        sleep(1)

        # Almacenamos na lista de los resultados de la página 1
        results = driver.find_elements_by_class_name('g')
        sleep(1)

        # Pulsar en la Página 2 localizando el elemento mediante el nombre de la clase
        click = driver.find_element_by_xpath('//a[@aria-label="Page 2"]')
        click.click()

        print('Imprimimos el 1º de los resultados guardados')
        print(results[0])

        # Ir al primer resultado mostrado en el punto anterior
        # driver.back() da error
        click = driver.find_element_by_link_text('Anterior')
        click.click()

        # Solo encontrará el 1º:
        resultados = driver.find_elements_by_class_name('g')
        click = resultados[0].find_element_by_partial_link_text('')
        click.click()
        sleep(1)

        # Localizar un elemento mediante el selector CSS y mostrar el tipo del elemento
        # driver.find_element_by_css_selector("a[data-planId='31']")
        csselem = driver.find_element_by_css_selector('p.n2')
        print('Elemento por css:')
        print(csselem)
        print('Tipo:', csselem.tag_name)
        sleep(1)

        # Localizar un elemento mediante su identificador mostrar el tipo del elemento
        # id="conjugacion"
        idelem = driver.find_element_by_id('conjugacion')
        print('Elemento por id:')
        print('Tipo:', idelem.tag_name)
        sleep(1)

    def tearDown(self):
        print('fin')
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
