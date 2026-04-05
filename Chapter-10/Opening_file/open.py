# it is use to open a file and reteriving the content or data.
f = open("Opening_file/myfile.txt", "r")

#here content is a variable which is store file data with the help of f.read()
content=f.read() 

#to print file data
print(content)

#it is most important to close the file after reteriving the data
f.close()