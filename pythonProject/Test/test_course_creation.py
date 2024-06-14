import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.Classes_Page import TestWebpageInteraction
from Pages.Login_page import LoginPage
from Pages.Add_course_page import AddCoursePage


class TestCourseCreation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Maximize the browser window

    def test_course_creation(self):
        login_page = LoginPage(self.driver)
        add_course_page = AddCoursePage(self.driver)

        login_page.login("admin", "admin")

        add_course_page.navigate_to_courses()

        add_course_page.add_course("Basic Life Support 2", "BLS")

        add_course_page.test_education_process()

        add_course_page.process_course()

        add_course_page.courses_report()


if __name__ == "__main__":
    unittest.main()
