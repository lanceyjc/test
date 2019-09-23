from base.base_page import PageAction


class DisplayPage(PageAction):
    # page elements
    display_button = {'xpath': 'text,显示'}
    search_button = {'id': 'com.android.settings:id/search'}
    search_text = {'id': 'android:id/search_src_text'}
    back_button = {'class_name': 'android.widget.ImageButton'}

    # setup
    def __init__(self, driver):
        PageAction.__init__(self, driver)
        self.click(self.display_button)

    # actions
    def click_search(self):
        self.click(self.search_button)

    def input_search_text(self, text):
        self.input_text(self.search_text, text)

    def click_back(self):
        self.click(self.back_button)

    def clear_search_text(self):
        self.clear_text(self.search_text)
