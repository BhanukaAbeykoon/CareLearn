import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "name")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/button")

    def login(self, username, password):
        self.driver.get("https://demo5.caresystemsinc.com/demo5/html_interface/login.jsp")
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        time.sleep(4)
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            pass

        WebDriverWait(self.driver, 100).until(
            EC.url_to_be("https://demo5.caresystemsinc.com/demo5/html_interface/manager/desktop.jsp"))
