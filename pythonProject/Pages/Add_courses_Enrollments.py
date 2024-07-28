import time

from selenium.webdriver.chrome import webdriver
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

        # select a record(7)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[7]/td[1]").click()
        time.sleep(3)

        # Enrollment button
        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[5]").click()
        time.sleep(3)

        # Enroll Employees
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/button[1]").click()
        time.sleep(3)

        # primary search button
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/button[1]").click()
        time.sleep(5)

        # search button
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[2]").click()
        time.sleep(9)

        # Employee select
        # change employee
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/table/tbody/tr[110]/td[1]").click()
        time.sleep(6)

        # accept
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/button[1]").click()
        time.sleep(3)

        # keep & Truncate
        keep_truncate = self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[2]")
        if keep_truncate.is_enabled():
            keep_truncate.click()
        else:
            # data
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("dialogContainer")
            self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/table/tbody/tr/td[1]").click()
            time.sleep(3)

        # cancel enrollment
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/div/button[3]").click()
        time.sleep(3)

        # approve enrollment
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        # View employee info button
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/div/button[4]").click()
        time.sleep(3)

        # view employee info button close
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]").click()
        time.sleep(3)

        # enrollments  button close
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]").click()

