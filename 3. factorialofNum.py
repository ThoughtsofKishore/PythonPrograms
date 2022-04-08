from math import factorial

num = int(input("Enter the value of num: "))

#Approach1 With factorial function from math module

#Factorial = factorial(num)

#print("Factorial of num is:", Factorial)
#Approach2

fact = 1
if num > 0:
    for i in range(1, num+1):
        fact *= i
    print("{} {} {} {}".format("Factorial of number", num, "is", fact))
elif num == 0:
    print("Factorial of 0 is 1")
elif num < 0:
    print("Enter a number >= 0")