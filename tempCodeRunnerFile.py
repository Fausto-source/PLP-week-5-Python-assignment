
class vehicle:
    def move(self):
        return "Car Driving fassst🚗"

class Plane:
    def move(self):
        return"Plane Flying ✈️"
    
class snake:
    def move(self):
        return "A snake Slithers 🐍"
    
##polymorphism in action
    
for transport in [vehicle(), Plane()]:
    print(transport.move())

for animal in [snake()]:
    print(animal.move())