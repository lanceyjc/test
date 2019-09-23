from base.base_page import PageAction


class SearchPage(PageAction):
    search_button = {'id': 'com.android.settings:id/search'}
    search_text = {'id': 'android:id/search_src_text'}
    back_button = {'class_name': 'android.widget.ImageButton'}

    def __init__(self, driver):
        PageAction.__init__(self, driver)
        self.click(self.search_button)

    def input_search_text(self, text):
        self.input_text(self.search_text, text)

    def click_back(self):
        self.click(self.back_button)
