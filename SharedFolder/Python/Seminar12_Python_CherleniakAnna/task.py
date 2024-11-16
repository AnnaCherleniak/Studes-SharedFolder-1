class Text:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.istitle():
            raise ValueError('Введены неверные данные')
        letters = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к',
                   'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
                   'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я')
        for i in value:
            if i.lower() not in letters:
                raise ValueError('Введены неверные данные')


class Student:
    __slots__ = ('_surname', '_name', '_patronymic')

    surname = Text()
    name = Text()
    patronymic = Text()

    def __init__(self, surname: str, name: str, patronymic: str) -> None:
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def __str__(self) -> str:
        return f'{self.surname} {self.name} {self.patronymic}'

    def __repr__(self) -> str:
        return (f'Student(surname={self.surname}, name={self.name}, '
                f'patronymic={self.patronymic})')


if __name__ == '__main__':
    st1 = Student('Черленяк', 'Анна', 'Леонидовна')
    print(st1)
    print(repr(st1))
