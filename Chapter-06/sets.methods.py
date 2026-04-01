# Here are some sets methods : -

s={12,32,5,6,"ram","raghav",9.7,True}

#✅.add() methods used for adding new elements in sets.
s.add("Deepak")   
print(s) #{32, True, 5, 6, 'ram', 9.7, 12, 'raghav', 'Deepak'}

#✅.remove() methods used for removing any specific elements from sets.
s.remove(32)
print(s)  #{True, 5, 6, 'ram', 9.7, 12, 'raghav', 'Deepak'}

#✅.pop() remove a random elements from sets.
s.pop()
print(s)

# #✅.clear() used for clear the sets.
# s.clear()
# print(s)