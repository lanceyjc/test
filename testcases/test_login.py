import allure
import pytest
from base.base_driver import android_driver
from base.base_yaml import get_yaml_data_file
from base.base_yaml import data_with_key
from page.login_page import LoginPage


login_data = get_yaml_data_file('login_data')


class TestLogin:
    def setup(self):
        self.login_page = LoginPage(android_driver())

    def teardown(self):
        self.login_page.driver.quit()
        del self.login_page

    @pytest.mark.parametrize('account', data_with_key(login_data['test_login']))
    @allure.MASTER_HELPER.feature('测试用例：登录功能')
    def test_login(self, account):
        test_no = account['test_no']
        commit = account['commit']
        username = account['username']
        password = account['password']
        toast = account['toast']
        allure.MASTER_HELPER.description('{0}: {1}'.format(test_no, commit))
        # enter the username
        allure.MASTER_HELPER.attach('输入账号', username)
        self.login_page.input_user(username)
        # enter the password
        allure.MASTER_HELPER.attach('输入密码', password)
        self.login_page.input_password(password)
        # click the login button
        self.login_page.click_login_button()
        allure.MASTER_HELPER.attach('断言toast', toast)
        img_path, toast_flag = self.login_page.is_toast_exist(toast)
        with open(img_path, 'rb') as img_data:
            img = img_data.read()
        allure.MASTER_HELPER.attach('断言截图', img, allure.MASTER_HELPER.attach_type.PNG)
        assert toast_flag
