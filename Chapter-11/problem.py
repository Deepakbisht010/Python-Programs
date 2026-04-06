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



# 📝Create a BankAccount class.
# The constructor should take account_holder_name and balance.
# Create methods:

# deposit(amount)
# withdraw(amount)
# show_balance()

class BankAccount:
    def __init__(slef,ac_holder_name,balance):
        slef.ac_holder_name=ac_holder_name
        slef.balance=balance
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance=self.balance-amount
        return self.balance
    
    def show_balance(self):
        print(f"The Accound Holder Name is : {self.ac_holder_name} \n")
        print(f"The balance is : {self.balance}")
        print("")
        
bank=BankAccount("Deepak",10000)
bank.show_balance()

bank.deposit(1000)
bank.show_balance()

bank.withdraw(500)
bank.show_balance()



# 📝Create a Circle class.
# The constructor should take radius.
# Create a method to calculate and display the area of the circle (π = 3.14).

class Circle:
    def __init__(self,radius):
        self.radius=radius
      
    def display(self):
        PI=3.14
        return PI*(self.radius*self.radius)


radius=float(input("Enter the radius of the circle : "))
  
are_cle=Circle(radius)
area_of_circle=are_cle.display() #Circle.display(are_cle)
print(f"The area of the circle is : {area_of_circle}")