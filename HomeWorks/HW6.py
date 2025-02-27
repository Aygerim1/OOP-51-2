class Flyable:
    def fly(self):
        return 'Летит'

class Swimmable:
    def swim(self):
        return 'Плавает'

class Duck(Flyable, Swimmable):
    def make_sound(self):
        return 'Кря-Кря!!'

donald_duck = Duck()
print(donald_duck.fly())  # Летит
print(donald_duck.swim())  # Плавает

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

donald_duck = Duck("Donald")
print(donald_duck.action())
print(Duck.mro())

import sqlite3

connect = sqlite3.connect('User.db')

cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        name VARCHAR(40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')

connect.commit()

def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES (?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь {name} добавлен")

add_user("Ardager", 26, "Гонки")
add_user("John", 33, "Плавание")

def get_user_by_name(name):
    cursor.execute('SELECT * FROM users WHERE name=?', (name,))
    user = cursor.fetchone()
    if user:
        return f"NAME: {user[0]} AGE: {user[1]} HOBBY: {user[2]}"
    else:
        return "Пользователь не найден"

print(get_user_by_name('Ardager'))