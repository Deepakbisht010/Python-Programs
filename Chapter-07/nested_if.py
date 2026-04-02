# Nested if, is the concept in  programming  where we use if under if .

age=int(input("Enter you age : "))
nationality=input("Enter your Nationaliy : ")

if(age>=18):
    if nationality.lower()=="indian" or nationality.lower()=="hindu":  # here .lower() function coverts user input (nationality) into lowercase. if nationality is equal to defined nationality then string will matched and executes true statement.
        print("You can Vote")
    else:
        print("Sorry you can't vote bacause you are not an Indian citizen!")
else:
    print("you can't vote because you are not eligible by age")