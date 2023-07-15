import random


things_map = {}

with open('things_map.txt', 'r') as file:
    for line in file.readlines():
        thing, weight = line.replace('\n', '').split(' ')

        things_map[thing] = int(weight)

print(things_map)

capacity = int(input('Введите размер рюкзака: '))


class Backpack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.things_map = {}


while True:
    backpack = Backpack(capacity)

    things = list(things_map.keys())
    random.shuffle(things)

    for thing in things:
        weight = things_map[thing]

        if weight <= backpack.capacity:
            backpack.things_map[thing] = weight
            backpack.capacity -= weight

    if backpack.capacity == 0 or backpack.things_map == things_map:
        break

print(backpack.things_map)
print(backpack.capacity)
