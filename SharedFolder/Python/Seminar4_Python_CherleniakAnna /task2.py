# Напишите функцию принимающую на вход только ключевые параметры(kwargs)
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> 
# {True: "rev", "YES": 'acc', 4: "stroka"}

def reverse_kwargs(**kwargs):
    res_dikt = {}
    for key, value in kwargs.items():
        if type(value) == list:
            value = str(value)
        res_dikt[value] = key
    return res_dikt


print(reverse_kwargs(name='Anna', cl=5, less=['математика', 'русский язык']))
