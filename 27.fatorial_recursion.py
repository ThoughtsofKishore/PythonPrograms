##Function calling the same function is called recursive function

def factorial(n):

    if n == 0 or n == 1:
        return 1

    elif n > 0:
        return n * factorial(n-1)

    elif n < 0:
        return "Does not exist"


num = int(input("Enter the value of num: "))

print("Factorial of " + str(num) + " :", factorial(num))
