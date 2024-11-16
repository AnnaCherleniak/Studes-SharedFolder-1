import datetime


def is_valid_date() -> bool:
    date = input('Введите дату в формате DD.MM.YYYY: \n')
    day, month, year = date.split('.')
    try:
        datetime.datetime.fromisoformat(f"{year}-{month}-{day}")
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    print(is_valid_date())
