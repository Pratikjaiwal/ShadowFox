class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Super Power: {self.super_power}, Weapon: {self.weapon}"
    def is_leader(self)
        return self.name == "Captain America"
    super_heroes = [
    Avenger("Captain America", 34, "Male", "Super Strength", "Shield"),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 40, "Male", "Fighting Skills", "Bow and Arrows"),
]for hero in super_heroes:
    print(hero.get_info())
    print(f"Is Leader: {'Yes' if hero.is_leader() else 'No'}")
    print() 
