# Multilevel inheritance means child calss who is already inherit a parent class , it is become or act a parent class for another child calss.

class parent:
    def parent_methodA(self):
        print("This is the parent class.")

class child(parent): #here child class inherit the parent class
    def child_methodB(self):
        print("This is the child class inheriting from parent.")

class grandchild(child):  #here child class become a parent class for grandchild class.
    def grandchild_methodC(self):
        print("This is the grandchild class inheriting from child.")

# Example usage
obj = grandchild()

obj.parent_methodA()
obj.child_methodB()
obj.grandchild_methodC()