# to understand the __repr__ method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self): #allows for objects of this class to be output as a string, both repr() and str().
         rep = 'Person(' + self.name + ',' + repr(self.age) + ')'
         return rep


John = Person("John", 20)
Sally = Person ("Sally", 28)
print(type(repr(Sally))," : ", repr(Sally))
print(type(str(Sally))," : ", str(Sally))