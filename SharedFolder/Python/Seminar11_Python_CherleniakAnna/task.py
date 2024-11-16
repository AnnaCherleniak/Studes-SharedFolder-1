import numpy as np


class Matrix:

    def __init__(self, *rows: list) -> None:
        self.row = rows

    def __str__(self) -> str:
        result = ''
        for row in self.row:
            result += f'{str(row)}\n'
        return result

    def __repr__(self) -> str:
        return f'Matrix({self.row})'

    def __add__(self, other) -> object | None:
        first = np.array(list(self.row))
        second = np.array(list(other.row))
        try:
            result = first + second
            rows = [list(row) for row in result]
        except ValueError:
            return None
        return Matrix(*rows)

    def __mul__(self, other) -> object | None:
        first = np.array(list(self.row))
        second = np.array(list(other.row))
        try:
            result = first.dot(second)
            rows = [list(row) for row in result]
        except ValueError:
            return None
        return Matrix(*rows)

    def __eq__(self, other: object) -> bool:
        return self is other


if __name__ == "__main__":
    m1 = Matrix([1, 2], [2, 3])
    m2 = Matrix([4, 5], [5, 6])
    m3 = m1
    m4 = Matrix([1, 3], [4, 6], [7, 9])
    print(m1)
    print(repr(m1))
    print(m1 + m2)
    print(m1 * m2)
    print(m1 == m2)
    print(m1 == m3)
    print(m4)
    print(m1 == m4)
    print(m1 * m4)
