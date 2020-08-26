class Animal:
    def __init__(self, name, age = 0): # Set defaults here, if none set it is required
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, age: {self.age}'

    def __add__(self, a):
        self.age = self.age + a
        return self 

    def yearOlder(self):
        self.age += 1

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def __str__(self):
        return f'Name: {self.name}, age: {self.age}, breed: {self.breed}'

    def yearOlder(self):
        self.age += 7


john = Animal('John', 20)
print(john)
john.yearOlder()
print(john)
john = john + 3
print(john)
spot = Dog('Spot', 5, 'Golden Retreiver')
print(spot)
spot.yearOlder()
print(spot)
john.yearOlder()
print(john)

