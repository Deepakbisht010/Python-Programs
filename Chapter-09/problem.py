#📝write a program using funcyion to find greatest of three numbers.

def greatest(a,b,c):
    if(a==b==c):
        return " All bumbers are equal"
    elif(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

print(f"The greatest number amoung {a},{b},{c} is : {greatest(a,b,c)}")



# 📝 Write a program ysing  function to convert Celsius to fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius *9/5)+32
    return fahrenheit

celsius=float(input("Enter temperature in celsius:"))
print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius)}°F")

print("")



#📝Write a recursive function to calculate the sum of first n natural numbers.

def sum_of_natural_numbers(n):
    if(n==0 or n==1):
        return 1
    return n+sum_of_natural_numbers(n-1)

n=int(input("Enter a number:"))
print(f"The sum of first {n} natural numbers is {sum_of_natural_numbers(n)}")

'''
*****
****
***     for n times
**
*
'''

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
    
n=int(input("Enter a number:"))
pattern(n)

#📝Write a pyhton finction to print multiplication table of given number.
def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} X {i} ={n*i}")
        
n=int(input("Enter a number to print multiplication table: "))
multiplication_table(n)