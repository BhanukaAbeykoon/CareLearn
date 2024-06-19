import unittest

from selenium import webdriver

from pythonProject.Pages.AddClass import AddClass_Class
from pythonProject.Pages.Add_Courses2 import AddCoursesClass
from pythonProject.Pages.Add_courses_Enrollments import EnrollmentsClass
from pythonProject.Pages.Courses_Report import CoursesReportClass
from pythonProject.Pages.Login_page import LoginPage
from pythonProject.Pages.Naviagete_to_Courses1 import AddCourseClass
from pythonProject.Pages.ReplicateClass import Replicate_Class
from pythonProject.Pages.TableFinder import TableFinderClass
from pythonProject.Pages.process_Course_Enrollments import ProcessCourseEnrollmentClass


# from Pages.Login_page import LoginPage
# from Pages.Add_course_page import AddCoursePage


class TestCourseCreation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  # Maximize the browser window

    def test_course_creation(self):
        login_page = LoginPage(self.driver)
        add_course = AddCourseClass(self.driver)
        Add_Courses2 = AddCoursesClass(self.driver)
        ReplicateClass = Replicate_Class(self.driver)
        AddClass = AddClass_Class(self.driver)
        Add_courses_Enrollments = EnrollmentsClass(self.driver)
        TableFinder = TableFinderClass(self.driver)
        process_Course_Enrollments = ProcessCourseEnrollmentClass(self.driver)
        Courses_Report = CoursesReportClass(self.driver)

        login_page.login("admin", "admin")
        #
        # add_course.navigate_to_courses()
        #
        # Add_Courses2.add_course("Basic Life Support 2", "BLS")
        #
        # ReplicateClass.replicate_class()
        #
        # AddClass.add_class()

        # Add_courses_Enrollments.enrollments()

        TableFinder.table_data_find()

        # process_Course_Enrollments.process_course()
        #
        # Courses_Report.courses_report()


if __name__ == "__main__":
    unittest.main()
