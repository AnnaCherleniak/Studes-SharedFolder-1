# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# Пример: [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

elements = ['11', 'hello', '5', '5', '1', 'hello world', '11', '88', '5']
result = []

for element in elements:
    if elements.count(element) > 1:
        if element not in result:
            result.append(element)
print(result)
