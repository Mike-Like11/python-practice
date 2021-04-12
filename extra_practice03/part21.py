import matplotlib.pyplot as plt
import random
import json
import email.utils

with open('https://github.com/true-grue/kispython/blob/main/pract3/failed.json', encoding='utf8') as f:
    table = json.loads(f.read())  # Таблица решений задач

with open('pract3/failed.json', encoding='utf8') as f:
    failed = json.loads(f.read())  # Данные по ошибкам

with open('pract3/messages.json', encoding='utf8') as f:
    messages = json.loads(f.read())  # Полученные сообщения

messages = [(m['subj'].upper(), email.utils.parsedate(m['date'])) for m in messages]
print(messages)
xs = range(0, 10)
# Символ ; здесь используется, чтобы не выводить служебную информацию на экран
plt.plot(xs, [random.random() for _ in xs]);
plt.show()