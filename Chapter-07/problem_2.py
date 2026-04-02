# Write a Python program that takes the marks of five subjects as input from the user.
# Calculate the percentage based on the total marks, and then print the grade according to the following conditions:

# Percentage 80 or above → Grade A
# Percentage between 60 and 79 → Grade B
# Percentage between 40 and 59 → Grade C
# Percentage below 40 → Fail

print("Enter the marks of five subjects")
hindi = int(input("Hindi marks : "))
english = int(input("English marks : "))
maths = int(input("Maths marks : "))
science = int(input("Science marks : "))
social = int(input("Social marks : "))

percentage=((hindi+english+maths+science+social)/500)*100

if(percentage>=80):
    print("Grade A")
    print(f"::Percentage : {percentage}")
elif(percentage>=60 and percentage<=79):
    print("Grade B")
    print(f"::Percentage : {percentage}")
elif(percentage>=40 and percentage<=59):
    print("::::Grade C::::")
    print(f"::Percentage : {percentage}")
else:
    print("Fail")
    print(f"::Percentage : {percentage}")


print("Thank you")