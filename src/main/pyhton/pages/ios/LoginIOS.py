from src.main.pyhton.utils.constants import constants
from appium import webdriver
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.tests.pyhton.ios import LoginIOSTests

class LoginIOS:

    btnMainLogIn = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="LOG IN"]')

    def FindMainLogIn(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub")
        wait = WebDriverWait(driver, 10)
        elem = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//XCUIElementTypeButton[@name="LOG IN"]')))
        # (driver.find_element_by_xpath('//XCUIElementTypeButton[@name="LOG IN"]'))
        print("elem is found")