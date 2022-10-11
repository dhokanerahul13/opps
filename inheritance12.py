#inheritance
'''
the mechanism of deriving a new class from and old one(existing class) such as 
the new class inherit all the members of lod class is called inheritance.

parent class/base class/super class/OLD Cass
child class/ derived class/ sub clASSS/ NEW CLASS.
#TYPES OF INHERITANCE
1) SINGLE INHERITANCE.


#constructor overriding googel oit
'''
#1) SINGLE INHERITANCE.
class Father:  #oldclass/parentclass/super class/base class
    money=1000000
    def show(self):
        print('parent class instacne method')
    @classmethod
    def showmoney(cls):
        print('parent money:-',cls.money)
    @staticmethod
    def stat():
        a=10
        print('parent class stat method',a)
class child(Father):#sub class/ new class/ derived class
    def display(self):
        print('child class instacne method')
c=child()
c.display()    
c.show()    
c.showmoney()
c.stat()
print(c.money)

#constructor in inheritance
'''
by default in inheriatnce  child class constructor wil call
'''
class father:
    def __init__(self):
        self.money=1000
        print('father class constructor')
    def show(self):
        print('father class instacne method') 
class child(father):
    def __init__(self):
        self.money=2000
        print('child class constructor')
    def display(self):
        print('child class instacne method')      
c=child()           
print(c.money)  

#constructor with parameter in inheritance
class father:
    def __init__(self,money):
        self.money=money
        print('father class constructor')
    def show(self):
        print('father class instacne method') 
class child(father):

    def display(self):
        print('child class instacne method',self.money)      
c=child(1000)           
print(c.money)  

'''
constructor overriding
method overriding
operator overriding


#super() method google
'''


#super() metod in inheritance
class father:
    def __init__(self,money):
        self.money=money
        print('father class constructor')
    def show(self):
        print('father class instacne method') 
class child(father):
    def __init__(self,money):
        
        self.money=money
        print('child class constructor')
        super().__init__(money)
    def display(self):
        print('child class instacne method',self.money)      
c=child(1000)           
print(c.money)  


#######################################################################
#2) multi-level inheritance-level of generations
print('###############################################')
class Father:
    def __init__(self):
        print('father class constructor')
    def show(self):
        print('father class ionstance mathod')
class child(father):
    def __init__(self):
        super().__init__(self) #here self is mandatory
        print('child class constructor')
    def showc(self):
        print('child class ionstance mathod')        
class grandchild(child):
    def __init__(self):
        super().__init__()  #here self is not manadatory
        print('grandchild class constructor')
    def showg(self):
        print('grandchild class ionstance mathod')  
g=grandchild()        
g.showg()
g.showc()
g.show()

#######################################################################
#3)hierachical inheritance-one parent multiple child
print('###############################################')
class Father:
    def __init__(self):
        print('father class constructor')
    def show(self):
        print('father class ionstance mathod')
class son(father):
    def __init__(self):
        super().__init__(self) #here self is mandatory
        print('son class constructor')
    def showc(self):
        print('son class ionstance mathod')            
class daughter(father):
    def __init__(self):
        # super().__init__(self) #here self is mandatory
        print('daughter class constructor')
    def showc(self):
        print('daughter class ionstance mathod')            
s=son()
d=daughter()

#####################################################################
#4)multiple inheritance-one child multiple parent
print('###############################################')
class Father1:
    def __init__(self):
        # super().__init__(self)
        print('father1 class constructor')
    def show(self):
        print('father1 class ionstance mathod')
class father:
    def __init__(self):
        super().__init__()
        print('father class constructor')
    def show(self):
        print('father class ionstance mathod')
class mother:
    def __init__(self):
        super().__init__()
        print('mother class constructor')
    def show(self):
        print('mother class ionstance mathod')
class child(mother,father,Father1):
    def __init__(self):
        super().__init__()
        print('child class constructor')
    def show(self):
        print('child class ionstance mathod')        
f=child()        


#5)hybrid inheritacnce
'''
inheeritance
overriding
super()
types of inheritance
'''