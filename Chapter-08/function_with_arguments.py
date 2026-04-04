#Function can be created with taking arguments .
def fun1(name):  #here name is a argument which is taken at the calling time.
    print(f"welcome back {name}")
    
fun1("Deepak Singh")  #use function with arguments



#with return arguments
def sum(a,b):
    return a+b #here return keyword return a+b sum

a=int(input("Enter a number : "))
b=int(input("Enter a number : "))

print(f"Sum of two numbers is {sum(a,b)}")  #using at calling time with throw a,b values also called arguments.


#default arguments : -
# When we do not want to pass certain arguments, we use default arguments.

def GoodDay(name , ends_with="Thank You"):  #here "Thank You " is a default arguments 
    print(f"Hello {name}, Welcome to python programming !\n {ends_with}")
 
ends_with="Nice to meet you !"   
name=input("Enter your name : ")
GoodDay(name) # it use default arguments without passing ends_with arguments.
GoodDay("Rahul" , ends_with) #Since we are passing the ends_with argument, the function will not use the default value.

