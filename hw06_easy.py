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



class Trap:
    def __init__(self, a, b, c, d):
        try:
            self.AB = round(math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2), 2)
            self.BC = round(math.sqrt((c[0]-b[0])**2 + (c[1]-b[1])**2), 2)
            self.CD = round(math.sqrt((d[0]-c[0])**2 + (d[1]-c[1])**2), 2)
            self.DA = round(math.sqrt((a[0]-d[0])**2 + (a[1]-d[1])**2), 2)
        except TypeError:
            print('Параметры заданы неправильно')

    def celes(self):
        return self.AB == self.CD

    def perimeter(self):
        return round(self.AB + self.BC + self.CD + self.DA, 2)

    def area(self):
        if self.celes():
            h = math.sqrt(self.AB**2 - ((self.DA - self.BC)**2) / 4)
            return round(1/2 * (self.BC + self.DA) * h, 2)
        else:
            p = self.perimeter() / 2
            return round((self.BC + self.DA)/abs(self.DA - self.BC) *
                         math.sqrt((p-self.DA)*(p-self.BC) *
                                   (p-self.DA-self.AB) *
                                   (p-self.DA-self.CD)), 2)


trap = Trap((-4, 2), (-2, 4), (3, 4), (5, 3))

print('Трапеция является равнобокой: {0}\n'
      'с Площадью {1} кв.см и Периметром {2} '
      'см'.format(trap.celes(), trap.area(), trap.perimeter()))
