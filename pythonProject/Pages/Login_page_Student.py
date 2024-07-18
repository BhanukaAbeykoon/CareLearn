import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPageClass:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "name")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/button")

    def login_student(self, username, password):
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

        time.sleep(3)
        # manager view button
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(5)

        WebDriverWait(self.driver, 100).until(
            EC.url_to_be("https://demo5.caresystemsinc.com/demo5/html_interface/manager/desktop.jsp"))
