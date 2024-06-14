import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWebpageInteraction(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        # cls.driver.get("https://demo5.caresystemsinc.com/demo5/html_interface/login.jsp")
        # cls.wait = WebDriverWait(cls.driver, 20)

    def test_education_process(self):
        time.sleep(3)
        education_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
        education_button.click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/button[2]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/input").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[2]/td[6]").click()
        time.sleep(4)

        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(5)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[7]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[2]").click()
        time.sleep(5)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[4]/td[6]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/input").send_keys(
            "SA007")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").send_keys("80")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/button[2]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[1]").click()

        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[6]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/input").send_keys(
            "P005")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").send_keys("95")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/input").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[3]/td[4]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").send_keys(
            "08,09")
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").send_keys("PM")

        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[2]/input").send_keys(
            "10,00")
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[2]/input").send_keys("PM")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[7]/td[2]/input").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/button[1]").click()
        time.sleep(10)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[2]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/table/tbody/tr[647]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[8]/td[2]/input").send_keys(
            "B 403")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[9]/td[2]/input").send_keys("7")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[10]/td[2]/input").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[3]/td[5]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").send_keys(
            "08,09")
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").send_keys("PM")

        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[2]/input").send_keys(
            "10,00")
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[2]/input").send_keys("PM")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[7]/td[2]/input").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[2]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/table/tbody/tr[647]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[7]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[5]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/table/tbody/tr[4]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/div/button[3]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[2]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/table/tbody/tr[647]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[7]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[5]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/table/tbody/tr[4]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/div/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[9]").click()
        time.sleep(3)

        present = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Present')]"))
        )

        present.click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[8]").click()
        time.sleep(5)

        passed1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Failed')]"))
        )

        passed1.click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[7]").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("22")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[6]").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/textarea").send_keys("test")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[5]/input").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/button[2]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[4]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[4]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[7]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[5]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[2]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/table/tbody/tr[647]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[7]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[5]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/table/tbody/tr[4]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/div/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
