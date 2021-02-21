import json

with open('test.json', 'r') as file:
    data_dict =  json.load(file)
print(data_dict['widget'])


with open('widget.json', 'w') as file2:
    json.dump(data_dict['widget'], file2)
