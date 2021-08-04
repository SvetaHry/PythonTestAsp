from src.main.pyhton.utils.constants.DeviceCapabilities import device_capabilities, appiumHost, Devices
from appium import webdriver

def get_driver(device_type=None):

    if device_type is None:
        raise ValueError('Device type not specified')

    if not isinstance(device_type, Devices):
        raise ValueError('device_type should be instance of Devices enum')

    if device_type not in device_capabilities:
        raise ValueError('Device capabilities for "{}" device not defined'.format(device_type.value))

    capabilities = device_capabilities[device_type]

    return webdriver.Remote(appiumHost, capabilities)
