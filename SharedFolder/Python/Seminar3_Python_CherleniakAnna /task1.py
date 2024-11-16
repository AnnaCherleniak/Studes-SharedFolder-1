#  Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

NAME_COMPARE = 'Alex'

camp_dict = {'Alex': ('рюкзак', 'палатка', 'спальник', 'аптечка'),
             'Ivan': ('рюкзак', 'еда', 'спички', 'вода'),
             'Maksim': ('спальник', 'рюкзак', 'вода', 'фонарик')}

list_name = list(camp_dict.keys())
index_name_compare = list_name.index(NAME_COMPARE)
temp = set(camp_dict[list_name.pop(index_name_compare)])
temp_compare = set(camp_dict[list_name[0]])
for ind, name in enumerate(list_name):
    temp.intersection_update(camp_dict[name])
    temp_compare.intersection_update(camp_dict[name])
print(f'Какие вещи взяли все три друга: {temp}')

temp_compare -= set(camp_dict[NAME_COMPARE])
print(f'Какие вещи есть у всех друзей кроме Alex: {temp_compare}')

temp = set(camp_dict[NAME_COMPARE])
for name in camp_dict:
    if name != NAME_COMPARE:
        temp = temp.difference(camp_dict[name])
print(f'Какие вещи уникальны, есть только у Alex: {temp}')
