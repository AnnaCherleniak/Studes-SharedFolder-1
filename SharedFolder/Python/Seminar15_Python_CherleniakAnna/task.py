# Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву
# и наличие только букв.
import logging
import argparse

FORMAT = '{levelname:<8} - {asctime}. {msg}'
logging.basicConfig(filename='log_student.log', style='{', format=FORMAT,
                    filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def log_decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Студент - {args[1:]}, {kwargs}')
        return result
    return wrapper


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

    @log_decor
    def __init__(self, surname: str, name: str, patronymic: str) -> None:
        try:
            self.surname = surname
            self.name = name
            self.patronymic = patronymic
        except Exception as e:
            logger.error(e)

    def __str__(self) -> str:
        return f'{self.surname} {self.name} {self.patronymic}'

    def __repr__(self) -> str:
        return (f'Student(surname={self.surname}, name={self.name}, '
                f'patronymic={self.patronymic})')


def parser():
    pars = argparse.ArgumentParser(prog='Student()')
    pars.add_argument('-s')
    pars.add_argument('-n')
    pars.add_argument('-p')
    args = pars.parse_args()
    return Student(*map(str, (args.s, args.n, args.p)))


if __name__ == '__main__':
    print(parser())
