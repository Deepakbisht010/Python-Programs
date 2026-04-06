# 📝 Create a Rectangle class.
# The constructor should take length and breadth.
# Create methods to calculate and display the area and perimeter.


class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    
    def display(self):
        print(f"The are of a rectangle is : {self.area()}")
        print(f"The perimeter of a rectangle is : {self.perimeter()}")


length=float(input("Enter the length of the rectangle : "))
width=float(input("Enter the width of the rectangle : "))

a=length
b=width

rec=Rectangle(a,b)
rec.display() #Rectangle.display(rec)

