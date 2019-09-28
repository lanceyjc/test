import allure, pytest
from base.base_driver import android_driver
from page.login_page import LoginPage
from base.base_yaml import get_yaml_data

login_data = get_yaml_data('login_data')

allure.MASTER_HELPER.environment(app_package='com.tpshop.malls')
allure.MASTER_HELPER.environment(app_activity='.SPMainActivity')
allure.MASTER_HELPER.environment(platform_name='Android')


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
        allure.MASTER_HELPER.description(commit)
        # enter the user
        allure.MASTER_HELPER.attach('输入账号', user)
        self.login_page.input_user(user)
        # enter the password
        allure.MASTER_HELPER.attach('输入密码', password)
        self.login_page.input_password(password)
        # click the login button
        self.login_page.click_login_button()
