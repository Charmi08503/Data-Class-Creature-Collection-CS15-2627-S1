
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
