# test case
# ----------
import time

from selenium import webdriver
from selenium.common import NoSuchFrameException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
driver = webdriver.Chrome()

driver.maximize_window()
# Open the login page
driver.get("https://demo5.caresystemsinc.com/demo5/html_interface/login.jsp")

# Find username and password input fields and login button
username_field = driver.find_element(By.NAME, "name")
password_field = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/button")

# Enter username and password
username_field.send_keys("admin")
password_field.send_keys("admin")

# Click the login button
login_button.click()

time.sleep(4)

try:
    alert = driver.switch_to.alert
    alert_text = alert.text
    print("Alert text:", alert_text)
    # Handle the alert as you need, for example, accept it
    alert.accept()
    print("alert accepted")
except:
    print("No alert found")

time.sleep(10)

# Wait for the page to load after login
WebDriverWait(driver, 100).until(
    EC.url_to_be("https://demo5.caresystemsinc.com/demo5/html_interface/manager/desktop.jsp"))

# Verify if login was successful
if "demo5" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed.")

time.sleep(5)

# Find Education button by xpath
education_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
# Click the Education button
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
