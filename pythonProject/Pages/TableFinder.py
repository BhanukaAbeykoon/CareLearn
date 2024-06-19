import time

from selenium.webdriver.common.by import By


class TableFinderClass:
    def __init__(self, driver):
        self.driver = driver
        self.dialog_container = "dialogContainer"

    def table_data_find(self):
        time.sleep(3)
        self.driver.switch_to.default_content()

        # Clicking the education button
        education_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
        education_button.click()
        time.sleep(5)

        # Clicking the classes button
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/button[2]").click()
        time.sleep(3)

        # View classes from
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[1]/input").click()
        time.sleep(3)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")

        # Selecting a date
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[4]/td[4]").click()

        # Clicking the accept button
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
        time.sleep(5)

        # Find national visa mts 12
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("mainWindow")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[2]/td[1]").click()

        # Enrollment button
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[4]/button[5]").click()
        time.sleep(3)

        # select first record
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/table/tbody/tr/td[2]").click()
        time.sleep(3)

        # modify module list button
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/button[2]").click()
        time.sleep(3)

        # Modify Enrollment modules
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr/td[2]/input").click()
        time.sleep(3)

        # remove a module
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/table/tbody/tr[2]/td").click()
        time.sleep(3)
        # click remove
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/button[3]").click()
        time.sleep(3)
        # click accept button
        self.driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
        time.sleep(3)

        # save changes button
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[4]/button[1]").click()
        time.sleep(3)

        # close button
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("dialogContainer")
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]").click()
        time.sleep(3)



