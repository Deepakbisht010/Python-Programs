# Exception handling maens hadle these cases which can throw error and may be program crash.

# syntax:-
# try:
#     #code which might throw exception.
# except Edxception as e:
#     print(e)

try :
    a=int(input("Enter a no : "))
    b=int(input("Enter a no : "))
    c=a/b
    print(c)
except ZeroDivisionError as e:  #here it show error. so if we want the program  does not throw error then we use it.
    print("You can't divided by zero")