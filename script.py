import requests
import json

letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

import itertools

combinations = itertools.product(letters, repeat=3)

combinations = filter(lambda x: x[0] != x[1] and x[1] != x[2], combinations)

for combination in combinations:
    a = ''.join(combination)
    url = f"https://pass.rw.by/ru/ajax/autocomplete/search/?term={a}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(a, len(data))

    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
