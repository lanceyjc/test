from base.base_page import PageAction


class NetworkPage(PageAction):
    # page element
    more_button = {'xpath': 'text,更多'}
    mobile_network_button = {'xpath': ('text,移动网络,1', 'index,0,1')}
    first_network_button = {'xpath': 'text,首选网络类型'}
    network_2g_button = {'xpath': 'text,2G'}
    network_3g_button = {'xpath': 'text,3G'}
    back_button = {'class_name': 'android.widget.ImageButton'}

    # setup
    def __init__(self, driver):
        PageAction.__init__(self, driver)
        self.click(self.more_button)

    # actions
    def click_mobile_network(self):
        self.click(self.mobile_network_button)

    def click_first_network(self):
        self.click(self.first_network_button)

    def click_network_2g(self):
        self.click(self.network_2g_button)

    def click_network_3g(self):
        self.click(self.network_3g_button)

    def click_back(self):
        self.click(self.back_button)
