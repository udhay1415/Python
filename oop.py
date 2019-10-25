# Example 1
class Dog():
    
    # Class object attribute
    species = "mammal"
    
    def __init__(self, breed):
        self.breed = breed

# Instantation        
myDog = Dog('pug');
print(myDog.species);

# Example 2
class Circle():
    pi = 2.14
    def __init__(self, radius):
        self.radius = radius
    
    # Object method
    def calculateArea(self):
        return self.radius*self.radius*self.pi
        
myCircle = Circle(2);
print(myCircle.radius);
print(myCircle.calculateArea());

# Example - Inheritance
class Animal(): # Base class
    def __init__(self):
        print('Animal created')
    def eating(self):
        print('Animal eating')

class Lion(Animal): # Derived class that can access the methods and properties of base class
    def __init__(self):
        print('Lion created')
        
myLion = Lion()
myLion.eating()

    