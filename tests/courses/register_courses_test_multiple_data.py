from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "Ivan Ivanov", "5100000000000008", "12/22", "123", "Gagarina", "Ufa"),
          ("Learn Python 3 from scratch", "Ivan Putin", "5100000000000008", "12/23", "124", "Ivanova", "Surgut"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccName, ccNum, ccExp, ccCVC, billingStreet, billingCity):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(name=ccName, num=ccNum, exp=ccExp, cvc=ccCVC, street=billingStreet, city=billingCity)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")
        self.courses.clickOnHomeButton()
