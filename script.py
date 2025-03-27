import requests
import json

letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

import itertools

combinations = itertools.product(letters, repeat=3)

combinations = filter(lambda x: x[0] != x[1] and x[1] != x[2], combinations)

for combination in combinations:
    a = ''.join(combination)
    if (a[0] in "абвгдеёжз"):
        continue
    url = f"https://pass.rw.by/ru/ajax/autocomplete/search/?term={a}"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            print(a, len(data))
        except requests.exceptions.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e}")

    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
