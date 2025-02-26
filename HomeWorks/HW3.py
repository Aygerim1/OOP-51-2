# Библиотека 'requests' позволяет отправлять HTTP-запросы.
# Она используется для работы с веб-страницами или API.
# В этом примере мы используем 'requests' для отправки GET-запроса на сайт example.com.
# Библиотека позволяет легко получать данные с интернета и работать с ними.
import requests

response = requests.get('https://example.com')

if response.status_code == 200:
    print("Запрос был успешным!")
    print("Содержимое страницы:", response.text)
else:
    print("Ошибка при запросе, статус код:", response.status_code)