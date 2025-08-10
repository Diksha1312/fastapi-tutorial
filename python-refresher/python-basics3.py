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
    def __init__(self, type_of_enemy: str, health_points: int = 10): # parameterized constructor
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
    def talk(self):
        print(f"{self.type_of_enemy} says: 'I will defeat you!'")
enemy = Enemy("Goblin")
enemy.talk()  # using the talk method

""" 
Encapsulation - restricting access to certain attributes or methods of an object.
In Python, we can use a single underscore (_) to indicate that an attribute is intended for internal use only,
or a double underscore (__) to make an attribute private, which prevents access from outside the class.
"""
""" Using single underscore for internal use"""
class Enemy:
    def __init__(self, type_of_enemy: str, health_points: int = 10):
        self._type_of_enemy = type_of_enemy  # internal use only
        self.health_points = health_points
    def talk(self):
        print(f"{self._type_of_enemy} says: 'I will defeat you!'")
enemy = Enemy("Goblin")
print(enemy._type_of_enemy)  # accessing internal attribute
""" Using double underscore for private attribute"""
class Enemy:
    def __init__(self, type_of_enemy: str, health_points: int = 10):
        self.__type_of_enemy = type_of_enemy  # private attribute
        self.health_points = health_points
    def talk(self):
        print(f"{self.__type_of_enemy} says: 'I will defeat you!'")
enemy = Enemy("Goblin")
# print(enemy.__type_of_enemy)  # this will raise an AttributeError because __type_of_enemy is private
print(enemy._Enemy__type_of_enemy)  # accessing private attribute using name mangling
enemy.talk()  # using the talk method   
""" Name mangling - Python's way of making private attributes inaccessible from outside the class.
This is done by prefixing the attribute name with the class name."""

"""
Inheritance - creating a new class that inherits attributes and methods from an existing class.
Method overriding - redefining a method in the child class that already exists in the parent class. 
"""

"""self vs super() - 
self refers to the instance of the class, while super() refers to the parent class.
self is used to access instance attributes and methods, while super() is used to call methods from the parent class.
"""
class Parent:
    def __init__(self, name: str):
        self.name = name        
    def greet(self):
        print(f"Hello, I am {self.name} from Parent class.")        

class Child(Parent):
    def __init__(self, name: str, age: int):
        super().__init__(name)  # calling the parent class constructor  
        self.age = age
    def greet(self):
        super().greet()  # calling the parent class greet method
        print(f"I am {self.name} from Child class, and I am {self.age} years old.")
child = Child("Alice", 10)
child.greet()  # calling the greet method from the child class, which also calls the parent class method
"""
Polymorphism - the ability to use a single interface to represent different data types.
In Python, this can be achieved through method overriding and operator overloading.
"""
class Parent:
    def speak(self):
        print("Parent speaks")
class Child(Parent): 
    def speak(self): # overriding the speak method
        print("Child speaks")
parent = Parent()
child = Child()
parent.speak()  # Output: Parent speaks
child.speak()   # Output: Child speaks

"""
Composition - a way to create complex objects by combining simpler objects.
Composition is a design principle where one class contains instances of other classes as attributes.
"""
class Car:
    def __init__(self, engine, wheels):
        self.engine = engine
        self.wheels = wheels
class Engine:
    def start(self):
        print("Engine started")
class Wheels:
    def rotate(self):
        print("Wheels rotating")
car = Car(Engine(), Wheels())
car.engine.start()  # Output: Engine started
car.wheels.rotate()  # Output: Wheels rotating