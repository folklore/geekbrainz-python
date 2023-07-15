names = ['Кирилл', 'Стас', 'Капитан Джек Воробей']
salaries = [30_000, 10_000, 20_000]
bonuses = ['99.35%', '50.15%', '75.25%']

# statement = {name: salary + salary * float(bonus.replace('%', '')) / 100 for name, salary, bonus in zip(names, salaries, bonuses)}

statement = {}

for name, salary, bonus in zip(names, salaries, bonuses):
    statement[name] = salary + salary * float(bonus.replace('%', '')) / 100

print(statement)

# {'Кирилл': 59805.0, 'Стас': 15015.0, 'Капитан Джек Воробей': 35050.0}
