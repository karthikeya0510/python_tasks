#OOPS CONCEPT
#ABSTRACTION
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

# Concrete class --- WE CANT CREATE ABSTRACT METHOF FOR ABSTRACT CLASSES SO CONCRETE CLASS IS BUILT
class Car(Vehicle):
    
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

# Using the abstraction
my_car = Car()
my_car.start_engine()
my_car.stop_engine()
