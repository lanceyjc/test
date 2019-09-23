import yaml,os


def get_yaml_data(file_name):
    """
    :param file_name: the yaml file name
    :return: data
    """
    path = os.getcwd() + '\\data\\' + file_name + '.yml'
    with open(path, 'r') as f:
        return yaml.safe_load(f)


if __name__ == '__main__':
    print(get_yaml_data('search_data'))
