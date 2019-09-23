import os
import time


# xpath
def make_xpath_with_feature(*args, contain=True, multi_condition=False):
    """
    create the xpath feature
    :param args: enter feature like 'text,settings'
    :param contain: contain or accurate
    :param multi_condition: single condition or multiple conditions
    :return:xpath path
    """
    if not args:
        raise ValueError("Please enter the feature")
    if len(args) == 1 and not multi_condition:
        key, value = args[0].split(',')
        if contain:
            return '//*[contains(@' + key + ',"' + value + '")]'
        else:
            return '//*[@' + key + '="' + value + '"]'
    elif len(args) > 1 and multi_condition:
        xpath = '//*['
        for feature in args:
            key, value = feature.split(',')
            xpath = xpath + '@' + key + '="' + value + '"and'
        return xpath[0:-3] + ']'
    else:
        raise ValueError("Please check the features and parameters")


# screen shot
def screen_shot(driver):
    time.sleep(0.5)
    current_time = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    pic_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
                + '\\reports\\screenshots\\'
                + current_time + '.png')
    driver.get_screenshot_as_file(pic_path)
    # time.sleep(1)
