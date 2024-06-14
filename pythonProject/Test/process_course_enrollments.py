import this
import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class TestCourseCreation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_course_creation(self):
        driver = self.driver
        driver.get("https://demo5.caresystemsinc.com/demo5/html_interface/login.jsp")

        driver.maximize_window()

        username_field = driver.find_element(By.NAME, "name")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/button")

        username_field.send_keys("admin")
        password_field.send_keys("admin")
        login_button.click()

        time.sleep(4)

        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print("Alert text:", alert_text)
            # Handle the alert as you need, for example, accept it
            alert.accept()
            print("alert accepted")
        except:
            print("No alert found")

        time.sleep(10)

        WebDriverWait(driver, 100).until(
            EC.url_to_be("https://demo5.caresystemsinc.com/demo5/html_interface/manager/desktop.jsp"))

        if "demo5" in driver.current_url:
            print("Login successful!")
        else:
            print("Login failed.")

        time.sleep(5)

        education_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
        education_button.click()
        time.sleep(5)

        driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/button[3]").click()
        time.sleep(3)

        driver.switch_to.frame("mainWindow")
        driver.find_element(By.XPATH, "/html/body/div[1]/input").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[1]/td[2]").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("mainWindow")
        driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[5]/td[1]").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div[4]/div/button[3]").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div[4]/div/button[1]").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        # Enroll in a course
        driver.find_element(By.XPATH, "/html/body/div[4]/button[1]").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[3]/td").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[3]/td[1]").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/div/textarea").send_keys("Test 1")
        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[3]/div[4]/button[1]").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("mainWindow")
        driver.find_element(By.XPATH, "/html/body/div[5]/button").click()
        time.sleep(3)

