# Union - make a sets which is not caontain repetative values
s1={12,22,11,34,44,8,6}
s2={12,67,44,25,11}
print(s1.union(s2))  #{34, 67, 6, 8, 11, 12, 44, 22, 25}



#intersection  - it is  sets which is only contain similar elements form both sets.
print(s1.intersection(s2))  #{11, 12, 44}