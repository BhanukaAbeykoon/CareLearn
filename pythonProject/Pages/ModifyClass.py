import time

from selenium.webdriver.common.by import By


class EnrollmentsClass:
    def __init__(self, driver):
        self.driver = driver
        self.dialog_container = "dialogContainer"
        self.add_course_button = (By.ID, "addCourseBtn")
        self.course_title_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]")
        self.course_code_field = (By.XPATH, "/html/body/div/div[2]/table/tbody/tr[2]/td[2]/input")
        self.modules_field = (By.ID, "Modules_Field")
        self.modules_dropdown = (By.ID, "selNoOfModules")

    def enrollments(self):
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

        # select a record
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[8]/td[1]").click()
        time.sleep(3)

        # Modify button
        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[3]").click()
        time.sleep(3)

        # class ID
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/input").send_keys(
            "ERl005")
        time.sleep(3)

        # Units that can enroll
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[3]/td[2]/input").click()
        time.sleep(3)

        # add all
        self.driver.switch_to.frame("dialogContainer")
        try:
            add_all_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/button[2]")
            if add_all_button.is_enabled():
                add_all_button.click()
            else:
                accept_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/button[1]")
                accept_button.click()
        except (ElementNotInteractableException, NoSuchElementException):
            accept_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/button[1]")
            accept_button.click()

        # grades that can enroll
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[4]/td[2]/input").click()
        time.sleep(3)

        # add all
        self.driver.switch_to.frame("dialogContainer")
        try:
            add_all_button = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/button[2]")
            if add_all_button.is_enabled():
                add_all_button.click()
            else:
                accept_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/button[1]")
                accept_button.click()
        except (ElementNotInteractableException, NoSuchElementException):
            accept_button = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]")
            accept_button.click()

        # course fee
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").send_keys(
            "95")
        time.sleep(3)

        # Location
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[8]/td[2]/input").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[8]/td[2]/input").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[8]/td[2]/input").send_keys(
            "B403")
        time.sleep(3)

        # capacity
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[9]/td[2]/input").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[9]/td[2]/input").clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[9]/td[2]/input").send_keys("15")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[10]/td[2]/input").click()
        time.sleep(3)

        # last day of enrollment
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[4]/td[6]").click()
        time.sleep(3)
        # accept button
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)

        # click save button
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/button[2]").click()
        time.sleep(3)

