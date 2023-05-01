from base.base_page import PageAction


class AboutPage(PageAction):
    about_button = {'xpath': 'text,关于手机'}
    mobile_info_button = {'xpath': 'text,Android 版本'}

    def __init__(self, driver):
        PageAction.__init__(self, driver)
        self.click(self.about_button, swipe=True)

    def click_mobile_info(self):
        self.click(self.mobile_info_button)

    def find_mobile_info(self, text):
        for ele in self.element({'id': 'android:id/summary'}, swipe=True):
            if text in ele.text:
                break
        else:
            raise print("%s没找到！" % text)
