from csv import reader as CSVreader
from random import randint


class Course():
    def __init__(self, id, title):
        self.id = id
        self.title = title

        self.quizes = []


    @property
    def mark(self):
        if len(self.quizes) == 0:
            return 0

        avg_quizes_score = sum(quiz.score for quiz in self.quizes) / len(self.quizes)

        if avg_quizes_score < 40:
            return 2
        elif avg_quizes_score < 60:
            return 3
        elif avg_quizes_score < 80:
            return 4
        else:
            return 5


    def __str__(self):
        quizes = ', '.join([str(quiz) for quiz in self.quizes])

        return f'"{self.title}", mark: "{self.mark}",\n    quiz results: {quizes}'


class Range:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value


    def __set_name__(self, owner, name):
        self.param_name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')


    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value < value > self.max_value:
            raise ValueError(f'Значение {value} должно быть больше {self.min_value} или меньше {self.max_value}')


class Quiz():
    score = Range(1, 100)


    def __init__(self, score):
        self.score = score


    def __str__(self):
        return f'{self.score}'


class CoursesLoader():
    FILE_NAME = 'cources.csv'

    def call(self):
        courses = []

        with open(self.FILE_NAME, 'r') as f:
            csv = CSVreader(f)

            for row in csv:
                courses.append(Course(row[0], row[1]))
        return courses


class Student():
    def __init__(self, name):
        self.name = name
        self._courses = CoursesLoader().call()


    def __str__(self):
        courses = []
        sum_marks = 0

        for course in self._courses:
          courses.append(str(course))
          sum_marks += course.mark

        avg_mark = int(sum_marks / len(courses))
        course_titles = ";\n  ".join(courses)

        return f'Student: "{self.name}", courses:\n  {course_titles}.\nAvg mark: "{avg_mark}"'


student = Student('Elizabeth Woolridge Grant')

i = 0
while True:
    i+=1

    course_id = randint(0, 6)
    score = randint(40, 100)
    student._courses[course_id].quizes.append(Quiz(score))

    if i > 100:
       break

print(student)


# Student: "Elizabeth Woolridge Grant", courses:
#   "Discrete Mathematics for Computer Science", mark: "4",
#     quiz results: 69, 41, 65, 62, 74, 49, 69, 73, 55, 47, 94, 40, 47, 81, 85;
#   "Computational Thinking and Problem Solving", mark: "5",
#     quiz results: 77, 98, 73, 91, 81, 84, 93, 57, 92, 63, 98, 94, 56, 75, 75;
#   "Introduction to Computer Science", mark: "4",
#     quiz results: 70, 58, 61, 69, 66, 96, 53, 99, 47, 88, 98;
#   "Abstraction and Design in Computation", mark: "4",
#     quiz results: 66, 72, 64, 46, 65, 98, 96, 78, 82, 86, 45, 63, 62, 60, 62, 85, 69, 77;
#   "Systems Programming and Machine Organization", mark: "4",
#     quiz results: 80, 61, 99, 100, 72, 53, 77, 91, 73, 92, 69, 45, 45, 78;
#   "Code, Data, and Art", mark: "4",
#     quiz results: 94, 93, 69, 72, 60, 66, 60, 49, 81, 46, 88;
#   "Privacy and Technology", mark: "4",
#     quiz results: 87, 73, 91, 40, 53, 65, 70, 51, 59, 62, 76, 54, 70, 59, 54, 84, 92.
# Avg mark: "4"
