import os
import subprocess

# Путь к папке с .ts файлами
directory = 'aaa/'

# Имя файла для списка сегментов
file_list_path = 'file_list.txt'

def create_file_list(directory, file_list_path):
    # Получаем список всех .ts файлов в папке
    ts_files = sorted([f for f in os.listdir(directory) if f.endswith('.ts')], key=lambda x: int(x.split('.')[0]))

    # Записываем список файлов в файл
    with open(file_list_path, 'w') as f:
        for ts_file in ts_files:
            f.write(f"file '{os.path.join(directory, ts_file)}'\n")

def concatenate_ts_files(file_list_path, output_file):
    # Команда для объединения файлов
    command = [
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', file_list_path,
        '-c', 'copy',
        output_file
    ]

    # Запускаем команду
    subprocess.run(command, check=True)

# Создание списка файлов
create_file_list(directory, file_list_path)

# Объединение файлов
output_file = 'output.mp4'
concatenate_ts_files(file_list_path, output_file)