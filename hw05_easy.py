# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil

def mymkdir(dirname):
    dirpath = os.path.join(os.getcwd(), dirname)
    try:
        os.mkdir(dirpath)
    except OSError:
        print('Такая директория уже существует')
    else:
        print("Успешно создана директория ")

def mydeldir(dirname):
    dirpath = os.path.join(os.getcwd(), dirname)
    try:
        os.rmdir(dirpath)
    except OSError:
        print('Такая директория не существует')
    else:
        print("Успешно удалена директория")

#[os.mkdir(os.path.join(os.getcwd(), 'dir_' + str(_))) for _ in range(1, 11)]
# Создает каталоги dir1 по dir2
#[os.rmdir(os.path.join(os.getcwd(), 'dir_' + str(_))) for _ in range(1, 11)]
# Уаделяет каталоги dir1 по dir2

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def mylistdir():
    z = [x[0] for x in os.walk(os.getcwd())]
    print(z)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def mycpfile(src, dsc):
    src_path = os.path.join(os.getcwd(), src)
    dsc_path = os.path.join(os.getcwd(), dsc)
    try:
        shutil.copy2(src_path, dsc_path)
    except OSError:
        print('Copy')

mycpfile('hw05_easy.py', 'hw05_easy_copy.py')

#print(os.path.basename(__file__))
def mycddir(dirname):
    dir_path = os.path.join(os.getcwd(), dirname)
    try:
        os.chdir(dir_path)
    except OSError:
        print('директория')
