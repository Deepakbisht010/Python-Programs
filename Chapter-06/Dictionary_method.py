#The dictionary methods are: -

marks={
    "hindi":89,
    "english":98,
    "math":92,
    "Science":96 
}

#✅.items() #used to return all emements from Dict. dict_items([('hindi', 89), ('english', 98), ('math', 92), ('Science', 96)])
print(marks.items())


#✅.keys() #return a list containing dictonary's keys.   dict_keys(['hindi', 'english', 'math', 'Science'])
print(marks.keys())

#✅.values() #retuns a list containig dictonary's values.  dict_values([89, 98, 92, 96])
print(marks.values())


#✅.update() # The .update() method is  used for updating or overwrite the the dictionary values or elements . if the key is not present in dictgionary that it added a new element in dictionary.
dictionary_update=marks.update({"Science":97})
print(dictionary_update)  # Update Science marks which is 97 . it returns None value
print(marks)     #Also be changed Original dictonary elements because Dicitonary is mutalbe.


#✅get()  # for returns any specific value with the help of keys. if the keys is not present in dictionary then it give us to a none value
print(marks.get("hindi"))



