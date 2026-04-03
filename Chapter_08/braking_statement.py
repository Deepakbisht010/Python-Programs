# Breaking statement are use to control the flow of program by specific keywords like break,continue,pass.

#break keyword : - it is use to exit the code of block.
for i in range(0,11):
    if(i==7):  
        break  # The code stops after the 7th iteration.
    print(i)
    
    
#continue keyword : - it is use to skip a particular iteration
for i in range(0,10):
    if(i==4):
        continue  # the specific iteration in skip which is 4
    print(i)


#pass keyword : - it is use to  instruct do nothing. Pass is a null statement in python.
for i in range(0,10):
    pass  # if we are not uses pass keyword then it throw error.

num=0
while(num<=10):
    print(num)
    num=num+1