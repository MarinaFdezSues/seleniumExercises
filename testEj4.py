import pickle
import unittest
from time import sleep
from selenium import webdriver
import testPOM


# Ejercicios con Page Object:
class Test4(unittest.TestCase):

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

        sleep(2)

    def tearDown(self):
        print('fin')
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
