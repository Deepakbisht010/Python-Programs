# With statement has a property which is that : don't have to explicity close the file 

with open("with_stmt/file.txt", "r") as f: # it is automatically closed the file after performing opeartions like read, write, append etc.
    data = f.read()
    print(data)
   

#here i am not using f.close() function.
