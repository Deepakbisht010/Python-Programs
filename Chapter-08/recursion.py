# Recursion : -
# Recursion is a programming technique in which a function calls itself to solve a problem, and it stops when a base condition is met.

def factorial(n):
    if(n==0 or n==1):   # it is base condition which is very important for stoping infinite recursive nature.
        return 1
    return n*factorial(n-1)  #It calls itself until the condition is met or the task is completed.
    
print(factorial(5))