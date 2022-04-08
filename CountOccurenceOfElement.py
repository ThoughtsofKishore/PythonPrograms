

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
