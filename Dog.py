# %%
'''
creating the dog class
'''
class Dog:
    #atribute of every object in this class
    species = "Canis Familiaries"
    def __init__(self, name, age):
        #each object in the class should have these specified
        self.name = name
        self.age = age
    #method
    def description (self):
        return f"{self.name} is {self.age} years old"
    #method
    def speak (self,sound):
        return f"{self.name} says {sound}"
    def __str__ (self):
        return f"{self.name} is {self.age} years old"
''''
creating an object of the class
'''
carlos = Dog("Carlos", 3)
palito = Dog("Palito", 4)

carlos.speak("crise na california")
palito.speak("hatanabá")

print (carlos)
