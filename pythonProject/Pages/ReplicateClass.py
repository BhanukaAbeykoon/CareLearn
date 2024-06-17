import time

from selenium.webdriver.common.by import By


class Replicate_Class:
    def __init__(self, driver):
        self.driver = driver
        self.dialog_container = "dialogContainer"
        self.add_course_button = (By.ID, "addCourseBtn")
        self.course_title_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]")
        self.course_code_field = (By.XPATH, "/html/body/div/div[2]/table/tbody/tr[2]/td[2]/input")
        self.modules_field = (By.ID, "Modules_Field")
        self.modules_dropdown = (By.ID, "selNoOfModules")

    def replicate_class(self):
        global alt_button_xpath
        time.sleep(3)
        self.driver.switch_to.default_content()
        education_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
        education_button.click()
        time.sleep(5)

        # classes button
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/button[2]").click()
        time.sleep(3)

        # view classes from
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/input").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")

        # select a month
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/select[1]").click()

        # February
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/select[1]/option[2]").click()

        # Date
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[1]/td[5]").click()

        # accept button
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(5)
        #
        # select a record
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[1]").click()
        time.sleep(3)

        # replicate class button
        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[2]").click()
        time.sleep(5)

        # select a date
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[4]/td[6]").click()
        time.sleep(3)

        # click accept button
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)

        # class ID
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/input").send_keys(
            "DA1009")
        time.sleep(3)

        # course fee
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").send_keys(
            "80")
        time.sleep(3)

        # save changes
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/button[2]").click()
        time.sleep(3)

        time.sleep(3)


