class A:
    _a=10        #protected
    __b=30        #private
    def disp(self):
        print(self._a)
        print(self.__b)
        
obj=A()
obj.disp()