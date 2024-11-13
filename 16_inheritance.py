                  #single inheritance#
'''
class father:
    name="mr. shiv singh"
    age=44
    land=15
    
    def disp(self):
        print("name : ",self.name)
        print("age : ",self.age)
        print("land : ",self.land)
        
class son(father):
    def show(self):
        print("name : ",self.name)
        print("age: ",self.age)
        print("land: father has 15 ekar land")
        
obj=son()
obj.disp()
obj.show()'''
               #multi level inheritance#
'''
class parent:
    surname="singh"
    def disp(self):
         print("manjeet",self.surname)
         
class child1(parent):
    def show(self):
        print("raj",self.surname)
        
class child2(child1):
    def display(self):
        print("mani",self.surname)
        
obj=child2()
obj.disp()
obj.show()
obj.display() '''
    #multiple inheritance #
'''
class A:
    back="java & DB "
    def backend(self):
        print("development using ",self.back)
class B:
    front="React js & Mongo DB"
    def frontend(self):
        print("frontend development using ",self.front)
class c(A,B):
    def show(self):
         print("good after noon developers")
         print("our new project is Tik Tok")
    
obj=c()
obj.backend()
obj.frontend()
obj.show()
 '''
 
            #hierchical inheritance#
class parent:
    a=10
    b=20
    def add(self):
        self.c=self.a+self.b
        print(self.c)
       
class child1(parent):
    def sub(self):
        self.c=self.a-self.b
        print(self.c)
        
class child2(parent):
    def multi(self):
        self.c=self.a*self.b
        print(self.c)
 
obj=child1()
obj2=child2()
obj.add()
obj.sub()
obj2.multi()
       
