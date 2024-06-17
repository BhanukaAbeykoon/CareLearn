import time
import unittest

from selenium.webdriver.common.by import By


class CoursesReportClass(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver
        self.dialog_container = "dialogContainer"
        self.add_course_button = (By.ID, "addCourseBtn")
        self.course_title_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]")
        self.course_code_field = (By.XPATH, "/html/body/div/div[2]/table/tbody/tr[2]/td[2]/input")
        self.modules_field = (By.ID, "Modules_Field")
        self.modules_dropdown = (By.ID, "selNoOfModules")

    def courses_report(self):
        driver = self.driver
        driver.switch_to.default_content()
        education_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
        education_button.click()

        time.sleep(5)

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

    # self.driver.switch_to.default_content()
    #
    # self.driver.switch_to.frame("dialogContainer")
    #
    # time.sleep(3)
    #
    # # select table row 4
    # self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/table/tbody/tr[4]").click()
    # time.sleep(3)
    #
    # # select make inactive
    # self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/button[4]").click()
    # time.sleep(5)

    #
    # self.driver.switch_to.default_content()
    #
    # education_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
    # education_button.click()
    # time.sleep(5)
    #
    # courses_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/button[1]")
    # courses_button.click()
    # time.sleep(10)
    #
    # try:
    #     self.driver.switch_to.frame("dialogContainer")
    # except NoSuchFrameException as e:
    #     print("Error: Unable to switch to the dialogContainer frame.")
    #     print(e)
    #     return
    #
    # self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[4]/button[1]").click()
    #
    # time.sleep(3)
    #
    # self.driver.switch_to.frame("dialogContainer")
    #
    # self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
    #
    # time.sleep(3)
