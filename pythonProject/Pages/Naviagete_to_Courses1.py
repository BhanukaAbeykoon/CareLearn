import time

from selenium.common import NoSuchFrameException, NoSuchElementException, TimeoutException, \
    ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait


class AddCourseClass:
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

        # Renew months
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

        # Accept button
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
        time.sleep(4)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[4]/button[3]").click()
        time.sleep(4)
