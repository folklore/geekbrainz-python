number = int(input('Введите число для проверки на простоту: '))

if number < 1:
    print('Введите число больше 0')
elif number > 100_000:
    print('Введите число меньше 100000')
elif number == 1:
    print('1 число простое!')
else:
    for x in range(number - 2):
        if(number % (x + 2) == 0):
            print(f'{number} число составное!')

            quit()

    print(f'{number} число простое!')

# Введите число для проверки на простоту: 13
# 13 число простое!

