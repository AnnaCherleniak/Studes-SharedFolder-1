# Дополнительно:
# решить задачу про таблицу умножения:
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

TITLE = 'ТАБЛИЦА УМНОЖЕНИЯ'
START = 2
STOP = 10
LAST_NUMBER_1 = int(STOP/2)
LAST_NUMBER_2 = STOP - 1
number_1 = START
number_2 = START

print(f'\t\t{TITLE}\n')
while number_2 <= STOP:
    for number_1 in range(START, LAST_NUMBER_1 + 1):
        if number_1 == LAST_NUMBER_1:
            print(f'{number_1} x {number_2} = {number_1 * number_2}\t')

        else:
            print(f'{number_1} x {number_2} = {number_1 * number_2}\t', end='')

    number_2 += 1

print()

number_2 = START
while number_2 <= STOP:
    for number_1 in range(LAST_NUMBER_1 + 1, STOP):
        if number_1 == LAST_NUMBER_2:
            print(f'{number_1} x {number_2} = {number_1 * number_2}\t')

        else:
            print(f'{number_1} x {number_2} = {number_1 * number_2}\t', end='')

    number_2 += 1
