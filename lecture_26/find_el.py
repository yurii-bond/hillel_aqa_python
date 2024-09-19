from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.maximize_window()
driver.get("http://localhost:8080/lecture_26/find_el.html")

# Знаходження елемента за ID
user_field = driver.find_element(By.ID, "username")
pass_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login_button")

# Знаходження елемента за XPath
user_field = driver.find_element(By.XPATH, "//input[@id='username']")
pass_field = driver.find_element(By.XPATH, "//input[@id='password']")
login_button = driver.find_element(By.XPATH, "//button[@id='login_button']")

# Знаходження елемента за CSS класом
user_field = driver.find_element(By.CSS_SELECTOR, ".input-field#username")
pass_field = driver.find_element(By.CSS_SELECTOR, ".input-field#password")
login_button = driver.find_element(By.CSS_SELECTOR, "#login_button")

# Знаходження елемента за назвою тегу
form_element = driver.find_element(By.TAG_NAME, "form")


# Знаходження елемента за XPath з вказанням значення
li_el2 = driver.find_element(By.XPATH, "//li[.='Елемент списку 2']")

# Знаходження елемента за XPath з вказанням iндексу
li_el2_idx = driver.find_element(By.XPATH, "//li[2]")

# Знаходження всіх елементів з тегом <li>
li_elements = driver.find_elements(By.TAG_NAME, "li")

# Пошук конкретного елемента серед отриманих
for li in li_elements:
    # пошук може бути повiльним якщо елементiв багато
    if li.text == "Елемент списку 2":
        # Знайдено потрібний елемент
        print("Знайдено елемент:", li.text)
        break

sleep(2)