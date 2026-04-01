# What will be the length of following sets s: -
# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")

#   📝Answer 

s=set()  #empty set
s.add(20)  #int
s.add(20.0) #float
s.add("20") #string


print(s)  #{20, '20'}
print(len(s))  # 20 (int) and 20.0 (float) are equal in value in Python: so the answer is 2 because 20 == 20.0   # True