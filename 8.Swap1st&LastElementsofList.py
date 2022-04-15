

arr = [1, 2, 3, 4, 5, 6]

# #Approach1
# arr[0], arr[-1]=arr[-1], arr[0]
#
# print(arr)


# #Approach2
# Temp=arr[0]
# arr[0]=arr[-1]
# arr[-1]=Temp
#
# print(arr)


# #Approach3 Using Tuple
#
# get = (arr[-1], arr[0])
# arr[0], arr[-1]=get
#
# print(arr)


# #Approach4 Using *operand
#
# start,*middle,end=arr
# arr=[end,*middle,start]
#
# print(arr)


#Approach5 Using pop, index and append methods of list

start=arr.pop(0)
end=arr.pop(-1)

arr.insert(0, end)
arr.append(start)

print(arr)