# Задание No6
# 📌 Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс
# Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    __height: int
    __weight: int
    __name: str

    def __int__(self, height, weight, name):
        self.__height = height
        self.__weight = weight
        self.__name = name


class Bird(Animal):
    __fly_speed: int
    __migrates: bool

    def __init__(self, fly_speed, migrates, height, weight, name):
        self.__fly_speed = fly_speed
        self.__migrates = migrates
        Animal(self, height, weight, name)

    def get_specific(self):
        return self.__fly_speed, self.__migrates


class Mammal(Animal):
    __run_speed: int
    __hibernates: bool

    def __init__(self, run_speed, hybernates, height, weight, name):
        self.__run_speed = run_speed
        self.__hibernates = hybernates
        Animal(self, height, weight, name)

    def get_specific(self):
        return self.__run_speed, self.__hibernates


class Fish(Animal):
    __swim_speed: int
    __carnivorous: bool

    def __init__(self, swim_speed, carnivorous, height, weight, name):
        self.__swim_speed = swim_speed
        self.__carnivorous = carnivorous
        Animal(self, height, weight, name)

    def get_swim_speed(self):
        return self.__swim_speed, self.__carnivorous
