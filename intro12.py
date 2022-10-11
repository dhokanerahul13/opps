'''
in python everything is a object.
python class is group of attributes/variables/ and methods/functions.

A Python class is like an outline for creating a new object. An object
 is anything that you wish to manipulate or change while working through the code.

 Class class name:
    constructor
    variable
    method 
'''

from pickle import MARK


l=[1,2,3,4]
print(type(l))

class Employee:   #classs
    def __init__(self):   #constrctor
        self.name='lalit'   #variable/properties
        self.age=30   #instance variable
        self.salary=80000
    def Emp_details(self):  #methods-actions -funtinality
        print(f'my name is {self.name} and my age is {self.age} and i got {self.salary}')  
e=Employee()          #object/class type variable/referance variabe/instance of class
print(e.name)
print(e.age)#accessing instance varaible outside of class using class type variabe.
print(e.salary)
print('######################################')
e.Emp_details()  #accessing method of class using class type variable outside of class

'''
attitutes/properties-are represented by variable which contain data.

 method/action-it perfrmn perticular taks,it is similar to function
constructor-python support specil type of method caled constructor for 
initilizing instance varaible. 
when we crete a objectfor that perticular class the constrctor will call
'''
print('#############################')
class student:
    def __init__(yogesh):
        yogesh.name='rahul'  #varaiable initilize
        print('hello how are you')

s=student()    
print(s.name)    

#classs
#object
#self


#passing data to class varaiable from outside of class
print('#####################################################')
class student:
    def __init__(yogesh,name,age,salary):#poditinal argument
        print('constructor calling')
        yogesh.name=name
        yogesh.age=age
        yogesh.salary=salary
s=student('lalit',28,23478)
print('#####################################################')
class student:
    def __init__(yogesh,name,age,salary=10000):#default argument
        print('constructor calling')
        yogesh.name=name
        yogesh.age=age
        yogesh.salary=salary
s=student('lalit',28,20000)
print(s.salary)
print('#####################################################')
class student:
    def __init__(yogesh,name,age,salary=10000):#keywordargument
        print('constructor calling')
        yogesh.name=name
        yogesh.age=age
        yogesh.salary=salary
s=student(name='lalit',age=28,salary=20000)#
print(s.salary)
d=student(name='lalit',age=28,salary=20000)
e=student(name='lalit',age=28,salary=20000)
print('#####################################################')
# class student:
#     def __init__(yogesh,name,mark*):#keywordargument
#         print('constructor calling')
#         yogesh.name=name
#         yogesh.marks=mark
       
# s=student(name='lalit',mark=(10,20,30,40))
# print(s.salary)