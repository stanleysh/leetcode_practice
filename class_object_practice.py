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


john = Animal('John', 20)
print(john)
john.yearOlder()
print(john)
john = john + 3
print(john)


# -------------------------------------------------------
# Natural Number example

class NaturalNumber:
    def __init__(self, prev):
        self.prev = prev
    
    def __str__(self):
        if self.prev == 0:
            return '0'
        return f'S({self.prev})'

    def __add__(self, b): #Other option __add__(a, b):, makes it a little less confusing
        while b.prev:
            b = b.prev
            self = NaturalNumber(self)
        return self

    def __sub__(self, b):
        while b.prev:
            b = b.prev
            self = self.prev
        return self

zero = NaturalNumber(0)
one = NaturalNumber(zero)
two = NaturalNumber(one)

assert(str(zero)) == '0'
assert(str(one)) == 'S(0)'
assert(str(two)) == 'S(S(0))'

three = two + one

print(three)
print(two)
assert(str(three)) == 'S(S(S(0)))'

assert(str(three-two)) == 'S(0)'