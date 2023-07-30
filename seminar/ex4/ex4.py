# Задание No4
# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь


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


class Employee(Person):
    __employee_id: int
    __access_level: int

    def __init__(self, employee_id, lastname, name, patronymic, age, height):
        self.__employee_id = employee_id
        self.__access_level = employee_id % 7
        Person.__init__(self, lastname, name, patronymic, age, height)

    def get_access_level(self):
        return self.__access_level


if __name__ == "__main__":
    employee = Employee(700009, 'Testov', 'Test', 'Testovich', 23, 180)
    print(employee.full_name())
    print(employee.get_access_level())
