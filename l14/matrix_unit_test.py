from libra import Matrix
import unittest


class TestMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = Matrix([[1,3,5],[2,4,6]])


    def test_transpose(self):
        expected_matrix = Matrix([[1,2],[3,4],[5,6]])
        self.assertEqual(self.matrix.transpose(), expected_matrix)


    def test_str(self):
        expected_output = '1, 3, 5\n2, 4, 6'
        self.assertEqual(str(self.matrix), expected_output)


    def test_repr(self):
        expected_output = 'Matrix([[1, 3, 5], [2, 4, 6]])'
        self.assertEqual(repr(self.matrix), expected_output)


    def test_when_eq(self):
        compared_matrix = Matrix([[1,3,5],[2,4,6]])
        self.assertTrue(self.matrix == compared_matrix)


    def test_when_not_eq(self):
        compared_matrix = Matrix([[1,2,3],[4,5,6]])
        self.assertFalse(self.matrix == compared_matrix)


    def test_add(self):
        matrix_2 = Matrix([[1,2,3],[4,5,6]])
        expected_matrix = Matrix([[2,5,8], [6,9,12]])
        self.assertEqual(self.matrix + matrix_2, expected_matrix)


if __name__ == '__main__':
    unittest.main()
