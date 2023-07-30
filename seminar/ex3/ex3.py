# Задание No3
# 📌 Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п.
#       на ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.


class Person(object):
    __lastname: str
    __name: str
    __patronymic: str
    __age: int
    __height: int

    def __init__(self, lastname, name, patronymic, age, height):
        self.lastname = lastname
        self.name = name
        self.patronymic = patronymic
        self.age = age
        self.height = height

    def birthday(self):
        self.age += 1

    def full_name(self):
        return str(f'{self.lastname} {self.name} {self.patronymic}')

    def get_age(self):
        return self.age


if __name__ == "__main__":
    person = Person('Testoff', 'Test', 'Testovich', 25, 158)
    print(f'{person.full_name() = }')
    print(f'{person.birthday() = }')
    print(f'{person.get_age() = }')
    person.age = 388
    print(f'{person.age = }')
