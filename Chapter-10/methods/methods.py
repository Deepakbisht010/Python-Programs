# file Methods are use to perform any specific task in  file handling.
# f.readlines()  used for rading all lines from file.
f=open("methods/demo.txt","r")

lines=f.readlines()  #it is used to read all lines from the file.

print(lines)

f.close()


#f.readline() USE to read a particular line(means use to read a single line)
f=open("methods/demo.txt","r")

line1=f.readline()   
print(line1)

line2=f.readline()
print(line2)

line3=f.readline()
print(line3)


f.close()