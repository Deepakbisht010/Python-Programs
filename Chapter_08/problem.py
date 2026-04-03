#📝 Write a Python program to print  even numbers or odd numbers  using a for loop.

num=int(input("Enter a number to check that the number is even or odd: "))

for i in range(0,num+1):
    if(num%2==0):
        print(f"{num} is an even number")
        break
    else:
        print(f"{num} is an odd number")
        break
    
    
#📝Take a number N from the user and print the sum of numbers from 1 to N using a loop

num=int(input("Enter a number: "))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(f"The sum of numbers from 1 to {num} is: {sum}")
 
 #using while loop 
i=1
sum=0
while(i<=num):
    sum=sum+i
    i+=1
print(f"The sum of numbers from 1 to {num} is: {sum}")


#📝Take a number from the user and print its multiplication table up to 10 using a loop

num=int(input("Enter a number: "))
i=1
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

#using while loop 
i=1   
while(i<=10):
    print(f"{num} X {i} = {num*i}")
    i+=1
    
# 📝Take a string input from the user and count how many vowels are present using a loop.

vowels="aeiou"
str=input("Enter a string: ")
count=0
for char in range(0,len(str)):
    if(str[char].lower() in vowels):
        count+=1
print(f"The number of vowels in the string is : {count}")  


# 📝Take a number from the user and check whether it is prime or not using a loop.

num=int(input("Enter a number: "))
for i in range(2,num):
    if(num%i==0):
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")
    

# 📝Take 5 numbers as input from the user using a loop and print the largest number.
num=int(input("Enter a number: "))
largest=num
for i in range(1,5):
    num=int(input("Enter a number: "))
    if(num>largest):
        largest=num
print(f"The largest number is: {largest}")



# 📝Take a number N from the user and print first N terms of the Fibonacci series using a loop
num=int(input("Enter  terms : "))
a=0
print(a)
b=1
print(b)
sum=0
for i in range(1,num+1):
    sum=a+b
    print(sum)
    a=b
    b=sum
    
    
# 📝 Print this 
# *
# **
# ***
# ****
# *****

for i in range(1, 6):
    print("*" * i)
    
    
# *****
# ****
# ***
# **
# *

for i in range(5, 0, -1):
    print("*" * i)
    
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
    
    
#     *
#    **
#   ***
#  ****
# *****

for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)
    
    
#     *
#    ***
#   *****
#  *******
# *********

for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
    