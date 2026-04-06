# Static methods :
# Sometimes we need a function that does not use the self arguments. We can define a static method like this : -

class Student:
    name="Deepak"
    age=25
    cgpa=9.6
    @staticmethod  #no need to use self or another arguments
    def dataShow():
        print(f"The Name is : {Student.name},Age is : {Student.age} and cgpa is : {Student.cgpa}")
        
stu=Student()
stu.dataShow()