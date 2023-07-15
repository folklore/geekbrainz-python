class Rectangle():
    """Прямоугольник — четырёхугольник, у которого все углы прямые (равны 90°)."""


    def __init__(self, a, b):
        self.a = a
        self.b = b


    @property
    def area(self):
        return self.a * self.b


    @property
    def perimeter(self):
        return 2 * (self.a + self.b)


    def __str__(self):
        return f'Rectangle a={self.a}, b={self.b}'


    def __repr__(self):
        return f'Rectangle({self.a}, {self.b})'


    def __add__(self, other):
        return Rectangle(self.a + other.a, self.b + other.b)
    def __sub__(self, other):
        if self.a < other.a:
            raise ValueError(f'original A side less than other A side')
        elif self.b < other.b:
            raise ValueError(f'original B side less than other B side')
        else:
            return Rectangle(self.a - other.a, self.b - other.b)


    def __eq__(self, other):
        return self.area == other.area
    def __gt__(self, other):
        return self.area > other.area
    def __ge__(self, other):
        return self.area >= other.area
    def __lt__(self, other):
        return self.area < other.area
    def __le__(self, other):
        return self.area <= other.area


rectangle = Rectangle(10, 20)
print(rectangle)

print(rectangle.area)
print(rectangle.perimeter)

print(Rectangle.__doc__)
print(repr(rectangle))

other_rectangle = Rectangle(3, 7)
print(other_rectangle)

print(f'== {rectangle == other_rectangle}')
print(f' > {rectangle > other_rectangle}')
print(f'>= {rectangle >= other_rectangle}')
print(f' < {rectangle < other_rectangle}')
print(f'<= {rectangle <= other_rectangle}')

nova_rectangle = rectangle + other_rectangle
print(nova_rectangle)

nova_rectangle = rectangle - other_rectangle
print(nova_rectangle)


# Rectangle a=10, b=20
# 200
# 60
# Прямоугольник — четырёхугольник, у которого все углы прямые (равны 90°).
# Rectangle(10, 20)
# Rectangle a=3, b=7
# == False
#  > True
# >= True
#  < False
# <= False
# Rectangle a=13, b=27
# Rectangle a=7, b=13
