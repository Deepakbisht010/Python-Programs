# A python program can think to the file by reading content from it and writing content to it.

# Open a file
f=open("file.txt","r")
content=f.read()
print(content)
f.close()