import yaml


def data_with_key(key):
    case_data_list = list()
    for case_data in key:
        key[case_data]['test_no'] = case_data
        case_data_list.append(key[case_data])
    return case_data_list


with open("./login_data.yml", "r") as f:
    data = yaml.full_load(f)['test_login']
print(data_with_key(data))
