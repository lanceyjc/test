import yaml

with open("./test.yml", "r") as f:
    data = yaml.full_load(f)
    print(data)
