import os, sys
sys.path.append(os.getcwd())

from base.clear_shot import clear_shot
# from base.base_driver import env_config


def make_screenshot_dir():
    screenshot_path = os.getcwd() + '\\screenshot'
    if not os.path.exists(screenshot_path):
        os.mkdir(screenshot_path)
    else:
        clear_shot()


# env_config()
make_screenshot_dir()
