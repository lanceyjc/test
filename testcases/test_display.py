import pytest
from base.base_driver import android_driver
from page.display_page import DisplayPage


class TestDisplay:

    def setup(self):
        self.display_page = DisplayPage(android_driver())

    def teardown(self):
        self.display_page.driver.quit()
        del self.display_page

    @pytest.mark.parametrize('a',['网络'])
    def test_mobile_search(self, a):
        # 点击放大镜
        self.display_page.click_search()
        # 输入数据
        self.display_page.input_search_text(a)
        self.display_page.screen_shot()
        self.display_page.clear_search_text()
        # 点击返回
        self.display_page.click_back()
