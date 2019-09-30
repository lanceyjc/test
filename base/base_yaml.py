import yaml,os


def get_yaml_data_file(file_name):
    """
    :param file_name: the yaml file name
    :return: data
    """
    path = os.getcwd() + '\\data\\' + file_name + '.yml'
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def data_with_key(key):
    """
    change a dict to a list
    :param key: data dict
    :return: data list
    """
    case_data_list = list()
    for case_data in key:
        key[case_data]['test_no'] = case_data
        case_data_list.append(key[case_data])
    return case_data_list


if __name__ == '__main__':
    print(get_yaml_data_file('search_data'))
