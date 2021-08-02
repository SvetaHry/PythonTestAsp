# from src.main.pyhton.utils.constants import logins_and_passowords

from unittest import TestCase
from src.main.pyhton.pages.ios import LoginIOS
from appium import webdriver
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from src.main.pyhton.pages.ios import LoginIOS


appiumHost = "http://127.0.0.1:4723/wd/hub"

ios_caps = {
    "platformName": "iOS",
    "platformVersion": "13.6",
    "deviceName": "UPTech iPhone 7 Plus",
    "automationName": "XCUITest",
    "app": "/Users/svetlanahrytsenko/Aspiration.ipa",
    "xcodeSigningId": "iPhone Developer",
    "xcodeOrgId": "44GZA2S45U",
    "udid": "2051d1f38b452091216a6a878eac9b8f856d0eae"
}

# def FindMainLogIn():
#     driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", ios_caps)
#     wait = WebDriverWait(driver, 10)
#     elem = wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//XCUIElementTypeButton[@name="LOG IN"]')))
#     # (driver.find_element_by_xpath('//XCUIElementTypeButton[@name="LOG IN"]'))
#     print("elem is found")
#
# FindMainLogIn()

class LoginIOSTest():
    log = LoginIOS.LoginIOS.FindMainLogIn()

