# Множественное наследование

# горизонтальное наследование
# class Flyable:

#     def fly(self):
#         return 'Летит'


# class Swimmable:

#     def swim(self):
#         return 'Плавает'


# class Duck(Flyable, Swimmable):

#     def make_sound(self):
#         return 'Кря-Кря!!'

# donald_duck = Duck()
# print(donald_duck.fly())
# print(donald_duck.swim())

# ромбовидное наследование

class Animal:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Издает звук"

    def action(self):
        return 'Базовое действие'


class Swimmable(Animal):

    def action(self):
        return 'Плавает'


class Flyable(Animal):

    def action(self):
        return 'Летит'


class Duck(Swimmable, Flyable):

    def make_sound(self):
        return 'Кря-Кря!!'

    # def action(self):
    #     return 'Летает и плавает'


donald_duck = Duck()
print(donald_duck.action())
print(Duck.mro())

import sqlite3

# A4
connect = sqlite3.connect('User.db')

# Рука с Ручкой
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
               ''')

# Сохранение изменений
connect.commit()


# CRUD - Create - Reate - Update - Delete


# Create
def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")


add_user("John", 33, "плавание")

