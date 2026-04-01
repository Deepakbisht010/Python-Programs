#Dictionary :- Dictionary is the collection of key value pairs. It is mutable and unordered. It store multiple data types in a single variable.

students={
    "id" : 1, #here id is Key and 1 is value . it is also be applied for all keys and value.
    "name" :"Deepak",
    "marks": 100,
    "cgpa" :9.2,
    "Address":"Almora"
}

length=students.len()
print(f"The length of Dictionary is {length}") #it provides length of dictionary

print(type(students))  #<class 'dict'>


print(students)