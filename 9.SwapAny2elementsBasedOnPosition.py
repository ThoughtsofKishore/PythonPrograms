
l1 = [10, 25, 98, 67, 81, 21]

p1 = int(input("Enter the position1 between (0-5):"))
p2 = int(input("Enter the position2 between (0-5):"))

#Approch1 By tuple
#get = (l1[p2], l1[p1])
#l1[p1], l1[p2] = get


#Approach2 By swap
l1[p1], l1[p2] = l1[p2], l1[p1]

print(l1)