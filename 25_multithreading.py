from time import sleep
from threading import Thread
class A(Thread):
    def run(self):
        for i in range(5):
           print("manjeet")
           sleep(1)

class B(Thread):
    def run(self):
        for i in range(5):
            print("raj")
            sleep(1)

t1=A()
t2=B()

t1.start()
t2.start()
