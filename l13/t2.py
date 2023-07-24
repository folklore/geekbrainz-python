class NegativeLengthError(ValueError):
    pass

a = int(input('Введите длину первой стороны: '))
b = int(input('Введите длину второй стороны: '))
c = int(input('Введите длину третьей стороны: '))

if(a<0 or b<0 or c<0):
    raise NegativeLengthError(f'Одна из сторон треугольника меньше нуля: {a=}, {b=}, {c=}')

if(a + b > c):
    if(b + c > a):
        if(c + a > b):
            print('Треугольник существует ...')

            if((a*a + b*b == c*c) or (b*b + c*c == a*a) or (c*c + a*a == b*b)):
                print('... и он прямоугольный')

            if(a == b and b == c and c == a):
                print('... и он равносторонний')
            elif(a == b or b == c or c == a):
                print('... и он равнобедренный')

            quit()

print('Треугольник с такими сторонами не существует.')
