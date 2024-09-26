from selenium.webdriver.common.by import By


class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver

    def search_result(self):
        return self.driver.find_element(By.XPATH, "//div[@id='result-stats']")