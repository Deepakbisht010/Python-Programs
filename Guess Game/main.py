# The program generates a random number between 1 and 100. The user keeps guessing until the correct number is found. After each guess, hints are given (greater/smaller). The game counts attempts, stores wrong guesses, and handles invalid input using exception handling.


import random

User_list=[]

try:
    user_input=input("Guess the number between 1 to 100:")
    num=int(user_input)


    rand=random.randint(1,100)

    # print(rand)

    count=1
    while True:  # whenever the break statement work then the loop is terminated.
        
        
        if(num==rand):
            print(f"You won  Congratulations 👏 😃! The currect number is {rand} and you are reaching at this number at  {count} attempts 👍")  
            print(f"Your Whole attemps is that {User_list}") 
            break
            
        elif num>rand:
                
            User_list.append(num)
                
            num=int(input(f"The number is smaller than {num} \n Enter again :"))
                
            count+=1
                
        elif num<rand:
                
            User_list.append(num)
                
            num=int(input(f"The number is greater than {num} \n Enter again : "))
                
            count+=1
            
except ValueError:
    print("Invalid input! Please enter a number.")
        
        
