# ✅ list method is a feature of list in python. it is basically used for doing operation in list for different different prespective.

Original_list=["yello", "Green",34, 70.98,True,"deepak"]


updated_list=Original_list.copy()   #copy() method hepl us to  copy original list into another list
print(updated_list)

Original_list.append("Sharma")  #append() method use to addon element in list.
print(Original_list)

value=Original_list.index("Green") # it describe index number of given element
print(value)

Original_list.pop(2)  #remove the index based element with the help of index
print(Original_list)

Original_list.remove("Sharma")  #it remove specific element with the help of it's existing value
print(Original_list)

Original_list.reverse()   #it reverse whole list 
print(Original_list)


list=[4,3,27,29,1,22,6,8,9,7]
list.sort()  #it arrange list in ascending order 
print(list)








