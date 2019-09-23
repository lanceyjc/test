import os

path = os.path.split(os.getcwd())[0] + '\\reports\\screenshots'
for file_name in os.listdir(path):
    if file_name.endswith('.png'):
        os.remove(path + '\\' + file_name)

