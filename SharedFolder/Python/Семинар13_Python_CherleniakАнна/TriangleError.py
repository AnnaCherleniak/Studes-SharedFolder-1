class TriangleError(Exception):
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __str__(self) -> str:
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'\
               f' - не существует'
