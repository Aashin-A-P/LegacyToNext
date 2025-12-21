import package1.ship
from package1.ship import greet,name
from package1 import ship
print(package1.ship.greet())
print(greet())
print(ship.name())