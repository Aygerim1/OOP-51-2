import sqlite3

connect = sqlite3.connect('User.db')
cursor = connect.cursor()

cursor.execute('DROP TABLE IF EXISTS users')
connect.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(40) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT,
        grade INTEGER
    )
''')
connect.commit()

def update_grade(user_id, new_grade):
    cursor.execute(
        'UPDATE users SET grade = ? WHERE id = ?',
        (new_grade, user_id)
    )
    connect.commit()
    print(f"Grade for subject with id {user_id} updated!!")

def add_user(name, age, hobby, grade):
    cursor.execute(
        'INSERT INTO users(name, age, hobby, grade) VALUES (?,?,?,?)',
        (name, age, hobby, grade)
    )
    connect.commit()
    print(f"User {name} added with grade {grade}")

add_user("John", 25, "Reading", 4)
add_user("Alice", 22, "Swimming", 5)

update_grade(1, 3)

def get_user_by_name(name):
    cursor.execute(
        'SELECT * FROM users WHERE name = ?',
        (name,)
    )
    user = cursor.fetchall()
    if user:
        print(f"NAME: {user[0][1]} AGE: {user[0][2]} HOBBY: {user[0][3]} GRADE: {user[0][4]}")
    else:
        print("User not found")

    get_user_by_name('John')