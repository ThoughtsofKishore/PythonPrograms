
l1 = [1, 68, 96, 14, 7, 52, 34]

n = int(input("Enter the number you want to search:"))

#Approach1 by for loop
#flag = 0

#for i in l1:
#    if i == n:
#        print("Found")
#        a = 1
#        break

#if flag == 0:
#    print("Not Found")

#Approach2  using in operator
if n in l1:
    print("Found")
else:
    print("not Found")
