import csv


with open('data.csv', newline='', ) as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        print(row.__len__())
        print(row)


with open('data.csv', newline='') as file:
    dict_csv = csv.DictReader(file)
    for _dict in dict_csv:
        print(_dict)


data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ["Alice", 25, 'Chicago'],
    ['Bob', 35, 'Los Angeles']
]

with open('output.csv', 'w', newline='') as csvf:
    writer = csv.writer(csvf, delimiter=';')
    writer.writerows(data)
