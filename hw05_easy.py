# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

def mymkdir():
    try:
        [os.mkdir(os.path.join(os.getcwd(), 'dir_' + str(_))) for _ in range(1, 11)]
    except FileExistsError:
        print('Такая директория уже существует')
    else:
        print("Успешно созданы директории dir_1 - dir_9")

def mydeldir():
    try:
        [os.rmdir(os.path.join(os.getcwd(), 'dir_' + str(_))) for _ in range(1, 11)]
    except FileExistsError:
        print('Такая директория не существует')
    else:
        print("Успешно удалены директории dir_1 - dir_9")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
