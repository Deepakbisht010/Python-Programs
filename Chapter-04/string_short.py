# We can access specific word with the help of sorting_method . 
# Syntax :-
#        str_name=[starting_index : ending_index]

name="Deepak"
print(name[0:3])  # ending index are not included with result string . here index no. 3 which is "p" are not included with result string 
  
# if we are not add ending index in sort method then .it's  ending_index  is  the length of string .
print(name[0:])   # ending_index= length_of_string(6)

print(name[:4])   #it is same as print(name[0:4])  . by default its satring_index is 0.
