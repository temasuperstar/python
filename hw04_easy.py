# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
a = [1, 2, 4, 0]
b = [el**2 for el in a]
print(b)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
a2 = [1, 2, 4, 5, 6]
b2 = [1, 2, 3, 7, 6]
n2 = list(set(a2) & set(b2))
print(n2)


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

a3 = [1, 2, 5, 8, 13, -7, 19, 21, -9]
b3 = [el for el in a3 if el % 3 and el > 0 and el % 4 != 0]
print(b3)