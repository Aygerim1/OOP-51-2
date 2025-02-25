# Родительский класс Heroes
class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return f"{self.name} is preparing for action!"

    def attack(self):
        return f"{self.name} attacks with power!"

class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def action(self):
        return f"{self.name} is aiming an arrow!"

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            return f"{self.name} shoots an arrow with {self.precision}% precision!"
        else:
            return f"{self.name} has no arrows left!"

hero = Heroes("Warrior", 100)
archer = Archer("Robin", 80, 10, 95)

print(hero.action())
print(hero.attack())

print(archer.action())
print(archer.attack())