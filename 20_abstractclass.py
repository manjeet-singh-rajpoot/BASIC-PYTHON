from abc import ABC,abstractmethod
class car(ABC):
    def show(self):
        print("every car has 4 wheels")
    @abstractmethod
    def speed(self):
        pass
class maruti(car):
    def speed(self):
        print("it has 100km/h speed")
        
class suzuki(car):
    def speed(self):
        print("it has 70km/h speed")
        
obj=maruti()
obj.show()
obj.speed()

obj2=suzuki()
obj2.show()
obj2.speed()
