import time

from selenium.common import NoSuchFrameException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCoursesClass:
    def __init__(self, driver):
        self.driver = driver
        self.dialog_container = "dialogContainer"
        self.add_course_button = (By.ID, "addCourseBtn")
        self.course_title_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]")
        self.course_code_field = (By.XPATH, "/html/body/div/div[2]/table/tbody/tr[2]/td[2]/input")
        self.modules_field = (By.ID, "Modules_Field")
        self.modules_dropdown = (By.ID, "selNoOfModules")

    def add_course(self, title, code):
        time.sleep(3)
        self.driver.switch_to.default_content()
        education_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
        education_button.click()
        time.sleep(5)

        courses_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/button[1]")
        courses_button.click()
        time.sleep(10)

        try:
            self.driver.switch_to.frame("dialogContainer")
        except NoSuchFrameException as e:
            print("Error: Unable to switch to the dialogContainer frame.")
            print(e)
            return

        self.driver.find_element(*self.add_course_button).click()
        time.sleep(4)
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.find_element(*self.course_title_field).send_keys(title)
        self.driver.find_element(*self.course_code_field).send_keys(code)
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[3]/td[2]/input").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")

        self.driver.find_element(By.ID, "selNoOfModules").click()

        time.sleep(4)

        option_3 = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/select")

        dropdown = Select(option_3)

        dropdown.select_by_value("3")

        time.sleep(5)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[2]").click()

        time.sleep(4)

        self.driver.switch_to.frame("dialogContainer")

        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[4]/input[1]").send_keys("SA")

        time.sleep(5)

        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()

        time.sleep(4)

        self.driver.switch_to.default_content()

        time.sleep(4)

        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[3]").click()
        time.sleep(5)

        self.driver.switch_to.frame(self.dialog_container)
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("87")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(4)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[4]").click()
        time.sleep(4)

        self.driver.switch_to.frame(self.dialog_container)
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[2]/td").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[3]/td").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
        time.sleep(4)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[5]").click()
        time.sleep(4)

        self.driver.switch_to.frame(self.dialog_container)
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("3")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(4)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td[2]").click()
        time.sleep(3)

        self.driver.switch_to.frame(self.dialog_container)
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("MA")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td[3]").click()
        time.sleep(3)

        self.driver.switch_to.frame(self.dialog_container)
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("77")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td[4]").click()
        time.sleep(3)

        self.driver.switch_to.frame(self.dialog_container)
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[2]/td").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[3]/td").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)
        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td[5]").click()
        time.sleep(3)

        self.driver.switch_to.frame(self.dialog_container)
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("4")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.switch_to.frame(self.dialog_container)

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[2]").click()

        time.sleep(3)

        self.driver.switch_to.frame(self.dialog_container)
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("TA")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()

        time.sleep(3)

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.switch_to.frame(self.dialog_container)

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[3]").click()

        time.sleep(3)

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("67")

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()

        time.sleep(3)

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.switch_to.frame(self.dialog_container)

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[4]").click()

        time.sleep(3)

        self.driver.switch_to.frame(self.dialog_container)

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[13]/td").click()

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[14]/td").click()

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()

        time.sleep(3)

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.switch_to.frame(self.dialog_container)

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[5]").click()

        time.sleep(3)

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("4")

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()

        time.sleep(3)

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()

        time.sleep(4)

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[4]/td[2]/label/input").click()

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[5]/td[2]/label/input").click()

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[7]/td[2]/input").click()

        time.sleep(3)

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/button[2]").click()

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()

        time.sleep(3)

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[8]/td[2]/input").clear()

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[8]/td[2]/input").send_keys("5")

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[9]/td[2]/input").click()

        time.sleep(3)

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[8]/td").click()

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[9]/td").click()

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()

        time.sleep(3)

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[10]/td[2]/input").clear()

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[10]/td[2]/input").send_keys("4")

        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[11]/td[2]/textarea").send_keys("test")

        time.sleep(3)

        # self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[12]/td[2]/input").send_keys(
        #     "https://www.wikipedia.org/")
        #
        # time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()

        time.sleep(3)

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.dialog_container)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[4]/button[2]").click()

        time.sleep(3)
