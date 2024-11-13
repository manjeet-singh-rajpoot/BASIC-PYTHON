class A:
    def show(self):
        print("welcome")
        
    def show(self,firstname=" "):
        print(firstname)
        
    def show(self,firstname=" ",lastname=" "):
        print(firstname,lastname)

obj=A()
obj.show()
obj.show("raj")
obj.show("raj","singh")