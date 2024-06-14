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

        courses_button = driver.find_element(By.ID, "mi31$0")
        courses_button.click()

        time.sleep(10)

        driver.switch_to.frame("dialogContainer")

        add_course = driver.find_element(By.ID, "addCourseBtn")
        add_course.click()

        time.sleep(7)

        driver.switch_to.frame("dialogContainer")

        course_title = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/label[1]")

        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]").send_keys(
            "Basic Life Support 2")

        time.sleep(7)

        driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[2]/td[2]/input").send_keys("BLS")

        time.sleep(4)

        driver.find_element(By.ID, "Modules_Field").click()

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.ID, "selNoOfModules").click()

        time.sleep(4)

        option_3 = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/select")

        dropdown = Select(option_3)

        dropdown.select_by_value("3")

        time.sleep(5)

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[2]").click()

        time.sleep(4)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[4]/input[1]").send_keys("SA")

        time.sleep(5)

        driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()

        time.sleep(4)

        driver.switch_to.default_content()

        time.sleep(4)

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[3]").click()

        time.sleep(5)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("87")

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()

        time.sleep(4)

        driver.switch_to.default_content()

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[4]").click()

        time.sleep(4)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[2]/td").click()

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[3]/td").click()

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()

        time.sleep(4)

        driver.switch_to.default_content()

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[5]").click()

        time.sleep(4)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("3")

        driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()

        time.sleep(4)
        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.switch_to.frame("dialogContainer")
        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td[2]").click()

        time.sleep(3)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("MA")

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()

        time.sleep(3)

        time.sleep(4)

        driver.switch_to.default_content()

        time.sleep(4)

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td[3]").click()

        time.sleep(3)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("77")

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()

        time.sleep(3)

        driver.switch_to.default_content()

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td[4]").click()

        time.sleep(3)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[2]/td").click()

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[3]/td").click()

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()

        time.sleep(3)

        driver.switch_to.default_content()

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td[5]").click()

        time.sleep(3)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("4")

        driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()

        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.switch_to.frame("dialogContainer")
        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[2]").click()

        time.sleep(3)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("AL")

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()

        time.sleep(3)

        time.sleep(4)

        driver.switch_to.default_content()

        time.sleep(4)

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[3]").click()

        time.sleep(3)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("75")

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()

        time.sleep(3)

        driver.switch_to.default_content()

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[4]").click()

        time.sleep(3)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[4]/td").click()

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[5]/td").click()

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()

        time.sleep(3)

        driver.switch_to.default_content()

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[5]").click()

        time.sleep(3)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("4")

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()

        time.sleep(3)

        driver.switch_to.default_content()

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()

        time.sleep(3)

        driver.switch_to.default_content()

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[4]/td[2]/label/input").click()

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[5]/td[2]/label/input").click()

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[7]/td[2]/input").click()

        time.sleep(3)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/button[2]").click()

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()

        time.sleep(3)

        driver.switch_to.default_content()

        driver.switch_to.frame("dialogContainer")

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[8]/td[2]/input").clear()

        driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[8]/td[2]/input").send_keys("5")

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[9]/td[2]/input").click()

        time.sleep(3)

        driver.switch_to.frame("dialogContainer")

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[13]/td").click()

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[14]/td").click()

        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()

        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
