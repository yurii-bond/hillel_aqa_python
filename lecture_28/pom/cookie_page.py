from selenium import webdriver
from selenium.webdriver.common.by import By


class CookiePage:
    def __init__(self, driver):
        self.driver = driver

    def cookie_accept_button(self):
        return self.driver.find_element(By.ID, "L2AGLb")


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    driver.maximize_window()
    page = CookiePage(driver)
    page.cookie_accept_button().click()