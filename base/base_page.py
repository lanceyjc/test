import base64
import os
import time

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class PageAction:

    def __init__(self, driver):
        self._url = driver[0]
        self._desired_caps = driver[1]
        self.driver = webdriver.Remote(self._url, self._desired_caps)
        self._LOCATOR_MAP = {'id': By.ID,
                             'xpath': By.XPATH,
                             'class_name': By.CLASS_NAME}
        self.__width = self.driver.get_window_size()['width']
        self.__height = self.driver.get_window_size()['height']

    # 常用操作
    def click(self, loc, swipe=False):
        self.element(loc, swipe).click()

    def input_text(self, loc, text, swipe=False):
        self.element(loc, swipe).send_keys(text)

    def clear_text(self, loc, swipe=False):
        self.element(loc, swipe).clear()

    # 获取元素属性
    def get_text(self, loc, swipe=False):
        return self.element(loc, swipe).text

    def get_attribute(self, loc, value, swipe=False):
        return self.element(loc, swipe).get_attribute(value)

    def get_location(self, loc, swipe=False):
        return self.element(loc, swipe).location

    # 滑动操作
    def swipe(self, start_x, start_y, end_x, end_y, duration=None):
        self.driver.swipe(self.__width * start_x, self.__height * start_y,
                          self.__width * end_x, self.__height * end_y, duration)

    def scroll(self, origin_ele_loc, destination_ele_loc, duration=None, swipe=False):
        origin_ele = self.element(origin_ele_loc, swipe)
        destination_ele = self.element(destination_ele_loc, swipe)
        self.driver.scroll(origin_ele, destination_ele, duration)

    def drag_and_drop(self, origin_ele_loc, destination_ele_loc, swipe=False):
        origin_ele = self.element(origin_ele_loc, swipe)
        destination_ele = self.element(destination_ele_loc, swipe)
        self.driver.drag_and_drop(origin_ele, destination_ele)

    def swipe_page(self):
        self.swipe(0.5, 0.75, 0.5, 0.25, 1500)

    # 常用KeyCode
    def mobile_back_key(self):
        self.driver.keyevent(4)

    # 元素定位
    def element(self, kw, swipe):
        """
        find_element
        :param swipe: bool, swipe page or not
        :param kw: 'locator':'value'
        :return: element
        """
        if not kw:
            raise ValueError("Please specify a locator")
        if len(kw) > 1:
            raise ValueError("Please specify only one locator")
        k, v = next(iter(kw.items()))
        if k == 'xpath':
            v = self.make_xpath_feature(v)
        while True:
            try:
                return WebDriverWait(self.driver, 1, 0.2).until(lambda x: x.find_element(self._LOCATOR_MAP[k], v))
            except TimeoutException:
                if swipe:
                    before_swipe = self.driver.page_source
                    self.swipe_page()
                    if self.driver.page_source == before_swipe:
                        raise NoSuchElementException
                else:
                    raise NoSuchElementException

    def elements(self, kw, swipe):
        """
        find_elements
        :param swipe: bool, swipe page or not
        :param kw: 'locator':'value'
        :return: element list
        """
        if not kw:
            raise ValueError("Please specify a locator")
        if len(kw) > 1:
            raise ValueError("Please specify only one locator")
        k, v = next(iter(kw.items()))
        if k == 'xpath':
            v = self.make_xpath_feature(v)
        while True:
            try:
                return WebDriverWait(self.driver, 1, 0.2).until(lambda x: x.find_elements(self._LOCATOR_MAP[k], v))
            except TimeoutException:
                if swipe:
                    before_swipe = self.driver.page_source
                    self.swipe_page()
                    if self.driver.page_source == before_swipe:
                        raise NoSuchElementException
                else:
                    raise NoSuchElementException

    # 截图
    def screen_shot(self):
        time.sleep(0.5)
        current_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        pic_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
                    + '\\reports\\screenshots\\'
                    + current_time + '.png')
        self.driver.get_screenshot_as_file(pic_path)

    # 发送数据到手机
    def send_file(self, path, data_source):
        data = str(base64.b64encode(data_source.encode('utf-8')), 'utf-8')
        self.driver.push_file(path, data)

    # 从手机中获取文件
    def get_file(self, path):
        data = self.driver.pull_file(path)
        return str(base64.b64decode(data), 'utf-8')

    # 拼接xpath
    @staticmethod
    def __xpath_feature(xpath, feature):
        key_index = 0
        value_index = 1
        option_index = 2
        if len(feature) == 2 or (len(feature) == 3 and feature[option_index].strip() == '0'):
            return xpath + 'contains(@' + feature[key_index].strip() + ',"' + feature[value_index].strip() + '")'
        elif len(feature) == 3 and feature[option_index].strip() == '1':
            return xpath + '@' + feature[key_index].strip() + '="' + feature[value_index].strip() + '"'
        else:
            raise ValueError('check the feature')

    # 处理xpath输入
    def make_xpath_feature(self, args):
        xpath_start = '//*['
        xpath_end = ']'
        xpath = ''
        if not args:
            raise ValueError("Please enter the feature")
        elif isinstance(args, str):
            # support original xpath locator
            if args.startswith('//'):
                return args
            # support single condition
            feature = args.split(',')
            xpath = self.__xpath_feature(xpath, feature)
            return xpath_start + xpath + xpath_end
        elif len(args) > 1:
            # support multiple conditions
            for fs in args:
                feature = fs.split(',')
                xpath = self.__xpath_feature(xpath, feature) + 'and '
            return xpath_start + xpath[0:-4] + xpath_end
        else:
            raise ValueError("check the feature")
