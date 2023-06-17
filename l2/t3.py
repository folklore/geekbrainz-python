a = input('Введите первую дробь: ')
b = input('Введите вторую дробь: ')

a_n, a_d = [int(v) for v in a.split('/')]
b_n, b_d = [int(v) for v in b.split('/')]

denominator = 1

while True:
    if denominator % a_d == 0 and denominator % b_d == 0:
        break
    else:
        denominator += 1

a_f = denominator / a_d
b_f = denominator / b_d

numerator = a_n * a_f + b_n * b_f

print(f'Сумма: {int(numerator)}/{denominator}')

print(f'Произведение: {a_n * b_n}/{a_d * b_d}')

# Введите первую дробь: 1/2
# Введите вторую дробь: 1/3
# Сумма: 5/6
# Произведение: 1/6
