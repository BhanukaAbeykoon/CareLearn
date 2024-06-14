import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCourseCreation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.get("https://chinternal.caresystemsinc.com/Capital_Health_QA_Branch/html_interface/login.jsp")
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
            alert.accept()
            self.assertEqual(alert_text, "Invalid username or password.")
        except:
            pass

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://demo5.caresystemsinc.com/demo5/html_interface/manager/desktop.jsp"))
        self.assertIn("demo5", driver.current_url)

    def process_course(self):
        driver = self.driver
        driver.get("https://demo5.caresystemsinc.com/demo5/html_interface/manager/desktop.jsp")

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


if __name__ == "__main__":
    unittest.main()
