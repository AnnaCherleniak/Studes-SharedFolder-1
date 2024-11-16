import os
import json


def directory_in_json(file_name: str, path_dir: str):
    with open(file_name, 'w', encoding='utf-8') as f:
        dir = read_directory(path_dir)
        json.dump(dir, f, indent=4)


def read_directory(path_dir: str) -> list:
    list_dir = []
    for dir, dir_name, file_name in os.walk(path_dir):
        for dir in dir_name:
            list_dir.append({
                'name': dir,
                'type': 'directory'
            })
        for f in file_name:
            name, type_file = f.split('.')
            list_dir.append({
                'name': name,
                'extension': f'.{type_file}',
                'type': 'file'
            })
    return list_dir


if __name__ == '__main__':
    path_dir = 'C:\\python tasks\\DZ\\Seminar8_Python_CherleniakAnna\\test'
    directory_in_json('result.json', path_dir)
