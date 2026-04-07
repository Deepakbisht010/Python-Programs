# Multiple inheritance means a derived class inherits from more than one base class.

class parent1:
    def displayA(self):
        print("This is a Parent class 1")
        
class parent2:
    def displayB(Self):
        print("This is a parent class 2")
        
class child(parent1,parent2):   # here child class inherit 2 parent class properties
    pass

child_obj=child()

child_obj.displayA() # it is inherit or using parent1 class properties
child_obj.displayB() # it is inherit or using parent2 class properties