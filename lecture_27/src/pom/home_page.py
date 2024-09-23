from lecture_27.src.pom.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.url_path = super().url + '/login_page'



