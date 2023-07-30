# Задание No5
# 📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.класса


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

    def get_fly_speed(self):
        return self.__fly_speed

    def get_migrates(self):
        return self.__migrates


class Mammal(Animal):
    __run_speed: int
    __hibernates: bool

    def __init__(self, run_speed, hybernates, height, weight, name):
        self.__run_speed = run_speed
        self.__hibernates = hybernates
        Animal(self, height, weight, name)

    def get_run_speed(self):
        return self.__run_speed

    def get_hibernates(self):
        return self.__hibernates


class Fish(Animal):
    __swim_speed: int
    __carnivorous: bool

    def __init__(self, swim_speed, carnivorous, height, weight, name):
        self.__swim_speed = swim_speed
        self.__carnivorous = carnivorous
        Animal(self, height, weight, name)

    def get_swim_speed(self):
        return self.__swim_speed

    def get_carnivorous(self):
        return self.__carnivorous
