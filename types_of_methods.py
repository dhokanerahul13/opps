#types of method
#1)instasnce method
'''
insidemethod implementation if weare usibng instacne varaible than such type of 
method are called instacne method.
'''

class student:
    def __init__(self,name, marks):
        self.name=name
        self.marks=marks
    def display(self):  #instance method beacuse they are using instance variable 
        print('hi',self.name) 
        print('your marks are:-',self.marks)
    def grade(self):
        if self.marks>=75:
            print('you got distinction')
        elif self.marks>=60:
            print('you got first class') 
        elif self.marks>=35:
            print('you are passs')
        else:
            print('failed............')
stu1=student('lalit',85)
stu2=student('rahuol',65)
stu3=student('amol',29)        
stu1.grade()
stu2.grade()
stu3.grade()                     


#instance method
'''
setter/mutator method
getter/accessor method
'''
print('######################################')
class student:
    def __init__(self,age=0):
        self.age=age
    def get_age(self):   #getter/accessor method
        return self.age
    def set_age(self,x):#settor/ mutator method
        self.age=x       
raj=student()
print(raj.get_age())
#setting the age using setter method.
raj.set_age(28)
#gettong a age using get method.
print(raj.get_age())

'''
setter method can be used to set values to the insatnce variable
def setname(self,variablle):
    self.varaibel=variable

#getter
def get_name(self):
    retirn self.name
'''


#class method
'''

 inside method declaration if we are using class varaiable/ static rthan such type of method is called 
 class method.
 we can  decalre class method explicitly by using @class method decorator.
 for class method we should provide cls varable at the tome of declaration.
'''
class Test:
    count=0  #class variabel
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def noofobject(cls):
        print('number of object craetyed for a test class:-',cls.count)    
t=Test() 
t1=Test()       
t.noofobject()

#static method
'''
this is general utility method.
inside  these method we wont use any instance variable or class variable.
here we wont provide any self, cls  argument
we declare static mnethod explicitly by using @staticmethod decorator
'''
print('#############################################################')

class math_calc:
    @staticmethod
    def add(x,y):
        print('sum of two is',x+y)
    @staticmethod
    def multi(x,y):
        print('multiplication of two is',x*y)
x=math_calc()            
x.add(2,3)
x.multi(3,6)
