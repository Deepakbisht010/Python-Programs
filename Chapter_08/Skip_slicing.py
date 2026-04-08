# Skip slicing is used for skip a pariticular number of iteration.

# for i in range(0,100,2):  #here starting point is 0 and ending point is 100 but skip iteration is 2
#     print(i)
    
# ✅slicing with list :-
l=[10,14,12,13,14,67,54,34,89]
for items in range(0,len(l),3):
    print(l[items])
    
    
# ✅Slicing with string
str="Deepak Bisht"
for char in range(0,len(str),2):
    print(str[char])
    
# ✅tuple slicing by for loop
t=(10,12,34,32,"Rahul", 45,"mukesh",78.90,True,False)

for item in range(0,len(t),2):
    print(t[item])
    
#✅ Dictionary slicing by for loop
dict={
    "id":1,
    "name":"deepak",
    "age":20,
    "cgpa":9.2
}
keys=list(dict)  #converts into list :  ['id', 'name', 'age', 'cgpa']
print(keys)

for value in range(0,len(keys),2):
    key=keys[value]
    print(f"{key} : {dict[key]}")
