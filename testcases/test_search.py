import pytest, allure
from base.base_driver import android_driver
from page.search_page import SearchPage
from base.base_yaml import get_yaml_data_file
from base.base_yaml import data_with_key

search_data = get_yaml_data_file('search_data')


class TestSearch:

    def setup(self):
        self.search_page = SearchPage(android_driver())

    def teardown(self):
        self.search_page.driver.quit()
        del self.search_page

    @allure.MASTER_HELPER.feature('测试用例：搜索')
    @pytest.mark.parametrize('text', data_with_key(search_data['test_search']))
    def test_search(self, text):
        test_no = text['test_no']
        search_text = text['text']
        allure.MASTER_HELPER.description(test_no)
        allure.MASTER_HELPER.attach('输入数据', search_text)
        self.search_page.input_search_text(search_text)
        self.search_page.screen_shot()
        self.search_page.click_back()
