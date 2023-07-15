import time


class Archive():
    """Хранит пару свойств. Например, число и строку.
При создании нового экземпляра класса,
старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов"""


    STORAGE = {}


    def __init__(self, number, text):
        self.STORAGE[time.time()] = [number, text]

        self.number = number
        self.text = text


    def __str__(self):
        return f'{self.number = }, {self.text = }'


    def __repr__(self):
        return f'Archive({self.number}, "{self.text}")'


archive = Archive(1, 'STR')
print(archive)

print(Archive.__doc__)
print(repr(archive))

print(Archive.STORAGE)
print(archive.STORAGE)


# self.number = 1, self.text = 'STR'
# Хранит пару свойств. Например, число и строку.
# При создании нового экземпляра класса,
# старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# Archive(1, "STR")
# {1689429881.4009888: [1, 'STR']}
# {1689429881.4009888: [1, 'STR']}
