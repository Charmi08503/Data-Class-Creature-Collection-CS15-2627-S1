
from dataclasses import dataclass

@dataclass
class Creature:
    name: str
    species: str
    level: int
    health: float


creature1 = Creature("Spider-Man", "Superhuman", 12, 95.0)
creature2 = Creature("Iron Man", "Human", 15, 100.0)
creature3 = Creature("Thor", "Asgardian", 20, 150.0)


print("Creature 1:")
print(creature1.name)
print(creature1.species)
print(creature1.level)
print(creature1.health)

print("Creature 2:")
print(creature2.name)
print(creature2.species)
print(creature2.level)
print(creature2.health)

print("Creature 3:")
print(creature3.name)
print(creature3.species)
print(creature3.level)
print(creature3.health)


creature1.level = 20
creature1.health = 120.5

print("Updated Creature 1:")
print(creature1.name)
print(creature1.species)
print(creature1.level)
print(creature1.health)

print("Creature 2:")
print(creature2.name)
print(creature2.species)
print(creature2.level)
print(creature2.health)

print("Creature 3:")
print(creature3.name)
print(creature3.species)
print(creature3.level)
print(creature3.health)


print("Create Your Own Avenger!")

name = input("Enter Avenger name: ")
species = input("Enter species: ")

while True:
    try:
        level = int(input("Enter level: "))

        if level < 0:
            print("Level cannot be negative.")
        else:
            break

    except ValueError:
        print("Please enter a whole number.")

while True:
    try:
        health = float(input("Enter health: "))

        if health < 0:
            print("Health cannot be negative.")
        else:
            break

    except ValueError:
        print("Please enter a valid number.")


creature4 = Creature(name, species, level, health)

print("Your New Avenger:")
print(creature4.name)
print(creature4.species)
print(creature4.level)
print(creature4.health)
