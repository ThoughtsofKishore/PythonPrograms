

arr = [41, 22, 57, 8, 4]

ele=0

# #Approach1 Using for loop
# flag=0
# for i in arr:
#     if i==ele:
#         flag=1
#         print("Element Found")
#         break
#
# if flag==0:
#     print("Element not found")


#Approach2 Using in operator
if ele in arr:
    print("Element found")
else:
    print("Element not found")