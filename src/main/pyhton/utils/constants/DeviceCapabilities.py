from enum import Enum

# class DeviceCapabilitiesConstants:
appiumHost = "http://127.0.0.1:4723/wd/hub"

# Samsung S10
android_caps = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "Galaxy S10e",
    "automationName": "Appium",
    "app": "/Users/svetlanahrytsenko/Downloads/app-alpha-stage.apk",
    "deviceID": "R28M51Y8DDL"
}

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

# # iPhone X
#     IOS_DEVICE_NAME = "iPhone X"
#     IOS_PLATFORM_VERSION = "14.3.1"
#     IOS_PLATFORM_NAME = "iOS"
#     IOS_XcodeSigningId = "iPhone Developer"
#     IOS_xcodeOrgId = "44GZA2S45U"
#     IOS_AUTOMATION_NAME = "XCUITest"
#     IOS_UDID_DEVICE = "61a22a56a7b3e715bc4a5517d9d839e42e38de63"
#     IOS_BundleId = "com.aspiration.summit.alpha"
#     IOS_APP_PATH = "/Users/svetlanahrytsenko/Aspiration.ipa"
#     IOS_URL = "http://127.0.0.1:4723/wd/hub"

# iPhone UPTech iPhone 7 Plus
#     IOS_DEVICE_NAME = "UPTech iPhone 7 Plus"
#     IOS_PLATFORM_VERSION = "13.6"
#     IOS_PLATFORM_NAME = "iOS"
#     IOS_XcodeSigningId = "iPhone Developer"
#     IOS_xcodeOrgId = "44GZA2S45U"
#     IOS_AUTOMATION_NAME = "XCUITest"
#     IOS_UDID_DEVICE = "2051d1f38b452091216a6a878eac9b8f856d0eae"
#     IOS_APP_PATH = "/Users/svetlanahrytsenko/Aspiration.ipa"
#     IOS_URL = "http://127.0.0.1:4723/wd/hub"

# # Android environment
# import unittest
# from appium import webdriver
#
# desired_caps = dict(
#     platformName='Android',
#     platformVersion='10',
#     automationName='Appium',
#     deviceName='Galaxy S10e',
#     app="/Users/svetlanahrytsenko/Downloads/app-alpha-stage.apk")
# )
# self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# el = self.driver.find_element_by_accessibility_id('item')
# el.click()
#
#
# # iOS environment
# import unittest
# from appium import webdriver
#
# desired_caps = dict(
#     platformName='iOS',
#     platformVersion='13.4',
#     automationName='xcuitest',
#     deviceName='iPhone Simulator',
#     app=PATH('../../apps/UICatalog.app.zip')
# )
#
# self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# el = self.driver.find_element_by_accessibility_id('item')
# el.click()


class Devices(Enum):

    IOS = 'ios'
    ANDROID = 'android'


device_capabilities = {
    Devices.IOS: {
        "platformName": "iOS",
        "platformVersion": "13.6",
        "deviceName": "UPTech iPhone 7 Plus",
        "automationName": "XCUITest",
        "app": "/Users/svetlanahrytsenko/Aspiration.ipa",
        "xcodeSigningId": "iPhone Developer",
        "xcodeOrgId": "44GZA2S45U",
        "udid": "2051d1f38b452091216a6a878eac9b8f856d0eae"
    },
    Devices.ANDROID: {
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "Galaxy S10e",
        "automationName": "Appium",
        "app": "/Users/svetlanahrytsenko/Downloads/app-alpha-stage.apk",
        "deviceID": "R28M51Y8DDL"
    }
}

