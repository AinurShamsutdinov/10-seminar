# Задание
# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# 📌 Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.

class Animal:
    __height: int
    __weight: int
    __name: str

    def __init__(self, height, weight, name):
        self.__height = height
        self.__weight = weight
        self.__name = name


class Bird(Animal):
    __fly_speed: int
    __migrates: bool

    def __init__(self, fly_speed, migrates, height, weight, name):
        self.__fly_speed = fly_speed
        self.__migrates = migrates
        Animal.__init__(self, height, weight, name)

    def get_specific(self):
        return self.__fly_speed, self.__migrates


class Mammal(Animal):
    __run_speed: int
    __hibernates: bool

    def __init__(self, run_speed, hibernates, height, weight, name):
        self.__run_speed = run_speed
        self.__hibernates = hibernates
        Animal.__init__(self, height, weight, name)

    def get_specific(self):
        return self.__run_speed, self.__hibernates


class Fish(Animal):
    __swim_speed: int
    __carnivorous: bool

    def __init__(self, swim_speed, carnivorous, height, weight, name):
        self.__swim_speed = swim_speed
        self.__carnivorous = carnivorous
        Animal.__init__(self, height, weight, name)

    def get_specific(self):
        return self.__swim_speed, self.__carnivorous


if __name__ == "__main__":
    bird = Bird(100, True, 20, 10, 'Sparrow')
    mammal = Mammal(40, True, 200, 500, 'Bear')
    fish = Fish(13, False, 50, 5, 'Karp')

    print(f'{bird.get_specific() = }')
    print(f'{mammal.get_specific() = }')
    print(f'{fish.get_specific() = }')

# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

class Fabric:
    __animal: Animal

    def __init__(self, animal, first_par, second_par, height, weight, name):
        if animal == 'Mammal':
            self.__animal = Mammal(first_par, second_par, height, weight, name)
        elif animal == 'Bird':
            self.__animal = Bird(first_par, second_par, height, weight, name)
        elif animal == 'Fish':
            self.__animal = Mammal(first_par, second_par, height, weight, name)

    def get_animal(self):
        return self.__animal


if __name__ == '__main__':
    bird = Fabric('Bird', 100, True, 20, 10, 'Sparrow').get_animal()
    mammal = Fabric('Mammal', 40, True, 200, 500, 'Bear').get_animal()
    fish = Fabric('Fish', 13, False, 50, 5, 'Karp').get_animal()

    print(f'{bird.get_specific() = }')
    print(f'{mammal.get_specific() = }')
    print(f'{fish.get_specific() = }')


# 📌 Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.

