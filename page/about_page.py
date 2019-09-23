from base.base_page import PageAction


class AboutPage(PageAction):
    about_button = {'xpath': 'text,关于手机'}
    mobile_info_button = {'xpath': 'text,状态信息'}

    def __init__(self, driver):
        PageAction.__init__(self, driver)
        self.click(self.about_button)

    def click_mobile_info(self):
        self.click(self.mobile_info_button)

    def find_mobile_info(self, text):
        for ele in self.elements({'id': 'android:id/summary'}):
            if text in ele.text:
                break
        else:
            raise print("%s没找到！" % text)
