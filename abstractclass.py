# python have predefine module ABC module ,ABC classes know as meta class 
# pvm(python virtual machine ) can't create objects of an abstract class.
# abstract method
# means in abstract class we write abstract class method defination in child class as per requiredment
# we can declare a method as abstract method by using @abstractmethod decoreter
from abc import ABC,abstractmethod

# abstract method ==method without body with pass keyword
# concrete method ==method with body
# we can't create object for abstract class 
# my=classname() we can't do this
  
class studentdetails(ABC):
    @abstractmethod
    def name(self,name):
        pass
    
    @abstractmethod
    def email_number(self,email,number):
        pass
    
    
class studentinformation(studentdetails):
    
    def name(self,name):
        if name=="avinash":
            print("you create code")
        else:
            print("abstract class method run successfully")
        return False
    
    def email_number(self,email,number):
        print("this is student email",email)
        print("this is student number",number)
        

obj=studentinformation()
obj.email_number("avinash@gmail.com",9260929613)
obj.name("aviansh")