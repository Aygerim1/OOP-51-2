lessons = [
    {"id": 1, "subject": "Math", "grade": 5},
    {"id": 2, "subject": "History", "grade": 4},
    {"id": 3, "subject": "Science", "grade": 3}}
def update_grade(id, new_grade):
    # Поиск урока с заданным id
    for lesson in lessons:
        if lesson["id"] == id:
            lesson["grade"] = new_grade
            print(f"Subject id {id} updated !!")
            return
        print(f"Subject id {id} not found !!")