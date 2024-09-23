from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://"

    def find_element(self, driver, locator: tuple[str, str]) -> WebElement:
        """Функція для очікування наявності елемента на сторінці"""
        try:
            element = WebDriverWait(driver, timeout=5).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise NoSuchElementException("За даний час елемент не зявився на сторінці")