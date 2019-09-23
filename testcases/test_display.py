import pytest,allure
from base.base_driver import android_driver
from page.display_page import DisplayPage


class TestDisplay:

    def setup(self):
        self.display_page = DisplayPage(android_driver())

    def teardown(self):
        self.display_page.driver.quit()
        del self.display_page

    @allure.MASTER_HELPER.testcase('测试搜索功能')
    @allure.MASTER_HELPER.feature('测试用例：搜索')
    @pytest.mark.parametrize('a',['网络'])
    def test_mobile_search(self, a):
        allure.MASTER_HELPER.attach('点击放大镜')
        self.display_page.click_search()
        allure.MASTER_HELPER.attach('输入数据：网络')
        self.display_page.input_search_text(a)
        self.display_page.screen_shot()
        self.display_page.clear_search_text()
        allure.MASTER_HELPER.attach('点击返回')
        self.display_page.click_back()
