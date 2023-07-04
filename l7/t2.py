# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать параметр желаемое конечное имя файлов.
#      При переименовании в конце имени добавляется порядковый номер.
# 2. принимать параметр количество цифр в порядковом номере.
# 3. принимать параметр расширение исходного файла.
#      Переименование должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени.
#      Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
#      К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

# --new_name=file --numbers_count=3 --original_extension=doc --new_extension=txt --fragment_name_range=3,6

import shutil
import os
import random
import sys


# Чистка
def clearing():
    shutil.rmtree('.', ignore_errors=True)


# Наполнение
def seeds():
    for extension in 21 * ['doc', 'rtf', 'odt']:
        file_name = ''.join(random.sample('abcdefghi', 9))
        full_file_name = f'{file_name}.{extension}'

        if not os.path.exists(full_file_name):
            with open(full_file_name, 'w') as f:
                f.write(full_file_name)


# Обработка
def execute(argv):
    _, *raw_params = argv

    params = dict()

    for param in raw_params:
        key, value = param.split('=')
        params[key.lstrip('-')] = value

    print(params)

    full_file_names = []

    for (path, ds, fs) in os.walk('.'):
        full_file_names.extend(fs)
        break

    i = 1

    for full_file_name in full_file_names:
        file_name, extension = os.path.splitext(full_file_name)

        if extension.replace('.', '') == params['original_extension']:
            if 'new_name' in params:
                new_name = params['new_name']
            else:
                new_name = ''

            counter = str(i).rjust(int(params['numbers_count']), '0')

            start_fragment, end_fragment = params['fragment_name_range'].split(',')
            fragment = file_name[int(start_fragment)-1:int(end_fragment)]

            new_extension = params['new_extension']

            new_full_file_name = f'{new_name}{fragment}{counter}.{new_extension}'
            os.replace(full_file_name, new_full_file_name)

            i += 1


if __name__ == '__main__':
    os.chdir('t2_cwd')

    clearing()
    seeds()
    execute(sys.argv)
