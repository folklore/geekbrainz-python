class Animal():
    TYPES_STORAGE = []
    LOCALE_NAME_CLASS = 'Животное'

    def __init__(self, name):
        self.name = name

    def report(self):
        return f'{self.LOCALE_NAME_CLASS} {self.name}'

    @classmethod
    def register(klass, type):
        if type not in klass.TYPES_STORAGE:
            klass.TYPES_STORAGE.append(type)

    @classmethod
    def create(klass, type, name, **kargs):
        return eval(type)(name, **kargs)


class Fish(Animal):
    Animal.register(__qualname__)
    LOCALE_NAME_CLASS = 'Рыба'

    def __init__(self, name, immersion_depth):
        super().__init__(name)
        self.immersion_depth = immersion_depth

    def report(self):
        common_report = super().report()
        return f'{common_report}, глубина погружения: {self.immersion_depth}!'


class Bird(Animal):
    Animal.register(__qualname__)
    LOCALE_NAME_CLASS = 'Птица'

    def __init__(self, name, flight_altitude):
        super().__init__(name)
        self.flight_altitude = flight_altitude

    def report(self):
        common_report = super().report()
        return f'{common_report}, высота полета: {self.flight_altitude}!'


class Мammal(Animal):
    Animal.register(__qualname__)
    LOCALE_NAME_CLASS = 'Млекопитающее'

    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def report(self):
        common_report = super().report()
        return f'{common_report}, вес {self.weight}!'


class Insect(Animal):
    Animal.register(__qualname__)
    LOCALE_NAME_CLASS = 'Насекомый'

    def __init__(self, name, limbs_count):
        super().__init__(name)
        self.limbs_count = limbs_count

    def report(self):
        common_report = super().report()
        return f'{common_report}, количество лапок: {self.limbs_count}!'


class Arachnid(Animal):
    Animal.register(__qualname__)
    LOCALE_NAME_CLASS = 'Паукообразный'

    def __init__(self, name, eyes_count):
        super().__init__(name)
        self.eyes_count = eyes_count

    def report(self):
        common_report = super().report()
        return f'{common_report}, количество глаз: {self.eyes_count}!'


print(Animal.TYPES_STORAGE, '\n')


animals = [
    Animal.create('Fish', 'Немо', immersion_depth=32),
    Animal.create('Bird', 'Вэлиант', flight_altitude=1024),
    Animal.create('Мammal', 'Балу', weight=512),
    Animal.create('Insect', 'Флик', limbs_count=16),
    Animal.create('Arachnid', 'Лукас', eyes_count=8)
]


for animal in animals:
    print(animal.report())

# ['Fish', 'Bird', 'Мammal', 'Insect', 'Arachnid'] 

# Рыба Немо, глубина погружения: 32!
# Птица Вэлиант, высота полета: 1024!
# Млекопитающее Балу, вес 512!
# Насекомый Флик, количество лапок: 16!
# Паукообразный Лукас, количество глаз: 8!
