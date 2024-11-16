# 1.Треугольник существует только тогда,
#  когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним,
#  равнобедренным или равносторонним.

class Triangle:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self) -> bool:
        if ((self.a + self.b) < self.c or
                (self.a + self.c) < self.b or
                (self.b + self.c) < self.a):
            return False
        return True

    def type_(self) -> str:
        if not self.is_triangle():
            return None
        if self.a == self.b == self.c:
            return 'Треугольник равносторонний'
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return 'Треугольник равнобедренный'
        return 'Треугольник разносторонний'


if __name__ == '__main__':
    t1 = Triangle(10, 7, 7)
    print(t1.is_triangle())
    print(t1.type_())
