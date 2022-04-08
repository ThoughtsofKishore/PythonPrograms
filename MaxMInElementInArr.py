

arr = [1, 22, 245, 57]

#Approach 1 using max function of python
#print("Maximum value of arr is:", str(max(arr)) + "\nMinimum value of arr is:", str(min(arr)))


#Approach 2

Max = arr[0]
Min = arr[0]

for i in range(len(arr)):
    if arr[i] > Max:
        Max = arr[i]
    elif arr[i] < Min:
        Min = arr[i]
    else:
        pass

print("Max value of arr is: ", Max)
print("Min value of arr is: ", Min)
