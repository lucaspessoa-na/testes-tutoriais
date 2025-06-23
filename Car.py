#%%
'''
Create dog class
'''
class car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __str__ (self):
        return f"The {self.color} car has {self.mileage} miles"

'''
criando objetos
'''
blue = car("blue", 20000)
red = car("red", 30000)
print(blue)
print(red)
# %%
