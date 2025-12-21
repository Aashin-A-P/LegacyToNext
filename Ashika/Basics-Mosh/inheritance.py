class Mammal:
    def walk(self):
        print('to walk')


class Dog(Mammal):
    def bark(self):
        print('barking')
        pass


dog1=Dog()
print(dog1.bark())
print(dog1.walk())