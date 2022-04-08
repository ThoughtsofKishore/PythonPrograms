
l1 = [10, 87, 31, 24, 76]

# Approach1
# Max1 = max(l1)
# l1.remove(Max1)
# Max2 = max(l1)
# print("Second Max Value of List l1 is {}".format(Max2))

# Approach2 By sorting
# l1.sort()
# print("Second Max Value of List l1 is {}".format(l1[-2]))


#Approach3 By using sets
l2 = set(l1)
l2.remove(max(l2))
print(max(l2))


