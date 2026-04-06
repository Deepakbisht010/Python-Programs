# constructor is a special method which is automatically run after the created object. It is also called dunder method.

class Student:
  
    def __init__(self, name,age,lan,course):
        self.name=name
        self.age=age
        self.lan=lan
        self.course=course
        
   
    def getdata(self):
        print(f"The name is {self.name} \n")
        print(f"age is : {self.age} \n")
        print(f"language is : {self.lan} \n")
        print(f"course is : {self.course}")  
    
stu=Student("Deepak",20,"Python","Data Science")
stu.getdata() #Student.getdata(stu)