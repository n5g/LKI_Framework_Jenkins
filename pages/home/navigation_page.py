import logging
from base.selenium_driver import SeleniumDriver
from utilities import custom_logger as cl
from base.basepage import BasePage

# class LoginPage(SeleniumDriver):
class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    _user_settings_icon = "//img[@alt='n3g@mail.ru']"
    _home = "//a[@class='navbar-brand header-logo']"

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses,locatorType="link")

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="link")

    def navigateToUserSettings(self):
        # userSettingsElement = self.waitForElement(locator=self._user_settings_icon, locatorType="xpath", pollFrequency=1)
        # self.elementClick(element=userSettingsElement)
        self.elementClick(locator=self._user_settings_icon, locatorType="xpath")

    def navigateToHome(self):
        self.elementClick(locator=self._home, locatorType="xpath")
