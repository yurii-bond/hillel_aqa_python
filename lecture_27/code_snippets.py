from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def webelement(driver, locator: tuple[str, str]):
    try:
        element = WebDriverWait(driver, timeout=5).until(
            EC.presence_of_element_located(locator)
        )
        return element
    except TimeoutException:
        print("За даний час елемент не зявився на сторінці")

def element_is_not_here(driver, xpath):
    try:
        WebDriverWait(driver, timeout=5).until_not(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return True
    except TimeoutException:
        print("Елемент продовжує бути на сторінці після очікуваного часу")
        return False

# Ініціалізуємо драйвер браузера
driver = webdriver.Chrome()
driver.get("https://www.example.com")
xpath = '//li[@id="ewuygeb"]'
xpath_locator = (By.XPATH, xpath)
if element_is_not_here(driver, xpath):
    print('All is well!')
element = webelement(driver, xpath_locator)
element.click()
# Закриття браузера
driver.quit()