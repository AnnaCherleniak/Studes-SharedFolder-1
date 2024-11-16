# 1. Напишите функцию, которая принимает на вход строку
#  - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов:
#  путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt

# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')

def elements_link(link):
    *a, b = link.split('/')
    b, c = b.split('.')
    return ('/'.join(a) + '/', b, '.' + c)


link = 'c:/Users/Vladislav/Desktop/deep_to_python/test.txt'
print(elements_link(link))
