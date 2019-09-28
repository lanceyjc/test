from base.base_page import PageAction


class LoginPage(PageAction):
    my_button = {'xpath': ('resource-id, com.tpshop.malls:id/mine_tv', 'text, 我的')}
    user_icon = {'id': 'com.tpshop.malls:id/head_img'}
    user_text = {'id': 'com.tpshop.malls:id/mobile_et'}
    password_text = {'id': 'com.tpshop.malls:id/pwd_et'}
    login_button = {'id': 'com.tpshop.malls:id/login_tv'}

    def __init__(self, driver):
        PageAction.__init__(self, driver)
        self.__jump_2_login_page()

    def __jump_2_login_page(self):
        self.click(self.my_button)
        self.click(self.user_icon)

    def input_user(self, text):
        self.input_text(self.user_text, text)

    def input_password(self, text):
        self.input_text(self.password_text, text)

    def click_login_button(self):
        self.click(self.login_button)
