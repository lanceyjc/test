import os


def clear_shot():
    # path = os.path.split(os.getcwd())[0] + '\\screenshot'
    try:
        path = os.getcwd() + '\\screenshot'
        for file_name in os.listdir(path):
            if file_name.endswith('.png'):
                os.remove(path + '\\' + file_name)
    except Exception:
        pass


if __name__ == '__main__':
    pass
