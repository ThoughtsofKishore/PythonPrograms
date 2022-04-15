
arr = [1, 2, 3, 4, 5]

#Approach1 by loop
# m = 1
# for i in arr:
#     m *= i


#Approach2 by installing numpy package
import numpy

m = numpy.prod(arr)
print(m)
