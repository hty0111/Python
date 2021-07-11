import json

numbers = [0, 1, 2, 3]
filename = 'myJson.json'
with open(filename, 'w') as f1:
    json.dump(numbers, f1)      #存储数据
with open(filename) as f2:
    print(json.load(f2))        #读取数据

