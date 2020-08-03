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


# -------------------------------------------------------
# Natural Number example

class NaturalNumber:
    def __init__(self, prev = None):
        self.prev = prev
    
    def __str__(self):
        if self.prev == None:
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

    def __ge__(a, b):
        while a.prev != None and b.prev != None:
            b = b.prev
            a = a.prev
        return b.prev == None

    def __mod__(a, b):
        while a >= b:
            a = a-b
        return a

def isPrime(n):
    i = two
    while n - one >= i:
        if n % i == zero:
            return False
        else:
            i = i + one
    return True

zero = NaturalNumber()
one = NaturalNumber(zero)
two = NaturalNumber(one)

print(zero)

assert(str(zero)) == '0'
assert(str(one)) == 'S(0)'
assert(str(two)) == 'S(S(0))'

three = two + one
four = NaturalNumber(three)

print(three)
print(two)
assert(str(three)) == 'S(S(S(0)))'

assert(str(three-two)) == 'S(0)'

assert(two >= two) == True
assert(str(three % two)) =='S(0)'
assert(str(four % two)) == '0'
assert(isPrime(three)) == True