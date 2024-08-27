import json
import ssl
from urllib import request, parse, error

url = "https://www.example.com"
# GET
response = request.urlopen(url)
data = response.read()

# print(response)
print(data, 'GET response')

# POST

data = {'key1': 'value1', 'key2': 'value2'}

data = parse.urlencode(data).encode('utf-8')
response = request.urlopen(url=url, data=data)
result = response.read()
print(result, 'POST response')

# PUT
result = None
data_to_send = {'key1': 'value1', 'key2': 'value2'}
# Кодування даних в формат JSON
data_encoded = json.dumps(data_to_send).encode('utf-8')

# Відправлення PUT-запиту з даними у форматі JSON
_request = request.Request(url + '/resource/123', method='PUT', data=data_encoded, headers={'Content-Type': 'application/json'})
print(_request.full_url)
try:
    with request.urlopen(_request) as f:
        result = f.read()
except error.HTTPError as http_error:
    print(http_error)
print(result, 'PUT response')


# DELETE
# Відправлення DELETE-запиту
response = request.Request(url + '/resource/123', method='DELETE')
try:
    with request.urlopen(response) as f:
        result = f.read()
except error.HTTPError as http_error:
    print(http_error)

print(result, "DELETE response")


# headers
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

_request = request.Request(url, headers=headers)
response = request.urlopen(_request)
data = response.read()
print(data, 'Request with headers')


# PARSE
url = "https://www.example.com/path/to/resource?param1=value1&param2=value2"

parsed_url = parse.urlparse(url)

print("Схема:", parsed_url.scheme)
print("Мережева адреса:", parsed_url.netloc)
print("Шлях:", parsed_url.path)
print("Параметри:", parsed_url.params)
print("Запити:", parsed_url.query)
print("Фрагмент:", parsed_url.fragment)

scheme = "https"
netloc = "www.example.com"
path = "/path/to/resource"
params = "param1=value1"
query = "param2=value2"
fragment = "section"

composed_url = parse.urlunparse((scheme, netloc, path, params, query, fragment))

print("Складений URL:", composed_url)

# Self-signed SSL
# Вимкнення перевірки сертифікатів (не рекомендується в продакшні)
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

url = "https://www.example.com"

try:
    # Вказання контексту SSL при використанні urllib
    response = request.urlopen(request.Request(url), context=context)
    print(response.read())
except Exception as e:
    print(f'Помилка: {e}')