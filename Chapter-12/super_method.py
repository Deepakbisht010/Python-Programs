# Super() method is use to access the method  of a super class in the derived class when we use constructor on class. 

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print(f"The name is {self.name} and age is {self.age} The name is : ")
        
class employee(student):
    def __init__(self,salary,post):
        self.salary=salary
        self.post=post
        
    def display(self):
        print(f"The salary is {self.salary} and post is {self.post}")
        
class teacher(employee):
    def __init__(self,name,age,salary,post):
        super().__init__(name,age)
        employee.__init__(self,salary,post)
        
tech_obj=teacher("Deepak" ,20, 113000,"HR")
tech_obj.display()