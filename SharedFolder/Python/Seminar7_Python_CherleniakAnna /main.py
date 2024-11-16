from random import randint, choice


VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_NUMBER = 0
MAX_NUMBER = 9


def generate_file(extension: str, min_len_name=6, max_len_name=30,
                  min_bytes=256, max_bytes=4096,
                  count_files=42):

    for _ in range(count_files):
        name_f = generate_name(min_len_name, max_len_name)
        with open(name_f, 'w') as f:
            f.write(str(generate_text_bytes(min_bytes, max_bytes)))


def generate_name(min_len_name: int, max_len_name: int,
                  extension='.txt') -> str:
    name_file = ''
    for _ in range(randint(min_len_name, max_len_name)):
        name_file += choice(VOWELS + CONSONANTS)
    return name_file + extension


def generate_text_bytes(min_bytes: int, max_bytes: int) -> bytes:
    list_numbers = []
    len_res = randint(min_bytes, max_bytes)
    for _ in range(len_res):
        list_numbers.append(randint(MIN_NUMBER, MAX_NUMBER))
    return bytes(list_numbers)


def generate_files_different(dict_files: dict, min_len_name=6, max_len_name=30,
                             min_bytes=256, max_bytes=4096):
    """Словарь содержит расширение и количество файлов.
    Количество переданных расширений может быть любым.
      Количество файлов для каждого расширения различно."""
    for key, value in dict_files.items():
        extension = key
        count_files = value
        for _ in range(count_files):
            name_f = generate_name(min_len_name, max_len_name, extension)
            with open(name_f, 'w') as f:
                f.write(str(generate_text_bytes(min_bytes, max_bytes)))


if __name__ == '__main__':
    generate_file('.txt', count_files=1)
    dict_files = {'.txt': 2, '.bin': 1}
    generate_files_different(dict_files)
