number = int(input('Задайте число: '))


def fib(n: int):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


gen = fib(number)
print(gen)

for fib_number in gen:
    print(fib_number, end=' ')

# Задайте число: 21
# <generator object fib at 0x1042ae890>
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
