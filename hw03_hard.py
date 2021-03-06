# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3



# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os

def myfu(a, b, c):
    '''
    Подсчет ЗП
    :param a: норма чаов
    :param b: стоимость часа
    :param c: отработанно
    :return: возвращаем значение ЗП
    '''
    if a == c:
        return a * b
    elif c > a:
        return (a * b) + ((c - a) * (b + b))
    elif a > c:
        return (a * b) - ((a - c) * (b + b))



def myfun(txtdoc):
    '''
    Возвращает словарь в зависимости от файла длины строк файла
    :param txtdoc: имя файла
    :return: возвращает словарь фимилия = цыфры
    '''
    path = os.path.join('data', txtdoc)
    with open(path, 'r', encoding='UTF-8') as f:
        b = []
        for line in f:
            a = line.split()
            b.append(a)

    if len(b[1]) == 3:

        s2 = {}
        for f in range(1, len(b)):
            u = b[f][1]
            y = int(b[f][2])
            s2[u] = y
        return (s2)

    else:
        s1 = {}
        for f in range(1, len(b)):
            a = int(b[f][2])
            v = int(b[f][4])
            x = b[f][1]
            h = (lambda x, y: x // y)(a, v)
            s1[x] = [v, h]
        return (s1)


s1 = myfun('workers')
s2 = myfun('hours_of')

# Слияние словарей

for key1, value1 in s1.items():
    for key2, value2 in s2.items():
        if key1 == key2:
            value1.append(value2)

# Подсчет ЗП через фунцию
for key, value in s1.items():
    print(key, myfu(value[0], value[1], value[2]))


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
