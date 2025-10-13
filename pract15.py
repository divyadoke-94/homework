from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Concrete classes
class Car(Vehicle):
    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car engine stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started")

    def stop(self):
        print("Bike engine stopped")

# Using abstraction
vehicles = [Car(), Bike()]
for v in vehicles:
    v.start()
    v.stop()