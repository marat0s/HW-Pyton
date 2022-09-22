import os

dir_path = r'D:/newNewDirectory'

list = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        list.append(path)
print(list)
