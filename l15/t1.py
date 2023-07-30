import locale
locale.setlocale(locale.LC_ALL, 'ru_RU')

import calendar
from datetime import datetime, date

import logging

logging.basicConfig(
    filename='t1.log',
    encoding='utf-8',
    format='{asctime} {levelname} {funcName}->{lineno}: {msg}',
    style='{',
    level=logging.NOTSET
)

logger = logging.getLogger(__name__)




class PreSetter():
    def __init__(self, possibles, default):
        self.possibles = possibles
        self.default = default

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value == '':
            result = self.default
        elif value in self.possibles:
            result = self.possibles[value]
        else:
            try:
                result = int(value)
            except ValueError:
                logger.error(f'Поймали ошибку при определении {instance}.')
                raise ValueError
        setattr(instance, self.param_name, result)




class Morpher():
    wday = PreSetter(dict(zip(calendar.day_name, range(7))),
                     datetime.now().weekday())
    month = PreSetter(dict(zip(calendar.month_name, range(12))),
                      datetime.now().month)


    def __init__(self, a='', d='', m=''):
        if a == '':
            self.number_wday = 1
        else:
            self.number_wday = int(''.join(filter(str.isdigit, a)))

        self.wday = d
        self.month = m
        self.year = datetime.now().year


    def date(self):
        """
        >>> Morpher('1-й', 'четверг', 'ноября').date()
        datetime.date(2023, 11, 2)
        >>> Morpher('3-я', 'среда', 'мая').date()
        datetime.date(2023, 5, 17)
        >>> Morpher('2-я', 'суббота', 'сентября').date()
        datetime.date(2023, 9, 9)
        >>> Morpher('1-я', 'суббота', '1').date()
        datetime.date(2023, 1, 7)
        """
        return date(self.year, self.month, self.day)


    @property
    def day(self):
        days = []
        for week in calendar.monthcalendar(self.year, self.month):
            for pos, day in enumerate(week):
                if day !=0 and pos == self.wday:
                    days.append(day)        
        return days[self.number_wday - 1]




if __name__ == '__main__':
    import doctest
    doctest.testmod()


# Trying:
#     Morpher('1-й', 'четверг', 'ноября').date()
# Expecting:
#     datetime.date(2023, 11, 2)
# ok
# Trying:
#     Morpher('3-я', 'среда', 'мая').date()
# Expecting:
#     datetime.date(2023, 5, 17)
# ok
# Trying:
#     Morpher('2-я', 'суббота', 'сентября').date()
# Expecting:
#     datetime.date(2023, 9, 9)
# ok
# Trying:
#     Morpher('1-я', 'суббота', '1').date()
# Expecting:
#     datetime.date(2023, 1, 7)
# ok
# 9 items had no tests:
#     t1
#     t1.Morpher
#     t1.Morpher.__init__
#     t1.Morpher.day
#     t1.PreSetter
#     t1.PreSetter.__get__
#     t1.PreSetter.__init__
#     t1.PreSetter.__set__
#     t1.PreSetter.__set_name__
# 1 items passed all tests:
#    4 tests in t1.Morpher.date
# 4 tests in 10 items.
# 4 passed and 0 failed.
# Test passed.
