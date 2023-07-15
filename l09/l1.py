import os
import sys


from random import randint
from csv import writer as CSVwriter, reader as CSVreader
from json import dumps as JSONdumper


VARIABLES_FILE_NAME = 'variables.csv'
RESULTS_FILE_NAME = 'results.json'


with open(VARIABLES_FILE_NAME, 'w') as f:
    csv = CSVwriter(f)

    for _ in range(randint(100, 1001)):
        row = [randint(1, 11), randint(3, 9), randint(5, 7)]
        csv.writerow(row)
    csv.writerow([2, 4, 2])


def saver(func):
    def wrapper():
        results = func()

        with open(RESULTS_FILE_NAME, 'w') as f:
            f.write(JSONdumper(results, indent = 2) )
        return results
    return wrapper


def tester(func):
    def wrapper():
        results = []

        with open(VARIABLES_FILE_NAME, 'r') as f:
            csv = CSVreader(f)

            for row in csv:
                result = func(*[int(i) for i in row])

                if result:
                    results.append(result)
        return results
    return wrapper


@saver
@tester
def quadratic(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return None # Без комплексных корней
    elif discriminant == 0:
        x = -b / (2 * a)

        return x, ''
    else:
        x1 = (-b + discriminant**0.5) / (2 * a)
        x2 = (-b - discriminant**0.5) / (2 * a)

        return x1, x2


print(quadratic())
