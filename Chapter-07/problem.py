# Write a Python program that takes a username and password as input from the user.
# Allow login only if both the username and password are correct; otherwise, display an appropriate error message.

name="Deepak"
password="Deepak@123"

u_name=input("Enter username : ")
pass_word=input("Enter you Password : ")

if(u_name==name and pass_word==password):
    print("Login successful!")
else:
    print("Invalid username or password.")
    
    
    
About="Hii am  Deepak Bisht from Almora."
if("Deepak" in About):  # the in keyword is use to check that The particular data is present in dataset or string.
    print("Yes this post about Deepak ")


#Write a Python program that takes three numbers as input from the user and prints the largest number among them. also print all bumbers list .
numbers_list=[]
num1=int(input("Enter first number : "))
numbers_list.append(num1)

num2=int(input("Enter second number : "))
numbers_list.append(num2)

num3=int(input("Enter third number : "))
numbers_list.append(num3)

print(f"Your Enterned number list is : {numbers_list}")

if(num1==num2 and num2==num3):
    print("All numbers are equal")

elif(num1>=num2 and num1>=num3):
    print(f"The largest number is : {num1}")
    
elif(num2>=num1 and num2>=num3):
    print(f"The largest number is : {num2}")
    
    
else:
    print(f"The largest number is : {num3}")
       


