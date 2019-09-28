import allure, pytest
from base.base_driver import android_driver
from page.login_page import LoginPage


class TestLogin:
    def setup(self):
        self.login_page = LoginPage(android_driver())

    def teardown(self):
        self.login_page.driver.quit()
        del self.login_page

    @allure.MASTER_HELPER.feature('测试用例：登录功能')
    @allure.MASTER_HELPER.testcase('测试登录功能')
    @pytest.mark.parametrize('account',[('13590248053','YJC520')])
    def test_login(self, account):
        user = account[0]
        password = account[1]
        allure.MASTER_HELPER.attach('输入账号', user)
        self.login_page.input_user(user)
        allure.MASTER_HELPER.attach('输入密码', password)
        self.login_page.input_password(password)
        allure.MASTER_HELPER.step('点击登录')
        self.login_page.click_login_button()
