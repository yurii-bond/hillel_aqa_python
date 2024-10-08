from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CustomCondition:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            element = driver.find_element(*self.locator)  # Знаходимо елемент
            return element.is_displayed()  # Перевіряємо, чи елемент відображається
        except:
            return False  # Якщо елемент не знайдено або не відображається, повертаємо False

# Приклад використання
driver.get("<http://example.com>")
wait = WebDriverWait(driver, 10)

# Очікувати, поки елемент із заданим CSS селектором не буде видимим
element = wait.until(CustomCondition((By.CSS_SELECTOR, "div.some-class")))

# Потім працюємо з елементом
element.click()