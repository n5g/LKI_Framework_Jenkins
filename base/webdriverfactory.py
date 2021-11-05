from webdriver_manager.chrome import ChromeDriverManager
import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "https://letskodeit.teachable.com/"
        # baseURL = "https://sso.teachable.com/secure/42299/checkout/342639/complete-javascript-guide"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path="D:\Download\geckodriver.exe")
        elif self.browser == "chrome":
            # Set chrome driver
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
            # driver = webdriver.Chrome(executable_path="D:\Download\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)

        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
            # driver = webdriver.Chrome(executable_path="D:\Download\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver