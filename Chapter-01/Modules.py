# module : module is a file containing code written by somebody else which can be imported and use in our program . 
# How to use it : Firstly we install a Module just like Flask. pyjoke,pyttsx3 etc with the help of pip command . here i am using pyjoke module 

#import module in top
import pyjokes

# assign in a variable or store in a variable to print it.
joke=pyjokes.get_joke()

# printing the statements
print(joke)