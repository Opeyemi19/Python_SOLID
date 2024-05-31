# Ce principe signifie que nous ne devrions pas être dépendants de d'autres interfaces ou de d'autres domaines de notre application. Cela permet de réduire le couplage de notre application pour rendre notre application complètement modulaire et découplée les autre éléments de l'application.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
        
    def stop_engine(self):
        print("Car engine stopped")
        
class Boat(Vehicle):
    def start_engine(self):
        print("Boat engine started")
        
    def stop_engine(self):
        print("Boat engine stopped")
        
def test_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.stop_engine()
    
car = Car()
boat = Boat()

test_vehicle(car)
test_vehicle(boat)