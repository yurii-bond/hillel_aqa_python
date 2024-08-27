# GET-запит

import requests

url = 'http://jsonplaceholder.typicode.com/posts/1/comments'
# response = requests.get(url)
response = requests.request('GET', url)

# Перевірка статус-коду
if response.status_code == 200:
    data = response.json()  # отримання даних у форматі JSON
    print('Отримано дані:', data)
else:
    print('Помилка. Статус-код:', response.status_code)


# GET with params
params = {'postId': 1, 'email': 'Nikita@garfield.biz'}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print('Отримано дані:', data)
else:
    print('Помилка запиту:', response.status_code)


# POST
url = 'http://jsonplaceholder.typicode.com/posts'
data_to_send = {'userId': 10, 'id': 1, 'title': 'Some title'}

response = requests.post(url, data=data_to_send)

# Перевірка статус-коду
if response.status_code == 201:
    created_data = response.json()  # отримання даних у форматі JSON
    print('Створено дані:', created_data)
else:
    print('Помилка. Статус-код:', response.status_code)


# PUT
url = 'http://jsonplaceholder.typicode.com/posts/1'
data_to_send = {'userId': 10, 'id': 1, 'title': 'New title'}

response = requests.put(url, data=data_to_send)

# Перевірка статус-коду
if response.status_code == 200:
    updated_data = response.text  # отримання даних у форматі текст
    print('Оновлено дані:', updated_data)
else:
    print('Помилка. Статус-код:', response.status_code)


# DELETE
url = 'http://jsonplaceholder.typicode.com/posts/1'
params = {'userId': 10, 'id': 101, 'title': 'New title'}
response = requests.delete(url, params=params)

# Перевірка статус-коду
if response.status_code == 200:
    print('Дані успішно видалено')
else:
    print('Помилка. Статус-код:', response.status_code)

# Requests
# requests.request(method='DELETE')
# requests.delete()

# requests.post(url='urel', data='sfsdf', json='{}', files=filesobj, headers=, cookies=, cert=, timeout=10)

# requests.get(url, auth={'login': 'password'})

# Session
# Створення сесії
session = requests.Session()

# Встановлення cookies для сесії
cookies = {'user_id': '12345', 'session_id': 'abcdef'}
session.cookies.update(cookies)

# Виконання запитів за допомогою сесії
response1 = session.get('https://example.com/page1')
response2 = session.get('https://example.com/page2')


# Adapter
from requests.adapters import HTTPAdapter

# Створення сесії
session = requests.Session()

# Налаштування адаптера з кількістю спроб 3
adapter = HTTPAdapter(max_retries=3)

# Додавання адаптера до сесії
session.mount('http://', adapter)
session.mount('https://', adapter)

# Виконання запиту з автоматичною повторною спробою
response = session.get('https://example.com')

# Відкриття файлу для завантаження
with open('file_to_upload.txt', 'rb') as file:
    files = {'file': file}

    # Виконання POST-запиту з файлом
    response = requests.post('https://example.com/upload', files=files)

# Обробка відповіді
print(response.text)

# Виконання GET-запиту для скачування файлу
response = requests.get('https://example.com/download')

# Запис файлу на диск
with open('downloaded_file.txt', 'wb') as file:
    file.write(response.content)


# SSL
response = requests.get('https://your-server.com', verify=False)
print(response.text)

