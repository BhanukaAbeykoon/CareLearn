import time

from selenium.webdriver.common.by import By


class ProcessCourseEnrollmentClass:
    def __init__(self, driver):
        self.driver = driver
        self.dialog_container = "dialogContainer"
        self.add_course_button = (By.ID, "addCourseBtn")
        self.course_title_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]")
        self.course_code_field = (By.XPATH, "/html/body/div/div[2]/table/tbody/tr[2]/td[2]/input")
        self.modules_field = (By.ID, "Modules_Field")
        self.modules_dropdown = (By.ID, "selNoOfModules")

    def process_course(self):
        driver = self.driver
        time.sleep(3)
        education_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
        education_button.click()
        time.sleep(5)

        # process course enrollment
        driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/button[3]").click()
        time.sleep(3)

        driver.switch_to.frame("mainWindow")
        driver.find_element(By.XPATH, "/html/body/div[1]/input").click()
        time.sleep(3)

        # Date
        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[1]/td[4]").click()
        time.sleep(3)

        # Accept
        driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)

        # click a record
        driver.switch_to.default_content()
        driver.switch_to.frame("mainWindow")
        driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr/td[1]").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("mainWindow")
        driver.find_element(By.XPATH, "/html/body/div[4]/div/button[3]").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("mainWindow")
        driver.find_element(By.XPATH, "/html/body/div[4]/div/button[1]").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        # Enroll in a course
        driver.switch_to.default_content()
        driver.switch_to.frame("mainWindow")
        driver.find_element(By.XPATH, "/html/body/div[4]/button[1]").click()
        time.sleep(3)

        # Select a student
        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[8]/td").click()
        time.sleep(3)

        # Accept
        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
        time.sleep(3)

        # select a course
        driver.switch_to.default_content()
        driver.switch_to.frame("dialogContainer")
        driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[1]").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/div/textarea").send_keys("Test 1")
        time.sleep(3)

        driver.find_element(By.XPATH, "/html/body/div/div[3]/div[4]/button[1]").click()
        time.sleep(3)

        driver.switch_to.default_content()
        driver.switch_to.frame("mainWindow")
        driver.find_element(By.XPATH, "/html/body/div[5]/button").click()
        time.sleep(3)
