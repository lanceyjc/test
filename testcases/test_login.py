import allure
import pytest
from base.base_driver import android_driver
from base.base_yaml import get_yaml_data
from page.login_page import LoginPage

desired_caps = android_driver()[1]
login_data = get_yaml_data('login_data')

# allure.MASTER_HELPER.environment(app_package=desired_caps['appPackage'])
# allure.MASTER_HELPER.environment(app_activity=desired_caps['appActivity'])
# allure.MASTER_HELPER.environment(platform_name=desired_caps['platformName'])
for cap in desired_caps:
    allure.MASTER_HELPER.environment(cap)


class TestLogin:
    def setup(self):
        self.login_page = LoginPage(android_driver())

    def teardown(self):
        self.login_page.driver.quit()
        del self.login_page

    @pytest.mark.parametrize('account', login_data['test_login'])
    @allure.MASTER_HELPER.feature('测试用例：登录功能')
    def test_login(self, account):
        commit = account[0]
        user = account[1]
        password = account[2]
        toast = account[3]
        allure.MASTER_HELPER.description(commit)
        # enter the user
        allure.MASTER_HELPER.attach('输入账号', user)
        self.login_page.input_user(user)
        # enter the password
        allure.MASTER_HELPER.attach('输入密码', password)
        self.login_page.input_password(password)
        # click the login button
        self.login_page.click_login_button()
        allure.MASTER_HELPER.attach('断言toast', toast)
        assert self.login_page.is_login(toast)
