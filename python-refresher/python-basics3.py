"""
Object oriented programming (OOP) in Python - class, object, attributes, methods
Abstraction, Inheritance, Polymorphism, Encapsulation - 4 pillars of OOP

""" 
class Enemy:
    type_of_enemy: str
    health_points: int = 10

enemy = Enemy()
enemy.type_of_enemy = "Goblin"
print(f"Enemy type: {enemy.type_of_enemy}, Health points: {enemy.health_points}")
"""
Abstraction - hiding complex implementation details and showing only the essential features of the object.
"""
class Enemy:
    type_of_enemy: str
    health_points: int = 10
    def talk(self):
        print(f"{self.type_of_enemy} says: 'I will defeat you!'")
enemy = Enemy()
enemy.type_of_enemy = "Goblin"
enemy.talk() # abstracting the talk method
"""
Constructors in Python - __init__ method, used to initialize object attributes when an object is created.
3 different types of constructors:
1. Default/Empty constructor - no parameters.
2. No argument constructor - takes parameters but no default values.
3. Parameterized constructor - takes parameters with default values.
"""
class Enemy:
    type_of_enemy: str
    health_points: int = 10

    def __init__(self, type_of_enemy: str): # parameterized constructor
        self.type_of_enemy = type_of_enemy

    def talk(self):
        print(f"{self.type_of_enemy} says: 'I will defeat you!'")
enemy = Enemy("Goblin")
enemy.talk()  # using the talk method

""" """