from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        # self.lp.login("n3g@mail.ru", "volcom99")
        self.lp.login(password="volcom99")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful") # "test_validLogin" - любое название


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("n3g@mail.ru", "volcom")
        result = self.lp.verifyLoginFailed()
        assert result == True