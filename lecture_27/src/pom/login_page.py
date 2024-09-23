from lecture_27.src.pom.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url_path = super().url + '/login_page'

    
