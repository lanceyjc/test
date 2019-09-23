# import pytest
from page.about_page import AboutPage
from base.base_driver import android_driver


class TestAbout:

    def setup(self):
        self.about_page = AboutPage(android_driver())

    def teardown(self):
        self.about_page.driver.quit()
        del self.about_page

    def test_mobile_info(self):
        self.about_page.click_mobile_info()
        self.about_page.screen_shot()
        self.about_page.mobile_back_key()

    # @pytest.mark.parametrize('text', ['Samsung'])
    # def test_xinghao(self, text):
    #     self.about_page.find_mobile_info(text)
