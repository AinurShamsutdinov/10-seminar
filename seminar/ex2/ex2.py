# Задание No2
# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.


class Rectangle:
    length: int
    depth: int

    def __init__(self, length, depth):
        if (length is None) or (depth is None):
            if length is not None:
                self.length = length
                self.depth = length
            elif depth is not None:
                self.length = depth
                self.depth = depth
        elif (length is not None) and (depth is not None):
            self.length = length
            self.depth = depth

    def perimeter(self):
        return (self.length + self.depth) * 2

    def area(self):
        return self.length * self.depth
