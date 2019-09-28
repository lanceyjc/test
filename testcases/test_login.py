import allure, pytest
from base.base_driver import android_driver
from page.login_page import LoginPage
from base.base_yaml import get_yaml_data

login_data = get_yaml_data('login_data')


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
        allure.MASTER_HELPER.attach('输入账号', user)
        self.login_page.input_user(user)
        allure.MASTER_HELPER.attach('输入密码', password)
        self.login_page.input_password(password)
        allure.MASTER_HELPER.step('点击登录')
        self.login_page.click_login_button()
