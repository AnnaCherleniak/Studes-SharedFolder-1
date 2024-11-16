# Напишите функцию для транспонирования матрицы
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def transposition_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix.append([matrix[0][i]])
    for row in range(1, len(matrix)):
        for col in range(len(matrix[0])):
            new_matrix[col].append(matrix[row][col])
    return new_matrix


def transposition_matrix_zip(matrix):
    new_matrix = []
    for row in zip(*my_matrix):
        new_matrix.append(list(row))
    return new_matrix


my_matrix = [[1, 4, 7], [2, 5, 8]]
print(my_matrix)
print(transposition_matrix(my_matrix))
# Второй вариант:
print(transposition_matrix_zip(my_matrix))
