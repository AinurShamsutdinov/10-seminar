# Задание No1
# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.
import math


class Circle:
    __radius: int

    def __init__(self, radius):
        self.radius = radius

    def lenght(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius / 2
