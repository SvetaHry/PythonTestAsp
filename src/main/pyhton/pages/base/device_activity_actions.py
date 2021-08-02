from appium import webdriver

# from selenium.webdriver.common.by import By

from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
import typing

class Locators(object):

    LOCATOR_ONE = (MobileBy.ACCESSIBILITY_ID, 'accessibility')
    LOCATOR_TWO = (MobileBy.XPATH, 'xpath_value')


