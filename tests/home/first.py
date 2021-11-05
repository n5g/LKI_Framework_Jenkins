import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginTests():

    def test_validLogin(self):
        option = webdriver.FirefoxOptions()
        option.set_preference("dom.webdriver.enabled", False)
        # option.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36')
        # driver = webdriver.Firefox(executable_path="D:\Download\geckodriver.exe",options=option)

        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
        # driver = webdriver.Firefox(executable_path="D:\Download\geckodriver.exe")

        baseURL = "https://letskodeit.teachable.com/"
        baseURL2 = "https://sso.teachable.com/secure/42299/users/sign_in?reset_purchase_session=1"
        # driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        loginLink = driver.find_element(By.PARTIAL_LINK_TEXT, "Login")
        loginLink.click()
        time.sleep(2)

        emailField = driver.find_element(By.ID, "email")
        emailField.send_keys("n3g@mail.ru")
        time.sleep(3)

        passwordField = driver.find_element(By.ID, "password")
        passwordField.send_keys("volcom99")
        time.sleep(3)

        loginButton = driver.find_element(By.NAME, "commit")
        loginButton.click()
        time.sleep(3)

        userIcon = driver.find_element(By.XPATH, "//img[@alt='n3g@mail.ru']")
        if userIcon is not None:
            print("Login successful")
        else:
            print("Login Failed")

        driver.quit()

ff = LoginTests()
ff.test_validLogin()

