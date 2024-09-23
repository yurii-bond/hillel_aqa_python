import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    # Ініціалізація драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()