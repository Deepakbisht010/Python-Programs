# Inheritance means using properties of another(base claas) class. basically it is use for code reusability.



class Parent:
    def show(self):
        print("This is a  parent class or base class")  # it a method of parent class
        
class child(Parent):  # here  the child class inheriting the parent class.
    def showB(self):
        print("This is a derived class or child calss")   # it a method of child class
        
child_obj=child()
child_obj.show()  # it is the method of parent class but with the help of inheritance we can easily access the parent calss properties in child class

child_obj.showB()  # it is child class methods

