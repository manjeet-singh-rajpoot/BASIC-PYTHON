                   # default constructor #

class A:
    name="manjeet"
    a=20
    def __init__(self):
        print(self.name)
    def show(self):
        print(self.a)

obj=A()
obj.show()
       
        #parametrized cunstructor#

class A:
    def __init__(self,name,age,address):
        print(name,age,address)

    def show(self):
        name="manjeet"
        print(name)
        
obj=A("raj",22,"ganj")
obj.show()