# Question: Write a Python program that:

# ✅Takes two numbers as input from the user.
# ✅ Calculates the sum of these two numbers.
# ✅ Prints the sum.
# ✅ Then prints the highest number among:
# ✅ First number
# ✅ Second number


a=int(input("Enter First number : "))
b=int(input("Enter Second Number : "))
c=(a+b)
 
print("The sum of given numbers is : " ,c)

print("The highest number is : " ,max(a,b))   #Here the max() function help us to find largesyt number between a and b

