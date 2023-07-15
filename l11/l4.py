class Matrix():
    """«Матрица» — американская научно-фантастическая медиафраншиза в жанре киберпанк."""


    def __init__(self, body):
        self.body = body


    def transpose(self):
        result = [[None for _ in self.body] for _ in self.body[0]]

        for h, line in enumerate(self.body):
            for w, item in enumerate(line):
                result[w][h] = item

        return result


    def __str__(self):
        return '\n'.join([', '.join([str(n) for n in line]) for line in self.body])


    def __repr__(self):
        return f'Matrix({self.body})'


    def __eq__(self, other):
        return self.body == other.body


    def __add__(self, other):
        new_body = [[None for _ in self.body[0]] for _ in self.body]

        for i in range(len(self.body)):    
            for j in range(len(self.body[0])): 
               new_body[i][j] = self.body[i][j] + other.body[i][j] 

        return Matrix(new_body)



print(Matrix.__doc__)


original_matrix = Matrix([
    [1, 3, 5],
    [2, 4, 6],
])
print(original_matrix)
print(repr(original_matrix))


other_matrix = Matrix([
    [1, 2, 3],
    [4, 5, 6]
])
print(other_matrix)
print(repr(other_matrix))


print(f'== {original_matrix == other_matrix}')


new_matrix = original_matrix + other_matrix
print(new_matrix)
print(repr(new_matrix))


# «Матрица» — американская научно-фантастическая медиафраншиза в жанре киберпанк.
# 1, 3, 5
# 2, 4, 6
# Matrix([[1, 3, 5], [2, 4, 6]])
# 1, 2, 3
# 4, 5, 6
# Matrix([[1, 2, 3], [4, 5, 6]])
# == False
# 2, 5, 8
# 6, 9, 12
# Matrix([[2, 5, 8], [6, 9, 12]])
