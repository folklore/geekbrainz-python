class Matrix():
    """
    «Матрица» — американская научно-фантастическая медиафраншиза в жанре киберпанк.
    >>> Matrix([[1,3,5],[2,4,6]])
    Matrix([[1, 3, 5], [2, 4, 6]])
    """

    def __init__(self, body):
        self.body = body


    def transpose(self):
        """
        >>> m = Matrix([[1,3,5],[2,4,6]])
        >>> m.transpose()
        Matrix([[1, 2], [3, 4], [5, 6]])
        """
        result = [[None for _ in self.body] for _ in self.body[0]]

        for h, line in enumerate(self.body):
            for w, item in enumerate(line):
                result[w][h] = item

        self.body = result
        return self


    def __str__(self):
        """
        >>> m = Matrix([[1,3,5],[2,4,6]])
        >>> str(m)
        '1, 3, 5\\n2, 4, 6'
        """
        return '\n'.join([', '.join([str(n) for n in line]) for line in self.body])


    def __repr__(self):
        """
        >>> m = Matrix([[1,3,5],[2,4,6]])
        >>> repr(m)
        'Matrix([[1, 3, 5], [2, 4, 6]])'
        """
        return f'Matrix({self.body})'


    def __eq__(self, other):
        """
        >>> m = Matrix([[1,3,5],[2,4,6]])
        >>> a = Matrix([[1,3,5],[2,4,6]])
        >>> m == a
        True
        >>> b = Matrix([[1,2,3],[4,5,6]])
        >>> m == b
        False
        """
        return self.body == other.body


    def __add__(self, other):
        """
        >>> m = Matrix([[1,3,5],[2,4,6]])
        >>> n = Matrix([[1,2,3],[4,5,6]])
        >>> m + n
        Matrix([[2, 5, 8], [6, 9, 12]])
        """
        new_body = [[None for _ in self.body[0]] for _ in self.body]

        for i in range(len(self.body)):    
            for j in range(len(self.body[0])): 
               new_body[i][j] = self.body[i][j] + other.body[i][j] 

        return Matrix(new_body)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
