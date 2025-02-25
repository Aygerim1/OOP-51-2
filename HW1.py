class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой lvl {self.lvl}, мое HP {self.HP}")

    def is_adult(self):
        if self.lvl >= 10:
            return True
        return False
hero1 = Hero("arsen", 5, 100)
hero2 = Hero("nurai", 15, 120)
hero3 = Hero("begai", 10, 110)

hero1.introduce()
hero2.introduce()
hero3.introduce()

print(f"hero1: {hero1.is_adult()}")
print(f"hero2: {hero2.is_adult()}")
print(f"hero3: {hero3.is_adult()}")