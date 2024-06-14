import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://demo5.caresystemsinc.com/demo5/html_interface/login.jsp")

driver.maximize_window()

username_field = driver.find_element(By.NAME, "name")
password_field = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/form/button")

username_field.send_keys("admin")
password_field.send_keys("admin")
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

WebDriverWait(driver, 100).until(
    EC.url_to_be("https://demo5.caresystemsinc.com/demo5/html_interface/manager/desktop.jsp"))

if "demo5" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed.")

time.sleep(5)

time.sleep(3)
driver.switch_to.default_content()
education_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[6]")
education_button.click()
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[2]/div[6]/div/button[2]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("mainWindow")
driver.find_element(By.XPATH, "/html/body/div[1]/input").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")

driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[2]/td[6]").click()
time.sleep(4)

driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
time.sleep(5)

driver.switch_to.default_content()
driver.switch_to.frame("mainWindow")
driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[7]/td[1]").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div[4]/button[2]").click()
time.sleep(5)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[4]/td[6]").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/input").send_keys("SA007")
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").clear()
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").send_keys("80")
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/button[2]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("mainWindow")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[4]/button[1]").click()

time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[2]/div/table/tbody/tr[6]/td[1]").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/button[1]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[2]/td[2]/input").send_keys("P005")
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[5]/td[2]/input").send_keys("95")
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/input").click()
time.sleep(3)

driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[3]/td[4]").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").send_keys(
    "08,09")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[1]/input").send_keys(
    "PM")

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[2]/input").send_keys(
    "10,00")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[6]/td[2]/label[2]/input").send_keys(
    "PM")
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[7]/td[2]/input").click()
time.sleep(3)

driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/button[1]").click()
time.sleep(10)

driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/button[2]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/table/tbody/tr[647]/td[1]").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/button[1]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[8]/td[2]/input").send_keys("B 403")
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[9]/td[2]/input").send_keys("7")
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[10]/td[2]/input").click()
time.sleep(3)

driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/table/tbody/tr[3]/td[5]").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[4]/button[2]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[2]/button[1]").click()
time.sleep(3)

driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/select/option[1]").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/button[1]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[2]/button[3]").click()
time.sleep(3)

driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[8]/td[2]/input").clear()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/table/tbody/tr[8]/td[2]/input").send_keys("12212")
time.sleep(5)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/button[1]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[9]").click()
time.sleep(3)

present = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Present')]"))
)

present.click()
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[8]").click()
time.sleep(5)

passed1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Failed')]"))
)

passed1.click()
time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[7]").click()
time.sleep(3)

driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[4]/input").send_keys("22")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[6]").click()
time.sleep(3)

driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[4]/textarea").send_keys("test")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[2]/div[1]/table/tbody/tr/td[5]/input").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/button[2]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("mainWindow")
driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[4]/td[1]").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div[4]/button[4]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("mainWindow")
driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[7]/td[1]").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div[4]/button[5]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/button[1]").click()
time.sleep(3)

driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/button[1]").click()
time.sleep(3)

driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/button[2]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/table/tbody/tr[647]/td[1]").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/button[1]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("mainWindow")
driver.find_element(By.XPATH, "/html/body/div[2]/table/tbody/tr[7]/td[1]").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div[4]/button[5]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/table/tbody/tr[4]/td[1]").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/div/button[3]").click()
time.sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("dialogContainer")
# driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
# time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[2]/table/tbody/tr[4]/td[1]").click()
time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/div/button[1]").click()
time.sleep(3)

driver.switch_to.frame("dialogContainer")
driver.find_element(By.XPATH, "/html/body/div/div[5]/button[1]").click()
time.sleep(3)
