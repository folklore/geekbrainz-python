import random


things = []

# Словарь изначально составлен для задания 4.
with open('things_map.txt', 'r') as file:
    for line in file.readlines():
        thing, weight = line.replace('\n', '').split(' ')
        things.append(thing)

print(f"Вещи: {', '.join(things)}")
print()


class Tourist():
    def __init__(self, name):
        self.name = name
        self.things = set()


kirill = Tourist('Кирилл')
stas = Tourist('Стас')
capitan_jack_sparrow = Tourist('Капитан Джек Воробей')

tourists = [kirill, stas, capitan_jack_sparrow]

for tourist in tourists:
    random.shuffle(things)
    tourist.things = set(things[0:5])

    print(f"{tourist.name}: {', '.join(tourist.things)}")
print()


each = ', '.join(set.intersection(*[tourist.things for tourist in tourists]))
print(f'Какие вещи взяли все три друга: {each}')
print()


print('Какие вещи уникальны, есть только у одного друга:')
for i, tourist in enumerate(tourists):
    rotate_tourists = tourists[i:] + tourists[:i]
    uniq = ', '.join(set.difference(*[tourist.things for tourist in rotate_tourists]))
    print(f'  {tourist.name}: {uniq}')
print()


print('Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует:')
for i, tourist in enumerate(tourists):
    rotate_tourists = tourists[i:] + tourists[:i]
    intersection = set.intersection(*[tourist.things for tourist in rotate_tourists[1:]])
    print(f"  {tourist.name}: {', '.join(intersection - tourist.things)}")

# Вещи: Пиво, Консервы, Спальник, Фонарь, Дождевик, Радио, Посуда, Нож, Горелка, Термос, Топор, Стул

# Кирилл: Радио, Посуда, Дождевик, Топор, Нож
# Стас: Горелка, Консервы, Топор, Нож, Спальник
# Капитан Джек Воробей: Горелка, Посуда, Фонарь, Нож, Пиво

# Какие вещи взяли все три друга: Нож

# Какие вещи уникальны, есть только у одного друга:
#   Кирилл: Радио, Дождевик
#   Стас: Консервы, Спальник
#   Капитан Джек Воробей: Фонарь, Пиво

# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует:
#   Кирилл: Горелка
#   Стас: Посуда
#   Капитан Джек Воробей: Топор
