# Задание No5
# 📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.класса

class Bird:
    __fly_speed: int
    __migrates: bool
    __height: int
    __weight: int
    __name: str

    def __init__(self, fly_speed, migrates, height, weight, name):
        self.__fly_speed = fly_speed
        self.__migrates = migrates
        self.__height = height
        self.__weight = weight
        self.__name = name

    def get_specific(self):
        return self.__fly_speed, self.__migrates


class Mammal:
    __run_speed: int
    __hibernates: bool
    __height: int
    __weight: int
    __name: str

    def __init__(self, run_speed, hybernates, height, weight, name):
        self.__run_speed = run_speed
        self.__hibernates = hybernates
        self.__height = height
        self.__weight = weight
        self.__name = name

    def get_specific(self):
        return self.__run_speed, self.__hibernates


class Fish:
    __swim_speed: int
    __carnivorous: bool
    __height: int
    __weight: int
    __name: str

    def __init__(self, swim_speed, carnivorous, height, weight, name):
        self.__swim_speed = swim_speed
        self.__carnivorous = carnivorous
        self.__height = height
        self.__weight = weight
        self.__name = name

    def get_specific(self):
        return self.__swim_speed, self.__carnivorous


if __name__ == "__main__":
    bird = Bird(100, True, 20, 10, 'Sparrow')
    mammal = Mammal(40, True, 200, 500, 'Bear')
    fish = Fish(13, False, 50, 5, 'Karp')

    print(f'{bird.get_specific() = }')
    print(f'{mammal.get_specific() = }')
    print(f'{fish.get_specific() = }')
