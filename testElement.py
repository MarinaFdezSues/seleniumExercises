from selenium.webdriver.support.ui import WebDriverWait


# Ejercicios con Page Object:
class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    # Página base

    def __set__(self, obj, txt):
        """Sets the text to the value supplied"""
        # Establece el texto proporcionado en txt.

        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda idriver: idriver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(txt)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        # Toma el texto de un objeto dado.

        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda idriver: idriver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
