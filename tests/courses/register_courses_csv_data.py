from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
from pages.home.navigation_page import NavigationPage

import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToHome()

    @pytest.mark.run(order=1)
    @data(*getCSVData("D:/Other/code/py_return/lets_kode_it/Letskodeit_Framework/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccName, ccNum, ccExp, ccCVC, billingStreet, billingCity):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(name=ccName, num=ccNum, exp=ccExp, cvc=ccCVC, street=billingStreet, city=billingCity)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
        # self.courses.clickOnHomeButton()
