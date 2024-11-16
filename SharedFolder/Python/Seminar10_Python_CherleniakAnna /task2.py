# 3. Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.


class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'

    def sum_(self, obj) -> object:
        numerator1 = self.numerator
        denominator1 = self.denominator
        numerator2 = obj.numerator
        denominator2 = obj.denominator
        numerator_new = 0
        denominator_new = 0
        if denominator1 == denominator2:
            numerator_new = numerator1 + numerator2
            denominator_new = denominator1
        else:
            numerator1 = numerator1 * denominator2
            numerator2 = numerator2 * denominator1
            numerator_new = numerator1 + numerator2
            denominator_new = denominator1 * denominator2
            for d in range(int(numerator_new/2) + 1, 1, -1):
                if numerator_new % d == 0 and denominator_new % d == 0:
                    numerator_new /= d
                    denominator_new /= d
        result = Fraction(int(numerator_new), int(denominator_new))
        return result

    def multi_(self, obj) -> object:
        numerator_new = self.numerator * obj.numerator
        denominator_new = self.denominator * obj.denominator
        for d in range(int(numerator_new/2) + 1, 1, -1):
            if numerator_new % d == 0 and denominator_new % d == 0:
                numerator_new /= d
                denominator_new /= d
        result = Fraction(int(numerator_new), int(denominator_new))
        return result


if __name__ == '__main__':
    f1 = Fraction(1, 5)
    f2 = Fraction(2, 8)

    print(f1.sum_(f2))
    print(f1.multi_(f2))
