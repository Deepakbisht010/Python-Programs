# Write a program that asks the user to enter an integer and handles the ValueError if the user enters a string.

try:
    user_input=input("Enter a number : ")
    num=int(user_input)
    print(f"You entered {num}")
    
except ValueError:
    print(f"You enter a string '{user_input}' which is not a number")
    
    
    
    
# Create a program that opens a file and handles the FileNotFoundError if the file does not exist.
try:
    f=open("file.txt","r")
    read=f.read()
    print(read)
except FileNotFoundError:
    print("The file is not found or does not exist")
    

# Write a program using try-except to handle multiple exceptions in a single block

try:
    add="For a addition of two number"
    sub="For a subtraction of two number"
    mul="For a multiplication of two number"
    div="For a division of two number"

    
    print(" :::::Calculator::::")
    print("")
    print(f"1:{add} \n 2:{sub} \n 3:{mul} \n 4:{div}")
  
    choice=int(input("Enter the following number to doing opeartion : "))
   
    # print(f"{choice}")
    
    if(choice==1 or choice==2 or choice==3 or choice==4):
       
    
        user_input1=input("Enter first number  : ")
        user_input2=input("Enter second number : ")
    

        num1=float(user_input1)
        num2=float(user_input2)
    
        match choice:
            case 1:
                print(f"{num1} + {num2} = {num1+num2}")
            
            case 2:
                print(f"{num1} - {num2} = {num1-num2}")
            
            case 3:
                
                print(f"{num1} * {num2} = {num1*num2}")
            
            case 4:
                print(f"{num1} / {num2} = {num1/num2}")

            case _:
                print("Invalid input")
    

    else:
        print(" ❌ Invalid input")
        
    
    file_name=input("Enter the file name : ")
    f=open(f"{file_name}","r")
    read=f.read()
    print(read)
    
    
except ZeroDivisionError:
    print(" ❌You can't divided by zero")
    

except ValueError:
    print(" ❌These are Not a number !")
    
except FileNotFoundError:
    print("❌The file '{file_name}.txt' does not exist please enter a valid file name .")
    




try:
    my_list=[1,2,3]
    print(my_list[2])
    print(my_list[3])

except IndexError:
    print("❌The index is not present in the list .")
    
    
    

    
    

   

    