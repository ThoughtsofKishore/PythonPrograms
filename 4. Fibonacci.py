# 0 1 1 2 3 5 8 13 21....

# n1 = 0
# n2 = 1
#
# print(n1)
# print(n2)
#
# for i in range(10):
#     Sum = n1 + n2
#     print(Sum)
#     n1 = n2
#     n2 = Sum


# 0 1 1 2 3 5 8 13 21 34

num = 5

fib1 = 0
fib2 = 1

print(fib1, end=" ")
print(fib2, end=" ")

if num > 2:
    for i in range(1, num-1):
        print(fib1+fib2, end=" ")
        fib1, fib2 = fib2, i
