# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os

def myfun(txtdoc):
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

#    print(intrs)

s1 = myfun('workers')
s2 = myfun('hours_of')

aa = []
for key1, value1 in s1.items():
    for key2, value2 in s2.items():
        if key1 == key2:
            value1.append(value2)


for key, value in s1.items():
    z = value
    for
    print(value)
    print(list(map(lambda x: x*x, value)))

