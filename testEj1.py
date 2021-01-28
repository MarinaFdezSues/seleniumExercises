import pickle
import unittest
from time import sleep

from selenium import webdriver

# Ejercicio de Navegación
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

        # Le decimos que busque e campo llamado 'q' -> El campo de Buscar
        element = driver.find_element_by_name('q')

        # Por si tuvieramos que guardar las cookies, se incluye esta instrucción y se comenta la carga de cookies
        # pra que se genere el documento con las cookies, y volvemos a ejecutar con esta instrucción comentada
        # y la de cargar cookies descomentada
        # doc = open("cookies.pkl", "wb")
        # pickle.dump(driver.get_cookies(), doc)
        # doc.close()

        # Le decimos que en el campo seleccionado escriba: 'Buscar”'
        element.send_keys('Buscar')

        # Le damos a buscar
        driver.find_element_by_name('btnK').click()

        # Recogemos en una lista los resultados y los imprimimos
        results = driver.find_elements_by_class_name('g')
        i = 0
        for r in results:
            i += 1
            print(i, ' - ', r)
        print()
        # Seleccionamos el enlace de 'Noticias'
        noticias = driver.find_element_by_link_text('Noticias')
        noticias.click()
        # Buscamos  los resultados y accedemos al 2º
        rnoticias = driver.find_elements_by_class_name('dbsr')

        click = rnoticias[2].find_element_by_partial_link_text('')
        click.click()

        sleep(1)

        cookies = driver.get_cookies()
        for c in cookies:
            # domain, name, value
            print(f'Dominio: {c["domain"]} - Nombre: {c["name"]} - Valor: {c["value"]}')

    def tearDown(self):
        print('fin')
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
