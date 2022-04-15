

l1 = ["geeks", "for", "geeks", "and", "geeks", "or", "geeks", "kishore", "geeks"]

# Approach1 By loop
# count = 0
#
# for i in l1:
#     if i == "geeks":
#         count += 1
#
# print("{} occur {} times".format("geeks", count))


#Approach2 by count method

#print("{} occur {} times".format("geeks", l1.count("geeks")))


#Approach3 By counter method
from collections import Counter

Dict = Counter(l1)

print("{} occur {} times".format("geeks", Dict["geeks"]))


#-------------------------------------------------------------------------------


arr = [1, 22, 3, 22, 7, 88, 42, 78, 88]

dict1={}

for i in arr:
    occ=arr.count(i)
    dict1[i]=occ

for x in dict1:
    print("{} occured {} time in the list arr".format(x,dict1[x]))
