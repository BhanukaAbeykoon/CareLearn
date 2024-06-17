import time

from selenium.webdriver.common.by import By


class AddClass_Class:
    def __init__(self, driver):
        self.driver = driver
        self.dialog_container = "dialogContainer"
        self.add_course_button = (By.ID, "addCourseBtn")
        self.course_title_field = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/input[1]")
        self.course_code_field = (By.XPATH, "/html/body/div/div[2]/table/tbody/tr[2]/td[2]/input")
        self.modules_field = (By.ID, "Modules_Field")
        self.modules_dropdown = (By.ID, "selNoOfModules")

    # Add class button
    # Switch back to the default content
    def add_class(self):
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

        self.driver.switch_to.default_content()

        # Switch to the main window frame
        self.driver.switch_to.frame("mainWindow")
        time.sleep(3)

        # Click the add class button
        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[1]").click()
        time.sleep(3)

        # Select a course
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[2]").click()
        time.sleep(3)

        # accept button
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
        time.sleep(3)

        # class ID
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/input").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/input").send_keys(
            "EH001")
        time.sleep(3)

        # course fee
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").send_keys(
            "2000")
        time.sleep(3)

        # Date
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/input").click()
        time.sleep(3)

        # 20 date select
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[4]/td[5]").click()
        time.sleep(3)

        # Accept button
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)

        # select start time
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").send_keys(
            "10:00", "AM")
        time.sleep(3)

        # select end time
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[2]/input").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[2]/input").send_keys(
            "11:00", "AM")
        time.sleep(3)

        # Instructor
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[7]/td[2]/input").click()
        time.sleep(3)

        # primary search
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[2]/div[1]/button[1]").click()
        time.sleep(3)

        # search
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/button[2]").click()
        time.sleep(5)

        # select a instructor
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/table/tbody/tr[102]/td[1]").click()
        time.sleep(6)

        # accept button
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[2]/div[5]/button[1]").click()
        time.sleep(3)

        # Location
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[8]/td[2]/input").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div[3]/div[1]/table/tbody/tr[8]/td[2]/input").send_keys("B409")

        # capacity
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[9]/td[2]/input").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[9]/td[2]/input").send_keys(
            "20")
        time.sleep(3)

        # Last day of enrollment
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[10]/td[2]/input").click()
        time.sleep(3)

        # select a date
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[4]/td[6]").click()
        time.sleep(3)

        # Accept button
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")

        # add module button if available
        def is_element_available(driver, by, value, timeout=10):
            try:
                element = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((by, value))
                )
                return element.is_enabled()
            except (TimeoutException, NoSuchElementException):
                return False

        try:
            add_module_xpath = "/html/body/div/div[3]/div[1]/div[1]/button[1]"
            alt_button_xpath = "/html/body/div/div[3]/div[2]/button[2]"

            # Check if the "Add Module" button is available (present and enabled)
            if is_element_available(self.driver, By.XPATH, add_module_xpath):
                add_module_button = self.driver.find_element(By.XPATH, add_module_xpath)
                add_module_button.click()
                time.sleep(3)

                # MOD 1
                mod1_label = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[1]/td[2]/label"))
                )
                mod1_label.click()
                time.sleep(3)

                # Switch to the frame for the date input
                self.driver.switch_to.frame("dialogContainer")
                date_input = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/input"))
                )
                date_input.click()
                time.sleep(3)

                # Select a Date
                date_selection = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/table/tbody/tr[4]/td[6]"))
                )
                date_selection.click()
                time.sleep(3)

                # Accept button
                accept_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[4]/button[2]"))
                )
                accept_button.click()
                time.sleep(3)
            else:
                # save button
                alt_button = self.driver.find_element(By.XPATH, alt_button_xpath)
                alt_button.click()
                time.sleep(3)

        except (NoSuchElementException, ElementNotInteractableException) as e:
            print(f"An error occurred: {e}")
