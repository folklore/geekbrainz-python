original_matrix = [
    [1, 3, 5],
    [2, 4, 6],
]

expected_matrix = [
    [1, 2],
    [3, 4],
    [5, 6],
]

print(original_matrix)


def matrix_transpose(matrix):
    result = [[None for _ in matrix] for _ in matrix[0]]

    for h, line in enumerate(matrix):
        for w, item in enumerate(line):
            result[w][h] = item

    return result


transposed_matrix = matrix_transpose(original_matrix)
print(transposed_matrix)

print(transposed_matrix == expected_matrix)


# [[1, 3, 5], [2, 4, 6]]
# [[1, 2], [3, 4], [5, 6]]
# True
