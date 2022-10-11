#types of variable in class
'''
1)instance variable
2)static varaible/class type varaible
3)local varaible
'''
#1) instance variable
'''
 if the vaue of varaible is varied from object to object then such type of variable iare 
 called instance varaible.
'''
#where we can declare instance variable
#1) inside constructor by using self keyword
from typing import Text


class Employee:
    def __init__(self):
        self.eno=101
        self.ename='lalit'  #inside constructor by using self keyword
e=Employee()
print(e.ename)
print(e.eno)        

#2)outside of class by using object referance
class Employee:
    def __init__(self):
        self.eno=101
        self.ename='lalit'  #inside constructor by using self keyword
e=Employee()
print(e.ename)
print(e.eno)   
e.ename='rahul'   #     outside of class by using object referance
print(e.ename)

#3)inside instance  method by  using kelf variable
class Employee:
    def __init__(self):
        self.eno=101
        self.ename='lalit'  
    def show(self):
        self.ename='amol'
        print(self.ename)    #inside instance  method by  using kelf variable
e=Employee()
b=Employee()
print(e.ename)
print(e.eno)   
e.ename='rahul'   #     outside of class by using object referance
print(e.ename)
# e.show()
print(b.ename)
####################################################################################
#accesseing instance variable
#inside of class by using self keword and outside of class by using object referance
class Employee:
    def __init__(self):
        self.eno=101
        self.ename='lalit'  #inside of class by using self keword
e=Employee()
b=Employee()
print(e.ename)
print(e.eno)   
e.ename='rahul'   #     outside of class by using object referance
print(e.ename)

####################################################################################

#2)static variable / class type variable
'''
 #if the value of variabe is not varied from object to object such type of varaibel is called
  static variable/ class tye variable.
#it decalre with in the class directly but outside of method.
#for total class only one copy of static variable will be created and shared by all object.
'''
class Test:
    x=10  # classs type variable
    def __init__(self):
        self.y=20  #instacne varaible

a=Test()
b=Test()
a.x=10
print(a.x) 
print(b.x)    
a.y=10
print(a.y)
print(b.y)   

#where we can declare class type varaibel
'''
1)declare inside of class but ouside of all method.
2)inside of constructor by using class name.
3)inside instnce method by using class name.
4)inside class method by using class name or cls word.*
5)inside static  method by using class name


'''
class Test:
    x=10  #1)declare inside of class but ouside of all method.
    def __init__(self):
        self.y=20  
        Test.z=20  #2)inside of constructor by using class name.
    def show(self):  #instsnce method
        Test.z=40    #3)inside instnce method by using class name.
    @classmethod
    def m1(cls):
        Test.r=30   #4)inside class method by using class name or cls word.*
        cls.r=50
    @staticmethod
    def m2():
        Test.x=40    #5)inside static  method by using class name
a=Test()
b=Test()
a.x=10
print(a.x) 
print(b.x)    
a.y=10
print(a.y)
print(b.y)   


############################################################################
#local varaible
'''
 somtimes to meet temporary requirement of [program we declare variable inside 
 method directly such type of variable are called local varaible

 local varaibe are craeted at the time of method execution  and destroy once method compte.
  local varaible having ocal scpoe so we can not access this variabe outside of method.
'''
class student:
    def m2(self):
        a=1000  #loacl varaiable
        print(a)

    def m3(self):
        print(a)    
s=student()
s.m2()  
s.m3()     