import time


class MyString(str):
    """Доступны все возможности str
Дополнительно хранятся имя автора строки и время создания"""


    def __init__(self, value, author):
        self.author = author
        self.created_at = time.asctime(time.localtime(time.time()))


    def __new__(cls, value, author):
        return super().__new__(cls, value) 


    def __repr__ (self):
        return f'MyString("{self}", "{self.author}")'


string = MyString('asdqwezxc', 'Stas')
print(string)

print(string.author)
print(string.created_at)

print(MyString.__doc__)
print(repr(string))

# asdqwezxc
# Stas
# Sat Jul 15 19:04:56 2023
# Доступны все возможности str
# Дополнительно хранятся имя автора строки и время создания
# MyString("asdqwezxc", "Stas")
