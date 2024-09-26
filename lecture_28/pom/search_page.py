from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def search_field(self):
        return self.driver.find_element(By.ID, "APjFqb")

    def search_button(self):
        return self.driver.find_element(By.XPATH, "(//input[@class='gNO89b' and @name='btnK'])[2]")
