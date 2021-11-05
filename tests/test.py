import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By






chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
driver.get("https://sso.teachable.com/secure/42299/checkout/342639/complete-javascript-guide")
driver.maximize_window()
driver.implicitly_wait(2)
driver.execute_script("window.scrollBy(0, 700);")

driver.find_element(By.XPATH, "//input[@data-test='credit-card-name']").send_keys("Ivan ivanov")



iframeCardNum = driver.find_element(By.XPATH, "//iframe[@title='Защищенное окно для ввода номера карты']")
driver.switch_to.frame(iframeCardNum)
cn = driver.find_element(By.XPATH, "//input[@placeholder='1234 1234 1234 1234']")
cn.send_keys("5100000000000008")

driver.switch_to.default_content()

iframeDateNum = driver.find_element(By.XPATH, "//iframe[@title='Защищенное окно для ввода даты истечения срока']")
driver.switch_to.frame(iframeDateNum)
en = driver.find_element(By.XPATH, "//input[@placeholder='ММ / ГГ']")
en.send_keys("10/22")

driver.switch_to.default_content()

iframeCvvNum = driver.find_element(By.XPATH, "//iframe[@title='Защищенное окно для ввода CVC-кода']")
driver.switch_to.frame(iframeCvvNum)
cn = driver.find_element(By.XPATH, "//input[@placeholder='CVC']")
cn.send_keys("123")

driver.switch_to.default_content()

time.sleep(3)