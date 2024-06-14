import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_page(self):
        driver = self.driver
        driver.get("https://demo5.caresystemsinc.com/demo5/html_interface/login.jsp")

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
            alert.accept()
            print("Alert accepted")
        except:
            print("No alert found")

        time.sleep(10)

        self.assertTrue(
            EC.url_to_be("https://demo5.caresystemsinc.com/demo5/html_interface/manager/desktop.jsp")(driver))
        print("Login successful!")

    def test_open_education_page(self):
        driver = self.driver
        self.test_login_page()  # Ensure login before opening education page

        education_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
        education_button.click()

        time.sleep(5)

        driver = self.driver
        self.test_open_education_page()  # Ensure education page is open before adding education

        driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/button[4]").click()
        time.sleep(3)

        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/input[1]").click()
        time.sleep(3)

        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[1]/td[2]").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/button[1]").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[4]/button[3]").click()
        time.sleep(3)

        print("Education added successfully.")


if __name__ == "__main__":
    unittest.main()
