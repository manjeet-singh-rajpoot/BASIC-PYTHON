class A:
    "manjeet singh "
    def disp(self):
        print("enter 1st num: ")
        a=int(input())
        
        print("enter 2nd num: ")
        b=int(input())
        
        c=a**b
        print("ans : ",c)
obj=A()
obj.disp()
print(obj.__doc__)
print(A.__doc__)