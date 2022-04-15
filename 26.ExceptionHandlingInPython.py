

print("Program is started")

try:
    num1, num2 = 105
    print(num1/num2)

except TypeError:
    print("Executing Except Block. Please provide number separated with comma Ex: 10, 5")

except ZeroDivisionError:
    print("Executing Except Block. The value of divisor cannot be zero. Please provide any other number")

else:
    print("Executing Else block. No exception is encountered.")

finally:
    print("Finally block executed")


print("Program completed")