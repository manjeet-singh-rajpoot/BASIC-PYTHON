from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def disp(self):
        pass

class square(shape):
    def disp(self):
        print("square has 4 sides...")

class circul(shape):
    def disp(self):
        print("circul has circul size...")

obj=square()
obj.disp()

obj2=circul()
obj2.disp()
  