# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Figure:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def plosh(self):
        p = 0.5 * (self.a + self.b + self.c)
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def visot(self):
        p = 0.5 * (self.a + self.b + self.c)
        return (2 * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))) / self.a

    def pirim(self):
        return self.a + self.b + self.c

t = Figure(3, 4, 5)

print(t.plosh())
print(t.visot())
print(t.pirim())



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

