"""
存放手机连接的参数和测试环境配置
"""
import allure

# 'automationName': 'Uiautomator2'

def android_driver():
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '5.1',
                    'appPackage': 'com.tpshop.malls',
                    'appActivity': '.SPMainActivity',
                    'deviceName': '192.168.182.105:5555',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True,
                    'automationName': 'Uiautomator2'}
    url = 'http://localhost:4723/wd/hub'
    return url, desired_caps


def ios_driver():
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '5.1',
                    'appPackage': 'com.android.settings',
                    'appActivity': '.Settings',
                    'deviceName': '192.168.56.101:5555',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True}
    url = 'http://localhost:4723/wd/hub'
    return url, desired_caps


def env_config():
    desired_caps = android_driver()[1]
    allure.MASTER_HELPER.environment(app_package=desired_caps['appPackage'])
    allure.MASTER_HELPER.environment(app_activity=desired_caps['appActivity'])
    allure.MASTER_HELPER.environment(platform_name=desired_caps['platformName'])
    allure.MASTER_HELPER.environment(platform_version=desired_caps['platformVersion'])
    allure.MASTER_HELPER.environment(device_name=desired_caps['deviceName'])
