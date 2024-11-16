# 2. Напишите код, который запрашивает число и сообщает является
# ли оно простым или составным.
# Используйте правило для проверки: “Число является простым,
# если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

number = 55
START = 2
STOP = number
MIN_BORDER = 0
MAX_BORDER = 100000
count = 0

if number < MIN_BORDER or number > MAX_BORDER:
    print('Введите число от 0 до 100 000')
elif number == 1 or number == 0:
    print('Числа 0 и 1 не являются ни простым, ни сложным')
else:
    for num in range(START, STOP):
        if number % num == 0:
            print('Число составное')
            count += 1
            break
    if count == 0:
        print('Число простое')
