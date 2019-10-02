import os


def clear_shot():
    # path = os.path.split(os.getcwd())[0] + '\\screenshot'
    path = os.getcwd() + '\\screenshot'
    for file_name in os.listdir(path):
        if file_name.endswith('.png'):
            os.remove(path + '\\' + file_name)


if __name__ == '__main__':
    pass
