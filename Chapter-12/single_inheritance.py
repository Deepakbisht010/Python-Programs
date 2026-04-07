# Single inheritance is the type of inheritance where a single drived class inherit only one single base class.


class parent:
    def display(self):
        print("It is a base class .")
        
class child(parent):   # a single child class inherit the parent class.
    def show(self):
        print("It is a derived class .")
        
obj = child()

obj.display()  # base class method
obj.show()     # derived class method
