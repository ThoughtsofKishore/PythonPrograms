

str1 = "welcome"

#Approach1
#print(len(str1))

#Approach2 By For loop
# count = 0
# for i in str1:
#     count += 1
#
# print(count)

#Approach3 By while loop
# count = 0
# while str1[count : ]:
#     count += 1
# print(count)


#Approach4 Using Join & Count
print("X".join(str1).count("X") + 1)
