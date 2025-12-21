class Point:
    def draw():
        print('to draw')


    def write():
        print('to write')




Point1=Point
Point1.x=10
print(Point1.x)

class Person:
    def __init__(self,name) :
        self.name=name

        
    def talk():
        print('to talk')



person1=Person('ashika')
print(person1.name)