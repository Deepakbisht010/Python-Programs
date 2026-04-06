# Self  Arguments or parameters  means taking a by default argument which is mosrt important to create a methods in a class. If we don't passing any arguments then program throw error . 

class Employee:
    lang="Python"
    salary=1200000
    def show(self): # without using  self or another arguments then it's  throw error  which was : TypeError: Employee.show() takes 0 positional arguments but 1 was given
    
        print(f"The salary is : {self.salary} and the language is : {self.lang} ")
        
        
obj_emp=Employee()
obj_emp.show()