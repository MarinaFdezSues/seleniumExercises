from testElement import BasePageElement
from testLocator import MainPageLocators


# Ejercicios con Page Object:
class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""
    # Esta clase recibe el texto de búsqueda del localizador específico

    # The locator for search box where search string is entered
    # El localizador para el cuadro de búsqueda donde se ingresa una cadena de búsqueda.

    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    # Clase de página base que se inicializa en cada clase de objeto de página.

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""
    # Los métodos de acción de la página de inicio van aquí.

    # Declares a variable that will contain the retrieved text
    # Se declara una variable que contendrá el texto recuperado.

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        # Verificia que el texto codificado en Py aparezca en el título.
        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        # Activa la búsqueda
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    # Los métodos de acción de la página de resultados de búsqueda van aquí.

    def is_results_found(self):
        # Probably should search for this text in the specific page element, but as for now it works fine
        # De momento se queda así
        return "No results found." not in self.driver.page_source
