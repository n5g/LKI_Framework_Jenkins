import logging

import time

from utilities import custom_logger as cl
from base.basepage import BasePage


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "search-courses"  # id   - JavaScript for beginners
    _course = "//div[contains(text(),'{0}')]"  # partial link text
    _all_courses = "//div[@class='course-listing-title']"  # xpath
    _enroll_button = "enroll-button-top"  # id
    _name_on_card = "//input[@data-test='credit-card-name']"  # xpath
    _cc_num = "//input[@placeholder='1234 1234 1234 1234']"
    _cc_exp = "//input[@placeholder='ММ / ГГ']"
    _cc_cvc = "//input[@placeholder='CVC']"
    _billing_street = "billingStreetAddressLine1"  # id
    _billing_city = "billingCity"  # id
    _submit_enroll = "//button[contains(text(),'Buy Now $99')]"  # xpath
    _enroll_error_message = "//li[contains(text(),'The card was declined.')]"  # xpath
    _i_frame_card_num = "//iframe[@title='Защищенное окно для ввода номера карты']"
    _i_frame_exp_date = "//iframe[@title='Защищенное окно для ввода даты истечения срока']"
    _i_frame_cvc = "//iframe[@title='Защищенное окно для ввода CVC-кода']"
    # _home = "//a[@class='navbar-brand header-logo']"

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box)  # locatorType="id" не указываю т.е он по умолчанию

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button)

    # def clickOnHomeButton(self):
    #     self.elementClick(locator=self._home, locatorType="xpath")

    def enterName(self, name):
        self.sendKeys(name, locator=self._name_on_card, locatorType="xpath")

    def enterCardNum(self, num):
        self.switchToFrame(locator=self._i_frame_card_num)
        self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.switchToFrame(locator=self._i_frame_exp_date)
        self.sendKeys(exp, locator=self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardCVC(self, cvc):
        self.switchToFrame(locator=self._i_frame_cvc)
        self.sendKeys(cvc, locator=self._cc_cvc, locatorType="xpath")
        self.switchToDefaultContent()

    def enterBillingStreet(self, street):
        self.sendKeys(street, locator=self._billing_street)

    def enterBillingCity(self, city):
        self.sendKeys(city, locator=self._billing_city)

    def clickEnrollSubmitButton(self):
        time.sleep(5)
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")


    def enterCreditCardInformation(self, name, num, exp, cvc):
        self.enterName(name)
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVC(cvc)

    def enterbillingAddress(self, street, city):
        self.enterBillingStreet(street)
        self.enterBillingCity(city)

    def enrollCourse(self, name="", num="", exp="", cvc="", street="", city=""):
        self.clickOnEnrollButton()
        # self.webScroll(direction="down")
        self.enterCreditCardInformation(name, num, exp, cvc)
        self.enterbillingAddress(street, city)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        result = self.isElementPresent(self._enroll_error_message, locatorType="xpath")
        return result
