import pytest
from base.base_driver import android_driver
from page.search_page import SearchPage
from base.base_yaml import get_yaml_data

search_data = get_yaml_data('search_data')


class TestSearch:

    def setup(self):
        self.search_page = SearchPage(android_driver())

    def teardown(self):
        self.search_page.driver.quit()
        del self.search_page

    @pytest.mark.parametrize('text', search_data['test_search'])
    def test_search(self, text):
        self.search_page.input_search_text(text)
        self.search_page.screen_shot()
        self.search_page.click_back()
