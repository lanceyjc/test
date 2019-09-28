from base.base_driver import android_driver
from page.login_page import LoginPage


class TestLogin:
    def setup(self):
        self.login_page = LoginPage(android_driver())

    def teardown(self):
        self.login_page.driver.quit()
        del self.login_page

    def test_login(self):
        self.login_page.input_user('13590248053')
        self.login_page.input_password('YJC520')
