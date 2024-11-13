class A:
    def disp(self):
        name="manjeet"
        d=20
        print(name)
        print(d)
        
class B(A):
    def show(self):
     self.a=10
     self._b=20
     __c=0
     __c=self.a+self._b
     print(__c)
    
obj=B()
obj.disp()
obj.show()