

num = 4
Sum = 0
for i in range(1, num):
    if num % i == 0:
        Sum += i

if Sum == num:
    print("{} is a perfect number".format(num))
else:
    print("{} is not a perfect number".format(num))


