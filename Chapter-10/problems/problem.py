# Take 5 lines of input from the user and store them in a file named user.text
# for i in range(0,5):
#     num=input("Enter the lines: \n")
#     with open("problems/user.txt","a") as f:
#         f.write(num+"\n")
        
        
        
#Copy all the contents of myfile.txt into a new file named copy.txt.
with open("problems/myfile.txt","r") as f:
    data=f.read()
with open("problems/copy.txt","w") as f:
    f.write(data)
    
    
    