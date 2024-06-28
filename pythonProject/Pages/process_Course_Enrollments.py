import time

from selenium.common import NoSuchElementException
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
        self.driver.switch_to.default_content()
        education_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
        education_button.click()
        time.sleep(5)

        # process course enrollment button
        process_course_enrollment_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/button[3]")
        process_course_enrollment_button.click()
        time.sleep(3)

        # view enrollments from
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/input").click()
        time.sleep(3)

        # select a month
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/select[1]").click()
        time.sleep(3)

        # select january
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/select[1]/option[1]").click()
        time.sleep(3)
        # select january 1st
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[1]/td[2]").click()
        time.sleep(3)

        # Accept
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)

        # click a record
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[6]/td[1]").click()
        time.sleep(3)

        # click cancel
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/button[3]").click()
        time.sleep(3)

        # confirm cancellation
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        # click approve
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/button[1]").click()
        time.sleep(3)

        # click approve enrollment button
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        # select a course
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[7]").click()
        time.sleep(3)

        # Enroll in a course
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[1]").click()
        time.sleep(3)

        # Select a student
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[8]/td").click()
        time.sleep(3)

        # Accept
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
        time.sleep(3)

        # select a course
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        try:
            # Try to find and click the course
            course = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr")
            course.click()
            time.sleep(3)
        except NoSuchElementException:
            # If the course is not found, click the cancel button
            cancel_button = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[4]/button[2]")
            cancel_button.click()

        # again click Enroll in a course
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[1]").click()
        time.sleep(3)

        # Select a student
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[1]/td").click()
        time.sleep(3)

        # Accept
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
        time.sleep(3)

        # select a course
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        try:
            # Try to find and click the course
            course = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr")
            course.click()
            time.sleep(3)
        except NoSuchElementException:
            # If the course is not found, click the cancel button
            cancel_button = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[4]/button[2]")
            cancel_button.click()

        # Submit enrollment request
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[4]/button[1]").click()
        time.sleep(3)

        # Try to find and click the keep and truncate button if it exists
        try:
            # keep and truncate pop up button
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame("dialogContainer")
            self.driver.switch_to.frame("dialogContainer")
            button = self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[2]")
            button.click()
            time.sleep(3)
        except NoSuchElementException:
            # If the element is not found, do nothing
            pass
        time.sleep(4)


time.sleep(5)
