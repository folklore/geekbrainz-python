from libra import Matrix
import pytest


@pytest.fixture
def matrix():
    return Matrix([[1,3,5],[2,4,6]])


def test_transpose(matrix):
    expected_matrix = Matrix([[1,2],[3,4],[5,6]])
    assert matrix.transpose() == expected_matrix


def test_str(matrix):
    expected_output = '1, 3, 5\n2, 4, 6'
    assert str(matrix) == expected_output


def test_repr(matrix):
    expected_output = 'Matrix([[1, 3, 5], [2, 4, 6]])'
    assert repr(matrix) == expected_output


def test_when_eq(matrix):
    compared_matrix = Matrix([[1,3,5],[2,4,6]])
    assert matrix == compared_matrix


def test_when_not_eq(matrix):
    compared_matrix = Matrix([[1,2,3],[4,5,6]])
    assert matrix != compared_matrix


def test_add(matrix):
    matrix_2 = Matrix([[1,2,3],[4,5,6]])
    expected_matrix = Matrix([[2,5,8], [6,9,12]])
    assert matrix + matrix_2 == expected_matrix
