class ZeroHeightError(AssertionError):
  pass

class SubZeroHeightError(AssertionError):
  pass

def set_height():
    while True:
        try:
            height = int(input('Введите высоту елки: '))
            break
        except ValueError as err:
            print(f'Вероятно вы указали не число: {err}')
    return height

height = set_height()

if height == 0:
    raise ZeroHeightError('Вы ввели 0 (ноль), таких елок нет(')
elif height < 0:
    raise SubZeroHeightError('Вы ввели отрицательную высоту, таких елок нет(')
else:
    for x in range(height):
        margin = ' ' * (height - x)
        side = x * '#'

        level = margin + side + '#' + side
        print(level)
    print()
