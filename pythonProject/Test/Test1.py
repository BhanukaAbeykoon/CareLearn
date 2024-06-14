import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the Google website
driver.get("https://www.google.lk")

# Find the search input element and type "Hello"
search_input = driver.find_element(By.CSS_SELECTOR, "#APjFqb")
time.sleep(3)
search_input.send_keys("Hello")
search_input.send_keys(Keys.ENTER)
time.sleep(5)
