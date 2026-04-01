# Ouestion : Take 5 numbers as input from the user, store them in a list, and print the largest number,sum of list elements and print the list in asending oreder .

number_list=[]
num1=int(input("Enter number 1 : "))
number_list.append(num1)

num2=int(input("Enter number 2 : "))
number_list.append(num2)

num3=int(input("Enter number 3 : "))
number_list.append(num3)

num4=int(input("Enter number 4 : "))
number_list.append(num4)

num5=int(input("Enter number 5 : "))
number_list.append(num5)

print(number_list)
sum_list=sum(number_list)
print(f"the sum of list is: {sum_list}")

acen=number_list.sort()
print(f"The list is asending order : {number_list}")



print("Largest number is : ",max(number_list))