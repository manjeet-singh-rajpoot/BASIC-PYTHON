class A:
    def show(self):
        print("this is a parent class")
        
class B(A):
    def show(self):
        print("this is a child class")
obj=B()
obj.show()