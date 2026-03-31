# String function is a predefined function which can for specific task.
  
str="hello programmers. welcome to python programming"
length=len(str)    #to calculate the length of string included space and dots.
print(f"Length of string is : {length}")  

upper=str.upper()    #to convert string in upper case
print(upper)

lower=str.lower()   #to convert string in lower case
print(lower)

check_ends=str.endswith("ing")  #check the string is end with the given letters . it return only true or false value
print(check_ends)

chack_start=str.startswith("ell")  #check the string is start with the given letters . it return only true or false value
print(chack_start)

cp_str=str.capitalize()   #it converts first letter of string in uppercase . Only string's first word's letter
print(cp_str)

rep_str=str.replace("python","object oriented ")  #it help us to replace or change any word to another specific word or letter.
print(rep_str)