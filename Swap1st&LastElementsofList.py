
l1 = [24, 69, 87, 32]

#Approach1 length minus one
#l1[0], l1[len(l1) - 1] = l1[len(l1) - 1], l1[0]


#Approach2 by negative indexing
#l1[0], l1[-1] = l1[-1], l1[0]


#Approach3 by tuple
#get = (l1[-1], l1[0])
#l1[0], l1[-1] = get


#Approach4 by *operand
#start, *middle, end = l1
#l1 = [end, *middle, start]


#Approach5 by pop method

firstElement = l1.pop(0)
lastElement = l1.pop(-1)

l1.insert(0, lastElement)
l1.append(firstElement)

print(l1)
