import pytest
from base.base_driver import android_driver
from page.network_page import NetworkPage


class TestNetwork:

    def setup(self):
        self.network_page = NetworkPage(android_driver())

    def teardown(self):
        self.network_page.driver.quit()
        del self.network_page

    def test_mobile_network_2g(self):
        self.network_page.click_mobile_network()
        self.network_page.click_first_network()
        self.network_page.click_network_2g()
        self.network_page.screen_shot()
        self.network_page.click_back()

    # @pytest.mark.run(order=0)
    def test_mobile_network_3g(self):
        self.network_page.click_mobile_network()
        self.network_page.click_first_network()
        self.network_page.click_network_3g()
        self.network_page.screen_shot()
        self.network_page.click_back()
