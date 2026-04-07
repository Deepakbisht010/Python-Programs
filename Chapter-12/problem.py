# Create a class Bird with method fly().
# Create child class Penguin that overrides fly().

class bird:
    def fly(self):
        print("The birds is flying")
        
        
class penguin(bird): 
    
    def fly(self):   # here child class override the parent class method
        print("The penguin is not flying")
        
obj_penguin = penguin()
obj_penguin.fly()  # it shows child class methods



# Create classes Father and Mother with their own methods.
# Create child class Child that inherits from both and calls both methods.

class father:
    def father_method(self):
        print("This is a father class")
        
class mother:
    def mother_method(self):
        print("This is a mother class")

        
class child(father,mother):
    def child_method(self):
        print("This is a child class")
        
child_obj=child()
child_obj.father_method()
child_obj.mother_method()
child_obj.child_method()
        
  