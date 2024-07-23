import time

from selenium.webdriver.common.by import By

from pythonProject.Pages.Login_page_Admin import LoginPage


class StudentEnrollmentClass:
    def __init__(self, driver):
        self.driver = driver
        self.dialog_container = "dialogContainer"
        self.add_course_button = (By.ID, "addCourseBtn")
        self.course_title_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]")
        self.course_code_field = (By.XPATH, "/html/body/div/div[2]/table/tbody/tr[2]/td[2]/input")
        self.modules_field = (By.ID, "Modules_Field")
        self.modules_dropdown = (By.ID, "selNoOfModules")

    def student(self):
        # # click education buttton
        # time.sleep(3)
        # self.driver.switch_to.default_content()
        # education_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
        # education_button.click()
        # time.sleep(5)
        #
        # # click my course enrollment button
        # self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/button").click()
        # time.sleep(5)
        #
        # # Enroll in course button
        # self.driver.switch_to.default_content()
        # self.driver.switch_to.frame("mainWindow")
        # enroll_in_course = self.driver.find_element(By.XPATH, "/html/body/div[4]/button[1]")
        # enroll_in_course.click()
        # time.sleep(5)
        #
        # # select a course
        # self.driver.switch_to.default_content()
        # self.driver.switch_to.frame("dialogContainer")
        # course_select = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr")
        # course_select.click()
        # time.sleep(3)
        #
        # # submit enrollment request
        # # with CSS selector
        # self.driver.switch_to.default_content()
        # self.driver.switch_to.frame("dialogContainer")
        # self.driver.find_element(By.CSS_SELECTOR, "#okBtn").click()
        # time.sleep(3)
        #
        # # Click My Menu
        # self.driver.switch_to.default_content()
        # self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]").click()
        # time.sleep(3)
        #
        # # click log out button
        # self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/button[15]").click()
        # time.sleep(3)

        # Again log in as admin
        login_page = LoginPage(self.driver)
        login_page.login("admin", "admin")
        time.sleep(3)

        # # Click Education button
        # time.sleep(3)
        # self.driver.switch_to.default_content()
        # education_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
        # education_button.click()
        # time.sleep(5)
        #
        # # process course enrollment button
        # process_course_enrollment_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/button[3]")
        # process_course_enrollment_button.click()
        # time.sleep(3)
        #
        # # view enrollments from
        # self.driver.switch_to.frame("mainWindow")
        # self.driver.find_element(By.XPATH, "/html/body/div[1]/input").click()
        # time.sleep(3)
        #
        # # select a month
        # self.driver.switch_to.default_content()
        # self.driver.switch_to.frame("dialogContainer")
        # self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/select[1]").click()
        # time.sleep(3)
        #
        # # select january
        # self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/select[1]/option[1]").click()
        # time.sleep(3)
        # # select january 1st
        # self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[1]/td[2]").click()
        # time.sleep(3)
        #
        # # Accept
        # self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        # time.sleep(3)
        #
        # # select pending record
        # self.driver.switch_to.default_content()
        # self.driver.switch_to.frame("mainWindow")
        # self.driver.find_element(By.CSS_SELECTOR, "td[title='Preceptorship P005']").click()
        # time.sleep(3)
        #
        # # click approve button
        # self.driver.find_element(By.CSS_SELECTOR, "#apprBtn").click()
        # time.sleep(3)
        #
        # # confirm approval
        # self.driver.switch_to.default_content()
        # self.driver.switch_to.frame("dialogContainer")
        # self.driver.find_element(By.CSS_SELECTOR, "button[class='primaryBtn thinBtn marginRight']").click()
        # time.sleep(3)

        # click my menu
        self.driver.switch_to.default_content()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]").click()
        time.sleep(3)

        #  click log out button
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/button[16]").click()
        time.sleep(3)
