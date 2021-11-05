import logging
from base.selenium_driver import SeleniumDriver
from utilities import custom_logger as cl
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

# class LoginPage(SeleniumDriver):
class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "Login"
    _email_field = "email"
    _password_field = "password"
    _login_button = "commit"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//img[@alt='n3g@mail.ru']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[contains(text(),'Your email or password is incorrect')]", locatorType="xpath")
        return result

    def verifyTitle(self):
        # return self.verifyPageTitle("Google")
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        self.nav.navigateToUserSettings()
        # logoutLinkElement = self.waitForElement(locator="a[href='/sign_out']", locatorType="css", pollFrequency=1)
        # self.elementClick(locator="a[href='/sign_out']", locatorType="css", element=logoutLinkElement)
        self.elementClick(locator="a[href='/sign_out']", locatorType="css")




