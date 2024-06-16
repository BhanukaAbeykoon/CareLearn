import time

from selenium.common import NoSuchFrameException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class AddCoursePage:
    def __init__(self, driver):
        self.driver = driver
        self.dialog_container = "dialogContainer"
        self.add_course_button = (By.ID, "addCourseBtn")
        self.course_title_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]")
        self.course_code_field = (By.XPATH, "/html/body/div/div[2]/table/tbody/tr[2]/td[2]/input")
        self.modules_field = (By.ID, "Modules_Field")
        self.modules_dropdown = (By.ID, "selNoOfModules")

    def navigate_to_courses(self):
        global element_text1, element_text2, element_text3, text_area
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

        inactive_button = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/label[3]/input")
        inactive_button.click()
        time.sleep(7)

        active_button = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/label[2]/input")
        active_button.click()
        time.sleep(3)

        alphabetOrder_button = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/label[5]/input")
        alphabetOrder_button.click()
        time.sleep(4)

        self.driver.switch_to.frame("dialogContainer")

        change_ordering_to_alphabetical = self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]")
        change_ordering_to_alphabetical.click()
        time.sleep(5)

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame("dialogContainer")

        user_defined = self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/label[6]/input")
        user_defined.click()
        time.sleep(4)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/table/tbody/tr[1]").click()
        time.sleep(4)

        # modify button
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/button[2]").click()
        time.sleep(4)

        self.driver.switch_to.frame("dialogContainer")

        time.sleep(4)

        # modiify Course Title
        course_title = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[1]/td[2]/input")
        time.sleep(4)

        course_title.clear()
        time.sleep(3)

        course_title.send_keys("National Visa")
        time.sleep(4)

        course_abbrev = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[2]/td[2]/input")
        time.sleep(4)

        course_abbrev.clear()
        time.sleep(3)

        course_abbrev.send_keys("Visa")
        time.sleep(4)

        # modules select
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[3]/td[2]/input").click()

        self.driver.switch_to.frame("dialogContainer")

        # select modules
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/select").click()

        time.sleep(3)

        # select 3 modules
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/select/option[3]").click()

        wait = WebDriverWait(self.driver, 10)  # 10 seconds timeout

        time.sleep(3)

        def get_element_text(xpath):
            try:
                element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                return element.text.strip()
            except TimeoutException:
                return None

        time.sleep(3)

        # Get text of the first element
        element_text1 = get_element_text("/html/body/div/div[2]/div[2]/table/tbody/tr[1]/td[2]")

        time.sleep(3)

        if element_text1:
            # Get text of the second element
            time.sleep(3)

            element_text2 = get_element_text("/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td[2]")
            time.sleep(3)
            if element_text2:
                # Get text of the third element
                element_text3 = get_element_text("/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[2]")
                time.sleep(3)
                if not element_text3:
                    try:
                        # Click the third element and insert a value
                        self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div[2]/div[2]/table/tbody/tr[3]/td[2]").click()
                        time.sleep(3)
                        self.driver.switch_to.frame("dialogContainer")
                        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("Test")
                        time.sleep(3)
                        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
                        time.sleep(3)
                        self.driver.switch_to.default_content()
                        self.driver.switch_to.frame("dialogContainer")
                        self.driver.switch_to.frame("dialogContainer")
                        self.driver.switch_to.frame("dialogContainer")
                        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
                        time.sleep(3)
                    except NoSuchElementException as e:
                        print("An error occurred:", e)

        # part enroll tick
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/table/tbody/tr[4]/td[2]/label/input'))
            )

            # Check if the element is a checkbox or radio button and its current state
            if element.get_attribute('type') in ['checkbox', 'radio']:
                if not element.is_selected():
                    element.click()
                    print("Element clicked.")
                else:
                    print("Element is already selected.")
            else:
                element.click()
                print("Element clicked.")

        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(3)
        # Exam is ticked or not
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/table/tbody/tr[5]/td[2]/label/input'))
            )

            # Check if the element is a checkbox or radio button and its current state
            if element.get_attribute('type') in ['checkbox', 'radio']:
                if not element.is_selected():
                    element.click()
                    print("Element clicked.")
                else:
                    print("Element is already selected.")
            else:
                element.click()
                print("Element clicked.")

        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(3)
        # select grades
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[7]/td[2]/input").click()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/table/tbody/tr[1]/td").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/table/tbody/tr[2]/td").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/button[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()

        time.sleep(3)
        # credit hours
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        CH = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[8]/td[2]/input")
        CH.click()
        CH1 = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[8]/td[2]/input")
        CH1.clear()
        CH2 = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[8]/td[2]/input")
        CH2.send_keys("12")
        time.sleep(3)

        # certification
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[9]/td[2]/input").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[2]/td").click()

        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[3]/td").click()
        time.sleep(3)

        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
        time.sleep(3)

        #Renew months
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        RM = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[10]/td[2]/input").click()
        RM1 = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[10]/td[2]/input")
        RM1.clear()
        RM2 = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[10]/td[2]/input")
        RM2.send_keys("3")
        time.sleep(3)

        # Text area select

        try:
            text_area = wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/table/tbody/tr[11]/td[2]/textarea")))
            text_area.click()
            time.sleep(3)
            text_area1 = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[11]/td[2]/textarea")
            text_area1.clear()
            time.sleep(4)
            text_area2 = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/table/tbody/tr[11]/td[2]/textarea")
            text_area2.send_keys("test")
            time.sleep(4)
        except TimeoutException:
            print("Text area not found or not clickable")

        # Accept
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
        time.sleep(4)

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

        time.sleep(3)

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

    def test_education_process(self):
        time.sleep(3)
        self.driver.switch_to.default_content()
        education_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
        education_button.click()
        time.sleep(5)

        # courses button
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/button[2]").click()
        time.sleep(3)

        # view classes from
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/input").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")

        # Select a date
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[1]/td[4]").click()
        time.sleep(4)

        # accept button
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(5)

        # select a record
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[1]").click()
        time.sleep(3)

        # # replicate class button
        # self.driver.find_element(By.XPATH, "/html/body/div[4]/button[2]").click()
        # time.sleep(5)
        #
        # # select a date
        # self.driver.switch_to.default_content()
        # self.driver.switch_to.frame("dialogContainer")
        # self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[4]/td[6]").click()
        # time.sleep(3)
        #
        # # click accept button
        # self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        # time.sleep(3)
        #
        # # class ID
        # self.driver.switch_to.default_content()
        # self.driver.switch_to.frame("dialogContainer")
        # self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/input").clear()
        # self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/input").send_keys(
        #     "OP1009")
        # time.sleep(3)
        #
        # # course fee
        # self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").clear()
        # self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").send_keys(
        #     "80")
        # time.sleep(3)
        #
        # # save changes
        # self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/button[2]").click()
        # time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/button[1]").click()

        time.sleep(3)

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

        # course fee
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").send_keys(
            "95")
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/input").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[4]/td[7]").click()
        time.sleep(3)

        # accept
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)

        # modify time
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").send_keys(
            "08,00")
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").send_keys(
            "AM")

        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[2]/input").send_keys(
            "05,00")
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[2]/input").send_keys(
            "PM")
        time.sleep(3)
        # Instructor
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
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/table/tbody/tr[103]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[8]/td[2]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[8]/td[2]/input").send_keys(
            "B 403")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[9]/td[2]/input").clear()

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[9]/td[2]/input").send_keys(
            "7")
        time.sleep(3)

        # last day of enrollment
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[10]/td[2]/input").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[3]/td[5]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)
        #
        # External student
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[2]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/select/option[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[7]").click()
        time.sleep(3)

        present = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Present')]"))
        )

        present.click()
        time.sleep(5)

        # self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[8]").click()
        # time.sleep(5)
        #
        # passed1 = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Failed')]"))
        # )
        #
        # passed1.click()
        # time.sleep(5)
        #
        # self.driver.find_element(By.XPATH,
        #                          "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[7]").click()
        # time.sleep(3)
        #
        # self.driver.switch_to.frame("dialogContainer")
        # self.driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("22")
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        # time.sleep(3)
        #
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[6]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
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
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[19]/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[4]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(5)

        # enrollments
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

        # Employee select
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/table/tbody/tr[466]/td[1]").click()
        time.sleep(3)

        # accept
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/button[1]").click()
        time.sleep(3)

        # data
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/table/tbody/tr/td[1]").click()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/div/button[3]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/div/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]").click()
        time.sleep(3)

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
