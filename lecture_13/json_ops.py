import json


json_str = '{"name": "John", "age": 30, "city": "New York"}'

with open('data.json', 'w') as file:
    data = json.loads(json_str)
    print(data)
    file.write(json.dumps(data, indent=3))


json_data = {
   "name": "John",
   "age": 30,
   "city": "New York"
}

with open('data2.json', 'w') as file:
    json.dump(json_data, file, indent=2)

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)

try:
    with open('data3.json', 'r') as _file:
        data = json.load(_file)
except json.JSONDecodeError as e:
    print('Json deserialization error: ', e)


try:
    with open('data4.json', 'w') as _file:
        json.dump(data, _file)
except PermissionError as e:
    print('File Permission Error: ', e)


try:
    with open('dat.json', 'r') as _file:
        data = json.load(_file)
except FileNotFoundError as e:
    print('File not found error: ', e)
